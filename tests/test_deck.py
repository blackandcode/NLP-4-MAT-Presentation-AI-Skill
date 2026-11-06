import copy
import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from audit_deck import audit
from render_deck import render, speaker_notes
from install import install

DATA = json.loads((ROOT / "examples/wonderland/presentation.json").read_text(encoding="utf-8"))
DATA_70_30 = json.loads((ROOT / "examples/danilo-wonderland-70-30/presentation.json").read_text(encoding="utf-8"))


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

    def test_speaker_notes(self):
        txt = speaker_notes(DATA)
        self.assertIn("C010", txt)
        self.assertIn("WHY", txt)
        txt_70_30 = speaker_notes(DATA_70_30)
        self.assertIn("C014", txt_70_30)
        self.assertIn("Djedova radionica", DATA_70_30["slides"][0]["diagram"]["nodes"][0])

    def test_install_dry_run_and_copy(self):
        with tempfile.TemporaryDirectory() as d:
            base = Path(d)
            n = install("claude", scope="project", destination=base, dry_run=True)
            self.assertGreaterEqual(n, 24)
            self.assertFalse((base / ".claude").exists())
            install("claude", scope="project", destination=base)
            self.assertTrue((base / ".claude/skills/4-mat-to-nlp-presentation/SKILL.md").is_file())
            self.assertTrue((base / ".claude/skills/4mat-perceptual-positions/SKILL.md").is_file())
            self.assertTrue((base / ".claude/skills/4mat-disney-strategy/SKILL.md").is_file())
            self.assertTrue((base / ".claude/skills/4mat-logical-levels/SKILL.md").is_file())
            self.assertTrue((base / ".claude/skills/4mat-start/SKILL.md").is_file())
            self.assertTrue((base / ".claude/agents/devils-advocate.md").is_file())
            self.assertTrue((base / ".claude/agents/perspective-explorer.md").is_file())
            self.assertTrue((base / ".claude/agents/disney-strategist.md").is_file())
            self.assertTrue((base / ".4mat-studio/knowledge/4MAT_FOUNDATIONS.md").is_file())
            self.assertTrue((base / ".4mat-studio/knowledge/NLP_POCKET_EXERCISES.md").is_file())
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
