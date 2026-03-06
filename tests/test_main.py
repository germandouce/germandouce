"""Tests para el generador de portada."""

import unittest

from src.main import Profile, build_cover, parse_skills


class CoverTests(unittest.TestCase):
    def test_parse_skills_ignores_empty_items(self) -> None:
        self.assertEqual(parse_skills("Python, ,FastAPI,,Docker"), ["Python", "FastAPI", "Docker"])

    def test_build_cover_with_skills(self) -> None:
        profile = Profile(name="Germán", role="Backend Developer", skills=["Python", "Docker"])
        markdown = build_cover(profile)
        self.assertIn("# 👋 Hola, soy Germán", markdown)
        self.assertIn("**Backend Developer**", markdown)
        self.assertIn("- Python", markdown)
        self.assertIn("- Docker", markdown)

    def test_build_cover_without_skills(self) -> None:
        profile = Profile(name="Germán", role="Developer", skills=[])
        markdown = build_cover(profile)
        self.assertIn("- (por definir)", markdown)


if __name__ == "__main__":
    unittest.main()
