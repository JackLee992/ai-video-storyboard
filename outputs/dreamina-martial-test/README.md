# Dreamina Martial Arts Test Run

This folder records real Dreamina CLI tests for the martial-arts storyboard workflow.

The first test used three inputs:

- `assets/character-reference.png`: character reference generated with built-in imageGen.
- `assets/dojo-environment-reference.png`: environment reference generated with built-in imageGen.
- `assets/storyboard-reference.png`: 9-panel storyboard generated earlier with built-in imageGen.

The second test used four final-color keyframes:

- `keyframes/key_01_stance.png`
- `keyframes/key_02_circle_pressure.png`
- `keyframes/key_03_visible_kick_contact.png`
- `keyframes/key_04_counter_stop.png`

## V1 Dreamina Submission

- Command: `dreamina multimodal2video`
- Model: `seedance2.0fast`
- Duration: `5`
- Ratio: `16:9`
- Resolution: `720p`
- Credit count reported by Dreamina: `25`
- Submit ID: `4b333123-b5cf-4465-acd7-17e4b9dbb68f`
- Log ID: `2026070610531001017203302173920CC`

## V1 Status

The original task was successfully submitted, queued, and then failed during final generation:

- First query: `gen_status=querying`, `queue_status=Queueing`, `queue_idx=3157`
- Second query: `gen_status=querying`, `queue_status=Queueing`, `queue_idx=3115`
- Latest query: `gen_status=fail`, `fail_reason="generation failed: final generation failed"`

## V4 Multiframe Submission

- Command: `dreamina multiframe2video`
- Inputs: 4 keyframes
- Transition durations: `1.5`, `1.7`, `1.8`
- Total duration: `5.209`
- Output: `1248x704`, `24fps`, `mp4`
- Credit count reported by Dreamina: `10`
- Submit ID: `075a1c71-fa7a-47ab-97b3-78899786259f`
- Result video: `results/075a1c71-fa7a-47ab-97b3-78899786259f_video_1.mp4`
- Preview sheets:
  - `results/preview_frames/multiframe-preview-contact-sheet.jpg`
  - `results/preview_frames/multiframe-preview-4fps.jpg`

## V4 Status

The multiframe task completed successfully:

- `gen_status=success`
- `queue_status=Finish`
- Result downloaded locally.

See `run-v4-qa.md` for the review notes.

## V5 Flow Submission

V5 responds to the problem that V4 has the right story beats but still feels too much like hard interpolation between poses.

- Command: `dreamina multiframe2video`
- Inputs: same 4 keyframes
- Transition durations: `2`, `2`, `2`
- Total duration: `6.209`
- Output: `1248x704`, `24fps`, `mp4`
- Credit count reported by Dreamina: `12`
- Submit ID: `52ddbfce-9875-4ae8-bc4c-62e0e6ed4ee4`
- Result video: `results/52ddbfce-9875-4ae8-bc4c-62e0e6ed4ee4_video_1.mp4`
- Preview sheet: `results/preview_frames/v5-flow-preview-4fps.jpg`

See `run-v5-flow-qa.md` for review notes.

## V6 Positive-Contact Submission

V6 responds to the observation that Dreamina may treat negative terms as active concepts. The generation prompt uses positive physical evidence only: planted feet, hip rotation, locked contact points, guard compression, recoil, and counter-force.

- Command: `dreamina multiframe2video`
- Inputs: 6 keyframes
- Added keyframes:
  - `keyframes/key_02b_weight_load.png`
  - `keyframes/key_03b_contact_recoil.png`
- Transition durations: `1.1`, `1.1`, `1.0`, `1.1`, `1.2`
- Total duration: `5.209`
- Output: `1248x704`, `24fps`, `mp4`
- Credit count reported by Dreamina: `10`
- Submit ID: `4008b6b8-aab1-4605-8295-e8de9aec2485`
- Result video: `results/4008b6b8-aab1-4605-8295-e8de9aec2485_video_1.mp4`
- Preview sheets:
  - `results/preview_frames/v6-positive-contact-preview-4fps.jpg`
  - `results/preview_frames/v6-contact-window-8fps.jpg`

See `run-v6-positive-contact-qa.md` for review notes.

## V7 Refs-Only Submission

V7 tests the lowest-control version requested by the user: only the character reference image and dojo environment reference image are provided. There are no storyboard panels, no keyframes, and no previous video input. The entire action is controlled through a positive-only physical prompt.

- Command: `dreamina multimodal2video`
- Model: `seedance2.0fast`
- Inputs:
  - `assets/character-reference.png`
  - `assets/dojo-environment-reference.png`
- Duration: `6`
- Ratio: `16:9`
- Resolution: `720p`
- Credit count reported by Dreamina: `30`
- Submit ID: `730d89dc-1672-4fe1-98ba-7dedb833f1a7`
- Status: `fail`
- Fail reason: `generation failed: final generation failed`

See `dreamina-prompt-v7-refs-only.md` for the submitted prompt.

## V7b Refs-Only Mini Submission

V7b keeps the same low-control setup but simplifies the action to one 4-second close-contact exchange and uses `seedance2.0mini`.

- Command: `dreamina multimodal2video`
- Model: `seedance2.0mini`
- Inputs:
  - `assets/character-reference.png`
  - `assets/dojo-environment-reference.png`
- Duration: `4`
- Ratio: `16:9`
- Output: `1280x720`, `24fps`, `mp4`, with audio
- Credit count reported by Dreamina: `36`
- Submit ID: `dc2c51df-ebeb-410d-b686-11bb69278be9`
- Result video: `results/dc2c51df-ebeb-410d-b686-11bb69278be9_video_1.mp4`
- Preview sheet: `results/preview_frames/v7b-refs-only-mini-preview-4fps.jpg`

## V8 Refs-Only Dense Exchange Submission

V8 follows the user's request to let the action direction be more creative and denser, while still using only the character and background references. It creates a 6-second close-range exchange with multiple attack-defense turns.

- Command: `dreamina multimodal2video`
- Model: `seedance2.0mini`
- Inputs:
  - `assets/character-reference.png`
  - `assets/dojo-environment-reference.png`
- Duration: `6`
- Ratio: `16:9`
- Output: `1280x720`, `24fps`, `mp4`, with audio
- Credit count reported by Dreamina: `54`
- Submit ID: `a84c3af0-a2cf-4b5e-be8a-c271754f00fa`
- Result video: `results/a84c3af0-a2cf-4b5e-be8a-c271754f00fa_video_1.mp4`
- Preview sheets:
  - `results/preview_frames/v8-refs-only-dense-preview-4fps.jpg`
  - `results/preview_frames/v8-refs-only-dense-contact-8fps.jpg`

See `dreamina-prompt-v8-refs-only-dense.md` and `run-v8-refs-only-dense-qa.md`.

## Seedance 2.0 Attempts

The CLI's `multiframe2video` command does not support `model_version`, so there is no direct way to force the successful multiframe route onto Seedance 2.0 from the current CLI surface.

Two Seedance 2.0 alternatives were tested:

- `multimodal2video --model_version seedance2.0` with 4 keyframes plus the V4 video as a motion rough cut.
  - Submit ID: `7008606c-7ee8-48b3-bae0-478014abd626`
  - Status: `fail`
  - Fail reason: `generation failed: final generation failed`
  - Credit count reported by Dreamina: `80`
- `frames2video --model_version seedance2.0` from the stance keyframe to the counter-stop keyframe.
  - Submit ID: `150886b8-d279-4a1d-9cdc-94f9bb332bb3`
  - Status: `fail`
  - Fail reason: `generation failed: final generation failed`
  - Credit count reported by Dreamina: `48`

Both failures used the `Video40_Pro` backend. The practical route that currently works is still the fast multiframe backend, with more fluid transition prompts and longer segment durations.

## Prompt

See `dreamina-prompt.md` for the original submitted prompt and full CLI plan.

See `dreamina-prompt-v2.md` for the corrected prompt that expands technique IDs such as `1.1` and `5.6` into concrete camera/blocking instructions. V2 has not been submitted to Dreamina yet.

See `dreamina-prompt-v3-ai-contact.md` for the AI-only contact revision. V3 removes live-action ideas such as "safe gap", "no real contact", and "miss behind the head"; it asks Dreamina for visible fictional contact with camera and performance impact.

See `dreamina-prompt-v4-multiframe.md` for the successful multiframe test. V4 changes the control method from one `multimodal2video` contact sheet to `multiframe2video` keyframes with one short transition prompt per movement segment.

## Storyboard Panel Crops

The original 9-panel storyboard has been split into individual panel crops under `panels/`. These are useful for selecting and repainting final-color keyframes, but they should not be sent directly as final video frames unless sketch-style output is acceptable.

## Diagnosis

See `improvement-analysis.md` for the control-method diagnosis and the recommended workflow for better storyboard restoration.
