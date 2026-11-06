import io
import sys
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import validate_repo


class RepoValidationTest(unittest.TestCase):
    def test_repository_is_valid(self):
        buf = io.StringIO()
        with redirect_stdout(buf):
            code = validate_repo.main()
        self.assertEqual(code, 0, buf.getvalue())

    def test_personal_terms_detected(self):
        errors = []
        validate_repo.check_generic(ROOT / "knowledge" / "x.md", "Open Loop A in Grandfather's workshop with Ogi.", errors)
        self.assertEqual(len(errors), 1)
        self.assertIn("Grandfather", errors[0])
        clean = []
        validate_repo.check_generic(ROOT / "knowledge" / "x.md", "Open Loop A with the presenter's origin story.", clean)
        self.assertEqual(clean, [])

    def test_missing_reference_detected(self):
        errors = []
        validate_repo.check_references(ROOT / "skills" / "4mat-nlp" / "SKILL.md", "Read knowledge/NOPE.md first.", errors)
        self.assertTrue(errors)
        ok = []
        validate_repo.check_references(ROOT / "skills" / "4mat-nlp" / "SKILL.md", "Read knowledge/FORMATS.md.", ok)
        self.assertEqual(ok, [])

    def test_skill_name_rule(self):
        self.assertTrue(validate_repo.SKILL_NAME.match("4-mat-to-nlp-presentation"))
        for bad in ("4MAT-start", "-lead", "trail-", "double--hyphen", "has space"):
            self.assertIsNone(validate_repo.SKILL_NAME.match(bad), bad)

    def test_frontmatter_crlf(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d) / "SKILL.md"
            p.write_bytes(b"---\r\nname: x\r\ndescription: y\r\n---\r\nbody\r\n")
            hdr, _ = validate_repo.parse_header(p)
            self.assertEqual(hdr["name"], "x")


if __name__ == "__main__":
    unittest.main()
