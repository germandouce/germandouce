"""CLI para generar una mini portada en Markdown."""

from __future__ import annotations

import argparse
from dataclasses import dataclass


@dataclass(frozen=True)
class Profile:
    name: str
    role: str
    skills: list[str]


def parse_skills(raw: str) -> list[str]:
    """Convierte una cadena CSV en lista limpia de skills."""
    items = [item.strip() for item in raw.split(",")]
    return [item for item in items if item]


def build_cover(profile: Profile) -> str:
    """Construye una portada en Markdown."""
    lines = [
        f"# 👋 Hola, soy {profile.name}",
        "",
        f"**{profile.role}**",
        "",
        "## 🧰 Stack",
    ]

    if profile.skills:
        lines.extend(f"- {skill}" for skill in profile.skills)
    else:
        lines.append("- (por definir)")

    return "\n".join(lines)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Genera una portada de perfil en Markdown")
    parser.add_argument("--name", default="Germán", help="Nombre visible en portada")
    parser.add_argument("--role", default="Developer", help="Rol profesional")
    parser.add_argument(
        "--skills",
        default="Python,Git",
        help="Skills separadas por coma, ej: Python,FastAPI,Docker",
    )
    return parser


def main() -> int:
    args = build_parser().parse_args()
    profile = Profile(name=args.name.strip() or "Germán", role=args.role.strip() or "Developer", skills=parse_skills(args.skills))
    print(build_cover(profile))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
