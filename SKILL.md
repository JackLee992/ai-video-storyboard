---
name: ai-video-storyboard
description: Turn a short video idea, script, ad concept, travel mood piece, animation premise, product shot, or AI video prompt into a storyboard-driven production workflow. Use when the user wants controllable AI video prompts for GPT Image/Image2 storyboard generation plus Seedance, Veo, Kling, Runway, or similar video models; needs character/product/environment reference prompts; complains that AI video is unstable, guesses too much, ignores camera direction, changes characters between shots, or lacks cinematic continuity.
---

# AI Video Storyboard

Use this skill to reduce AI-video guesswork by inserting a storyboard layer between the idea and the video model.

## Workflow

1. Normalize the brief.
   - Capture story, subject, setting, style, aspect ratio, target duration, platform, and model if provided.
   - If unspecified, assume `15 seconds`, `16:9`, and a final full-color video. Mention assumptions briefly.
   - If the user only gives a vibe, turn it into a concrete micro-story before prompting image or video models.

2. Expand the idea into shot text.
   - Choose the grid by complexity: `4` for a very short beat, `9` for medium mood/product pieces, `16` for standard short scenes, `25` for multi-character, action-heavy, or high-turning-point scenes.
   - Each panel needs: panel number, shot size, camera angle or movement, visible action, expression or emotional beat, important prop/environment cue, and narrative function.
   - Avoid evenly weighted panels. Build rhythm: establish, approach, detail, pressure, reveal, climax, hold.
   - Make the final panel the clearest climax, product hero, or emotional freeze.

3. Generate the storyboard-image prompt.
   - Ask the image model for one horizontal `16:9` contact sheet with the chosen grid.
   - Use rough black-and-white director sketch language: clear silhouettes and spatial relations, not polished comic art, not final color, not a poster.
   - Require simple annotations: red for subject/object motion, blue for camera movement, green for composition focus, orange for light direction, purple for emotion/sound/story emphasis, black text for panel number plus a short note.
   - Prohibit timecodes. Require panel numbers.

4. Stabilize reusable visual assets before video.
   - For recurring characters: create front/side/back character turnaround prompts on a plain background.
   - For products or hero objects: create front/side/top or hero-angle reference prompts, preserving shape, material, color, and logo/text constraints.
   - For place-driven scenes: create an environment/layout reference prompt that clarifies entrances, paths, windows, counters, stairs, landmarks, and action zones.
   - Match the final video style in these reference images, not the rough storyboard style.

5. Generate the video prompt.
   - Tell the video model that the storyboard is a sequence reference only.
   - Explicitly say not to preserve grid panels, storyboard table layout, black-and-white sketch style, annotations, panel numbers, or timecodes in the final video.
   - Specify final style, key sequence, camera language, subject continuity, motion tempo, lighting/color palette, and negative constraints.
   - Keep prompts direct and visual. Replace generic adjectives with visible behaviors.

6. QA and iterate.
   - Inspect storyboard before generating video: grid count, readable action, shot variety, continuity path, clear light direction, final memory beat, no static repeated panels.
   - Inspect final video prompt: no request to output a storyboard, no contradictory style instruction, subject identity locked, duration/aspect clear, motion not overpacked.
   - If output drifts, fix the storyboard or reference assets first; do not only add more adjectives to the video prompt.

## Resources

- Read `references/prompt-patterns.md` when you need compact prompt templates, a grid-selection table, or a QA checklist.
- Use `scripts/build_prompt_pack.py` when the user provides a structured brief and wants a quick first-pass prompt pack.
