#!/usr/bin/env python3

from __future__ import annotations

import argparse
import json
from datetime import datetime
from pathlib import Path
from typing import Any


def format_date(date_text: str | None) -> str:
    if not date_text:
        return "Present"

    try:
        parsed = datetime.strptime(date_text, "%Y-%m-%d")
    except ValueError:
        return date_text
    return parsed.strftime("%b %Y")


def format_date_range(start: str | None, end: str | None) -> str:
    if not start and not end:
        return ""
    return f"{format_date(start)} - {format_date(end)}"


def render_basics(data: dict[str, Any]) -> list[str]:
    basics = data.get("basics", {})
    lines: list[str] = []

    name = basics.get("name", "")
    label = basics.get("label", "")
    if name:
        lines.append(f"# {name}")
    if label:
        lines.append(label)
    lines.append("")

    contact_parts = [
        basics.get("email", ""),
        basics.get("phone", ""),
        basics.get("url", ""),
    ]
    contact = " | ".join([part for part in contact_parts if part])
    if contact:
        lines.append(contact)

    location = basics.get("location", {})
    location_parts = [
        location.get("city", ""),
        location.get("region", ""),
        location.get("countryCode", ""),
    ]
    location_line = ", ".join([part for part in location_parts if part])
    if location_line:
        lines.append(location_line)

    summary = basics.get("summary", "")
    if summary:
        lines.append("")
        lines.append("## Summary")
        lines.append(summary)

    profiles = basics.get("profiles", [])
    if profiles:
        lines.append("")
        lines.append("## Profiles")
        for profile in profiles:
            network = profile.get("network", "")
            username = profile.get("username", "")
            url = profile.get("url", "")

            prefix = network
            if username:
                prefix = f"{prefix} ({username})" if prefix else username

            if prefix and url:
                lines.append(f"- {prefix}: {url}")
            elif prefix:
                lines.append(f"- {prefix}")
            elif url:
                lines.append(f"- {url}")

    return lines


def render_work(work: list[dict[str, Any]]) -> list[str]:
    if not work:
        return []

    lines = ["", "## Experience"]
    for job in work:
        name = job.get("name", "")
        position = job.get("position", "")
        date_range = format_date_range(job.get("startDate"), job.get("endDate"))

        if position and name:
            lines.append(f"### {position} - {name}")
        else:
            lines.append(f"### {position or name}")

        if date_range:
            lines.append(date_range)

        summary = job.get("summary", "")
        if summary:
            lines.append(summary)

        highlights = job.get("highlights", [])
        for highlight in highlights:
            lines.append(f"- {highlight}")

        lines.append("")

    if lines and lines[-1] == "":
        lines.pop()
    return lines


def render_education(education: list[dict[str, Any]]) -> list[str]:
    if not education:
        return []

    lines = ["", "## Education"]
    for entry in education:
        institution = entry.get("institution", "")
        study_type = entry.get("studyType", "")
        area = entry.get("area", "")
        date_range = format_date_range(entry.get("startDate"), entry.get("endDate"))

        title = " - ".join([part for part in [study_type, area] if part])
        if institution and title:
            lines.append(f"### {institution} | {title}")
        else:
            lines.append(f"### {institution or title}")

        if date_range:
            lines.append(date_range)

        url = entry.get("url")
        if url:
            lines.append(url)

        lines.append("")

    if lines and lines[-1] == "":
        lines.pop()
    return lines


def render_skills(skills: list[dict[str, Any]]) -> list[str]:
    if not skills:
        return []

    lines = ["", "## Skills"]
    for skill in skills:
        name = skill.get("name", "")
        level = skill.get("level", "")
        keywords = skill.get("keywords", [])

        header = name
        if level:
            header = f"{header} ({level})" if header else level
        if header:
            lines.append(f"- **{header}**")

        if keywords:
            lines.append(f"  {', '.join(keywords)}")

    return lines


def render_certificates(certificates: list[dict[str, Any]]) -> list[str]:
    if not certificates:
        return []

    lines = ["", "## Certificates"]
    for cert in certificates:
        name = cert.get("name", "")
        issuer = cert.get("issuer", "")
        date_text = format_date(cert.get("date")) if cert.get("date") else ""
        url = cert.get("url", "")

        headline_parts = [part for part in [name, issuer] if part]
        headline = " - ".join(headline_parts)
        if date_text:
            headline = f"{headline} ({date_text})" if headline else date_text
        if headline:
            lines.append(f"- {headline}")
        if url:
            lines.append(f"  {url}")

    return lines


def render_projects(projects: list[dict[str, Any]]) -> list[str]:
    if not projects:
        return []

    lines = ["", "## Projects"]
    for project in projects:
        name = project.get("name", "")
        description = project.get("description", "")
        url = project.get("url", "")

        lines.append(f"- **{name}**" if name else "-")
        if description:
            lines.append(f"  {description}")
        if url:
            lines.append(f"  {url}")

    return lines


def render_languages(languages: list[dict[str, Any]]) -> list[str]:
    if not languages:
        return []

    lines = ["", "## Languages"]
    for entry in languages:
        language = entry.get("language", "")
        fluency = entry.get("fluency", "")
        content = " - ".join([part for part in [language, fluency] if part])
        if content:
            lines.append(f"- {content}")

    return lines


def render_interests(interests: list[dict[str, Any]]) -> list[str]:
    if not interests:
        return []

    lines = ["", "## Interests"]
    for interest in interests:
        name = interest.get("name", "")
        keywords = interest.get("keywords", [])
        if name:
            lines.append(f"- **{name}**")
        if keywords:
            lines.append(f"  {', '.join(keywords)}")

    return lines


def render_references(references: list[dict[str, Any]]) -> list[str]:
    if not references:
        return []

    lines = ["", "## References"]
    for reference in references:
        name = reference.get("name", "")
        content = reference.get("reference", "")
        if name and content:
            lines.append(f"- {name}: {content}")
        elif name:
            lines.append(f"- {name}")
        elif content:
            lines.append(f"- {content}")

    return lines


def render_resume(data: dict[str, Any]) -> str:
    sections: list[str] = []
    sections.extend(render_basics(data))
    sections.extend(render_work(data.get("work", [])))
    sections.extend(render_education(data.get("education", [])))
    sections.extend(render_skills(data.get("skills", [])))
    sections.extend(render_certificates(data.get("certificates", [])))
    sections.extend(render_projects(data.get("projects", [])))
    sections.extend(render_languages(data.get("languages", [])))
    sections.extend(render_interests(data.get("interests", [])))
    sections.extend(render_references(data.get("references", [])))
    return "\n".join(sections).strip() + "\n"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate a Markdown resume from a JSON Resume file."
    )
    parser.add_argument(
        "--input",
        default="resume.json",
        help="Path to the input JSON resume file (default: resume.json).",
    )
    parser.add_argument(
        "--output",
        default="resume.md",
        help="Path to the output Markdown file (default: resume.md).",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    input_path = Path(args.input)
    output_path = Path(args.output)

    if not input_path.exists():
        print(f"Input file does not exist: {input_path}")
        return 1

    try:
        with input_path.open("r", encoding="utf-8") as handle:
            data = json.load(handle)
    except json.JSONDecodeError as exc:
        print(f"Invalid JSON in {input_path}: {exc}")
        return 1

    content = render_resume(data)
    output_path.write_text(content, encoding="utf-8")
    print(f"Resume generated: {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())