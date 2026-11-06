import copy
import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from audit_deck import audit, crosscheck_evidence
from render_deck import render, speaker_notes
from install import install

DATA = json.loads((ROOT / "examples/wonderland/presentation.json").read_text(encoding="utf-8"))
DATA_70_30 = json.loads((ROOT / "examples/danilo-wonderland-70-30/presentation.json").read_text(encoding="utf-8"))
E2E = ROOT / "tests" / "e2e"


def _slide(phase, minutes=1, cycle=None, notes="Say this.", **extra):
    s = {"phase": phase, "minutes": minutes, "title": phase, "headline": phase, "speaker_notes": notes,
         "body": ["A risk and a limit"] if phase == "what-if" else ["point"]}
    if phase == "how":
        s["audience_prompt"] = "Try it"
    if cycle:
        s["cycle"] = cycle
    s.update(extra)
    return s


def _deck(slides):
    return {"title": "t", "audience": "a", "medium": "workshop",
            "duration_minutes": sum(s["minutes"] for s in slides), "slides": slides}


class DeckTest(unittest.TestCase):
    def test_valid_example(self):
        errors, warnings = audit(DATA)
        self.assertEqual(errors, [])
        self.assertEqual(warnings, [])

    def test_valid_70_30_example(self):
        errors, warnings = audit(DATA_70_30)
        self.assertEqual(errors, [])
        self.assertEqual(warnings, [])
        self.assertEqual(DATA_70_30["duration_minutes"], 20)
        self.assertEqual(len(DATA_70_30["slides"]), 12)

    def test_sequence_out_of_order(self):
        deck = copy.deepcopy(DATA)
        deck["slides"][2], deck["slides"][4] = deck["slides"][4], deck["slides"][2]
        errors, _ = audit(deck)
        self.assertTrue(any("order" in e.lower() for e in errors))

    def test_duration_mismatch(self):
        deck = copy.deepcopy(DATA)
        deck["duration_minutes"] = 22
        errors, _ = audit(deck)
        self.assertTrue(any("sum" in e.lower() for e in errors))

    def test_missing_phase(self):
        deck = copy.deepcopy(DATA)
        deck["slides"] = [s for s in deck["slides"] if s["phase"] != "how"]
        errors, _ = audit(deck)
        self.assertTrue(any("Missing 4MAT phases" in e for e in errors))

    def test_nested_cycles_valid(self):
        slides = [_slide("mini-what", cycle="frame"), _slide("why", cycle="frame")]
        for m in ("m1", "m2"):
            slides += [_slide(p, cycle=m) for p in ("why", "what", "how", "what-if")]
        slides += [_slide("what-if", cycle="close")]
        errors, _ = audit(_deck(slides))
        self.assertEqual(errors, [])

    def test_nested_cycle_out_of_order_inside_cycle(self):
        slides = [_slide("mini-what", cycle="frame"), _slide("why", cycle="m1"), _slide("how", cycle="m1"),
                  _slide("what", cycle="m1"), _slide("what-if", cycle="m1")]
        errors, _ = audit(_deck(slides))
        self.assertTrue(any("cycle 'm1'" in e for e in errors))

    def test_nested_cycle_must_be_contiguous(self):
        slides = [_slide("mini-what", cycle="a"), _slide("why", cycle="b"), _slide("what", cycle="a"),
                  _slide("how", cycle="c"), _slide("what-if", cycle="c")]
        errors, _ = audit(_deck(slides))
        self.assertTrue(any("not contiguous" in e for e in errors))

    def test_nested_session_must_close_with_what_if(self):
        slides = [_slide("mini-what", cycle="a"), _slide("why", cycle="a"), _slide("what", cycle="a"),
                  _slide("what-if", cycle="a"), _slide("how", cycle="b")]
        errors, _ = audit(_deck(slides))
        self.assertTrue(any("close with what-if" in e for e in errors))

    def test_speaking_rate_overrun_warning(self):
        slides = [_slide(p) for p in ("mini-what", "why", "what", "how", "what-if")]
        slides[2]["speaker_notes"] = "word " * 400
        _, warnings = audit(_deck(slides))
        self.assertTrue(any("overrun" in w for w in warnings))
        _, warnings = audit(_deck(slides), max_wpm=0)
        self.assertFalse(any("overrun" in w for w in warnings))

    def test_mini_what_too_long_warning(self):
        slides = [_slide("mini-what", minutes=3)] + [_slide(p) for p in ("why", "what", "how", "what-if")]
        _, warnings = audit(_deck(slides))
        self.assertTrue(any("MINI WHAT" in w for w in warnings))

    def test_evidence_crosscheck(self):
        ledger = (ROOT / "examples/wonderland/evidence.md").read_text(encoding="utf-8")
        self.assertEqual(crosscheck_evidence(DATA, ledger), [])
        deck = copy.deepcopy(DATA)
        deck["slides"][0]["evidence_ids"] = ["C999"]
        self.assertTrue(any("C999" in e for e in crosscheck_evidence(deck, ledger)))
        self.assertTrue(crosscheck_evidence(DATA, "no ids here"))

    def test_example_ledgers_cover_cited_ids(self):
        for deck, folder in ((DATA, "wonderland"), (DATA_70_30, "danilo-wonderland-70-30")):
            ledger = (ROOT / "examples" / folder / "evidence.md").read_text(encoding="utf-8")
            self.assertEqual(crosscheck_evidence(deck, ledger), [], folder)

    def test_e2e_scenario_decks(self):
        decks = sorted(E2E.glob("*/presentation.json"))
        self.assertGreaterEqual(len(decks), 3)
        for path in decks:
            data = json.loads(path.read_text(encoding="utf-8"))
            errors, _ = audit(data)
            self.assertEqual(errors, [], path.parent.name)
            ledger = path.with_name("evidence.md")
            if ledger.is_file():
                self.assertEqual(crosscheck_evidence(data, ledger.read_text(encoding="utf-8")), [], path.parent.name)

    def test_html_escaping(self):
        deck = copy.deepcopy(DATA)
        deck["slides"][0]["title"] = "<script>alert(1)</script>"
        h = render(deck)
        self.assertIn("&lt;script&gt;alert(1)&lt;/script&gt;", h)
        self.assertNotIn("<script>alert(1)</script>", h)
        self.assertIn("aria-label", h)
        self.assertIn("ArrowRight", h)
        self.assertIn("diagram cycle", h)
        self.assertNotIn("Visual / demonstration:", h)

    def test_render_shows_cycle(self):
        slides = [_slide("mini-what", cycle="frame")] + [_slide(p, cycle="m1") for p in ("why", "what", "how", "what-if")]
        deck = _deck(slides)
        self.assertIn("· m1 ·", render(deck))
        self.assertIn("[m1]", speaker_notes(deck))

    def test_speaker_notes(self):
        txt = speaker_notes(DATA)
        self.assertIn("C010", txt)
        self.assertIn("WHY", txt)
        txt_70_30 = speaker_notes(DATA_70_30)
        self.assertIn("C014", txt_70_30)

    def test_install_dry_run_and_copy(self):
        with tempfile.TemporaryDirectory() as d:
            base = Path(d)
            n = install("claude", scope="project", destination=base, dry_run=True)
            self.assertEqual(n, 16 + 2 + 6)
            self.assertFalse((base / ".claude").exists())
            install("claude", scope="project", destination=base)
            for skill in ("4-mat-to-nlp-presentation", "4mat-start", "4mat-perceptual-positions",
                          "4mat-disney-strategy", "4mat-logical-levels"):
                self.assertTrue((base / f".claude/skills/{skill}/SKILL.md").is_file(), skill)
            self.assertTrue((base / ".claude/skills/4-mat-to-nlp-presentation/references/4mat-architecture.md").is_file())
            self.assertTrue((base / ".claude/agents/devils-advocate.md").is_file())
            self.assertTrue((base / ".claude/agents/nlp-coach.md").is_file())
            self.assertFalse((base / ".claude/agents/perspective-explorer.md").exists())
            self.assertTrue((base / ".4mat-studio/knowledge/4MAT_FOUNDATIONS.md").is_file())
            self.assertTrue((base / ".4mat-studio/knowledge/FORMATS.md").is_file())
            self.assertTrue((base / ".4mat-studio/knowledge/AGENT_CONTRACT.md").is_file())
            self.assertTrue((base / ".4mat-studio/scripts/render_deck.py").is_file())
            with self.assertRaises(FileExistsError):
                install("claude", scope="project", destination=base)

    def test_gemini_no_claude_agents(self):
        with tempfile.TemporaryDirectory() as d:
            install("gemini", scope="project", destination=Path(d))
            self.assertTrue((Path(d) / ".gemini/skills/4-mat-to-nlp-presentation/SKILL.md").is_file())
            self.assertTrue((Path(d) / ".gemini/skills/4mat-start/SKILL.md").is_file())
            self.assertFalse((Path(d) / ".claude/agents").exists())


if __name__ == "__main__":
    unittest.main()
