#!/usr/bin/env python3
"""Build a first-pass AI video storyboard prompt pack from a compact brief."""

from __future__ import annotations

import argparse
import json
import re
import textwrap


def duration_seconds(duration: str) -> float | None:
    match = re.search(r"(\d+(?:\.\d+)?)", duration)
    if not match:
        return None
    value = float(match.group(1))
    lowered = duration.lower()
    if "min" in lowered or "分钟" in lowered:
        return value * 60
    return value


def choose_grid(story: str, requested: str | None, duration: str) -> int:
    if requested and requested != "auto":
        return int(requested)
    text = story.lower()
    seconds = duration_seconds(duration)
    complexity_words = [
        "chase",
        "fight",
        "battle",
        "multiple",
        "crowd",
        "twist",
        "转折",
        "追逐",
        "打斗",
        "多人",
        "群像",
    ]
    word_count = len(story.split())
    cjk_chars = sum(1 for ch in story if "\u4e00" <= ch <= "\u9fff")
    if (
        any(w in text for w in complexity_words)
        or word_count > 180
        or cjk_chars > 280
        or (seconds is not None and seconds > 20)
    ):
        return 25
    if word_count > 90 or cjk_chars > 140 or (seconds is not None and seconds >= 12):
        return 16
    if word_count > 35 or cjk_chars > 60 or (seconds is not None and seconds >= 7):
        return 9
    return 4


def block(text: str) -> str:
    return textwrap.dedent(text).strip()


def build_pack(args: argparse.Namespace) -> dict[str, str | int]:
    grid = choose_grid(args.story, args.grid, args.duration)
    subject = args.subject or "Describe the recurring character, hero object, or main visual subject."
    scene = args.scene or "Describe the key setting, geography, props, and light sources."
    style = args.style or "Specify the final visual style, palette, mood, and realism level."
    negatives = args.negatives or "grid layout, storyboard panels, annotations, timecodes, inconsistent subject identity, unnecessary text"

    shot_text_prompt = block(
        f"""
        Act as a film storyboard director. Turn the idea below into storyboard-ready shot text.

        Use {grid} panels. For every panel include: panel number, shot size, camera angle
        or camera movement, visible subject action, expression or emotional beat, key prop
        or environment cue, and narrative function.

        Vary the rhythm: establish, approach, detail, pressure/reveal, climax, hold.
        Every panel must visibly change through action, pose, expression, framing, camera
        position, or story state. Make the final panel the strongest climax, product hero,
        or emotional freeze.

        Return three sections: Story content; Subject / scene notes; Style notes.

        Idea:
        {args.story}
        """
    )

    storyboard_prompt = block(
        f"""
        Create one horizontal {args.aspect} director storyboard contact sheet using a {grid}-panel film layout.

        Style it as a rough black-and-white pencil storyboard sketch with clear silhouettes,
        readable spatial relations, and loose production drawing quality. Do not make final
        color art, polished comic art, a poster, or a rendered illustration.

        Every panel must show a distinct step in the story. Vary action, pose, expression,
        shot size, camera position, or camera movement. Keep only environment details that
        support the story.

        Add simple annotations: red arrows for subject/object movement, blue arrows for
        camera movement, green marks for composition focus, orange marks for light direction,
        purple marks for emotion/sound/story emphasis, and black text for panel number plus
        a short shot note. No timecodes.

        Story:
        {args.story}

        Subject / scene notes:
        {subject}
        {scene}

        Style notes:
        {style}
        """
    )

    reference_prompt = block(
        f"""
        Create a fully colored {args.aspect} reference sheet for "{args.title}" in the final video style.

        Main subject:
        {subject}

        Setting:
        {scene}

        If the subject is a character, show front, side, and back views on a plain background.
        If it is a product or hero object, show front, side, and top/hero angles. Preserve
        shape, material, colors, signature details, clothing/accessories, and scale. Keep
        contours clear enough for later video reference.

        Final style:
        {style}
        """
    )

    video_prompt = block(
        f"""
        Generate a complete {args.duration} video in {args.aspect}.

        Use the attached storyboard only to understand shot order, subject path, camera
        rhythm, and story progression. Do not output a storyboard, grid, panel layout,
        annotations, panel numbers, black-and-white sketch, or prompt table. The final
        video must be fully colored.

        Sequence:
        {args.story}

        Final style:
        {style}

        Continuity:
        Keep the same subject identity, outfit/object shape, scene geography, lighting
        direction, and color palette across shots.

        Avoid:
        {negatives}
        """
    )

    return {
        "title": args.title,
        "grid": grid,
        "duration": args.duration,
        "aspect": args.aspect,
        "shot_text_prompt": shot_text_prompt,
        "storyboard_image_prompt": storyboard_prompt,
        "reference_asset_prompt": reference_prompt,
        "video_prompt": video_prompt,
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build storyboard-driven AI video prompts.")
    parser.add_argument("--title", required=True, help="Project title.")
    parser.add_argument("--story", required=True, help="Short story, ad concept, or video idea.")
    parser.add_argument("--subject", default="", help="Character, product, or hero object notes.")
    parser.add_argument("--scene", default="", help="Location, props, geography, and light notes.")
    parser.add_argument("--style", default="", help="Final video style, palette, and mood.")
    parser.add_argument("--duration", default="15 seconds", help="Target duration.")
    parser.add_argument("--aspect", default="16:9", help="Aspect ratio.")
    parser.add_argument("--grid", choices=["auto", "4", "9", "16", "25"], default="auto")
    parser.add_argument("--negatives", default="", help="Mistakes to avoid.")
    parser.add_argument("--format", choices=["markdown", "json"], default="markdown")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    pack = build_pack(args)
    if args.format == "json":
        print(json.dumps(pack, ensure_ascii=False, indent=2))
        return

    print(f"# {pack['title']} Prompt Pack")
    print(f"\nGrid: {pack['grid']} panels")
    print(f"Duration: {pack['duration']}")
    print(f"Aspect: {pack['aspect']}")
    for key, heading in [
        ("shot_text_prompt", "Shot Text Prompt"),
        ("storyboard_image_prompt", "Storyboard Image Prompt"),
        ("reference_asset_prompt", "Reference Asset Prompt"),
        ("video_prompt", "Video Prompt"),
    ]:
        print(f"\n## {heading}\n")
        print(pack[key])


if __name__ == "__main__":
    main()
