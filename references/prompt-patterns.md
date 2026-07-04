# AI Video Storyboard Prompt Patterns

Source inspiration: Heisen AI Lab article, "用GPT Image2故事板+Seedance来掌控视频（附完整提示词）", https://mp.weixin.qq.com/s/eE4_ti3Juz3VMhIqmKaKWw

This reference paraphrases the workflow into reusable patterns. Do not copy the article's long prompt blocks into user deliverables unless the user supplied the text themselves.

## Grid Selection

| Grid | Use For | Typical Duration |
| --- | --- | --- |
| 4 panels | One simple action, reveal, or emotional beat | 3-6 seconds |
| 9 panels | Product/mood piece, short ad, simple travel or lifestyle scene | 8-12 seconds |
| 16 panels | Standard short narrative with clear beginning, middle, ending | 12-20 seconds |
| 25 panels | Multi-character, action-heavy, suspense, chase, fight, or many turns | 20-40 seconds |

## Shot Text Prompt

Use this before image generation:

```text
Act as a film storyboard director. Turn the following idea into storyboard-ready shot text.

Choose 4, 9, 16, or 25 panels based on complexity. For every panel include:
panel number, shot size, camera angle or camera movement, visible subject action,
expression or emotional beat, key prop or environment cue, and narrative function.

Vary the rhythm. Include establishing, movement, detail, pressure/reveal, and ending beats.
Every panel must visibly change through action, pose, expression, framing, camera position,
or story state. The final panel must be the strongest climax, product hero, or emotional hold.

Return three sections:
Story content
Subject / scene notes
Style notes

Idea:
{story}
```

## Storyboard Image Prompt

```text
Create one horizontal 16:9 director storyboard contact sheet using a {grid}-panel film layout.

Style: rough black-and-white pencil storyboard sketch, clear silhouettes, readable spatial
relations, loose production drawing quality. Do not make final color art, a polished comic,
a poster, or a rendered illustration.

Each panel must show a distinct step in the story. Vary action, pose, expression, shot size,
camera position, or camera movement. Keep only environment details that help the story.

Add simple annotations in each panel:
red arrow = subject or object movement
blue arrow = camera movement
green mark = composition or focus
orange mark = light direction
purple mark = emotion, sound, or story emphasis
black text = panel number and a short shot note

No timecodes. Every panel must be numbered. The last panel must be the clearest climax,
product hero, or ending freeze.

Story content:
{story_content}

Subject / scene notes:
{subject_scene_notes}

Style notes:
{style_notes}
```

## Reference Asset Prompts

Character turnaround:

```text
Create a 16:9 character turnaround reference for "{title}".

Subject:
{character_description}

Show the same character from front, side, and back on a plain white or light-gray background.
Preserve face shape, body proportion, clothing, accessories, colors, and signature details.
Use the final video style, fully colored and clean enough to use as an identity reference.
Avoid exaggerated poses unless the project requires them.
```

Product/object reference:

```text
Create a 16:9 product/object reference sheet for "{title}".

Subject:
{product_description}

Show the same object from front, side, and top/hero angle on a plain white or light-gray
background. Preserve shape, size, material, color, surface details, and logo/text rules.
Use the final video style, fully colored, with crisp contours for later video reference.
```

Environment reference:

```text
Create a 16:9 environment reference for "{title}".

Setting:
{environment_description}

Clarify spatial layout, entrances, paths, action zones, windows/light sources, major props,
and landmarks. Keep the scene simple enough for video generation. Use the final video style,
fully colored, with clear lighting and atmosphere.
```

## Video Prompt Pattern

```text
Generate a complete {duration} video in {aspect}.

Use the attached storyboard only to understand shot order, subject path, camera rhythm,
and story progression. Do not output a storyboard, grid, panel layout, annotations, panel
numbers, black-and-white sketch, or prompt table. The final video must be fully colored.

Final style:
{style_notes}

Sequence:
{sequence_summary}

Camera and motion:
{camera_motion_notes}

Continuity:
Keep the same subject identity, outfit/object shape, scene geography, lighting direction,
and color palette across shots.

Avoid:
{negative_constraints}
```

## QA Checklist

Before image generation:
- The story has a visible beginning, change, and ending.
- Grid count matches complexity.
- Each panel has action or camera variation.
- The final panel is the strongest visual memory.

Before video generation:
- The prompt says the storyboard is a reference, not the final look.
- It forbids grid/table/panel/text/annotation artifacts.
- Character, product, or location references are specified when continuity matters.
- Camera motion is concrete and not overloaded.
- Negative constraints remove likely model mistakes without fighting the desired style.
