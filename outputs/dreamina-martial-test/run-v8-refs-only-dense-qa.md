# V8 Refs-Only Dense Exchange QA

## Submission

- Command: `dreamina multimodal2video`
- Model: `seedance2.0mini`
- Submit ID: `a84c3af0-a2cf-4b5e-be8a-c271754f00fa`
- Status: `success`
- Credits: `54`
- Output video: `results/a84c3af0-a2cf-4b5e-be8a-c271754f00fa_video_1.mp4`
- Output spec: `1280x720`, `24fps`, `6.042s`, `mp4`, with audio
- Preview sheets:
  - `results/preview_frames/v8-refs-only-dense-preview-4fps.jpg`
  - `results/preview_frames/v8-refs-only-dense-contact-8fps.jpg`

## Setup

Only two reference images were provided:

- `assets/character-reference.png`
- `assets/dojo-environment-reference.png`

No keyframes, storyboard panels, or previous videos were used.

## Visual QA

Compared with V7b:

- V8 creates a denser exchange, with repeated forearm contact, hand checks, low-line leg contact, and close-range body pressure.
- It feels more like a back-and-forth martial-arts drill than a single pose-to-pose action.
- Character and dojo continuity remain usable.
- Audio is present in the generated file.

Compared with V6:

- V8 has better rhythm and more interaction variety.
- V6 has stronger locked-contact control because it uses explicit contact keyframes.
- V8 is less exact but more alive; V6 is more controlled but more posed.

## Current Takeaway

For Dreamina:

- Character/background references plus rich prompt can produce a lively exchange.
- Heavy, unmistakable contact still benefits from explicit contact keyframes.
- The best next approach is hybrid: use refs-only rich prompting for general rhythm, then generate or select keyframes only for the hardest impact moments.
