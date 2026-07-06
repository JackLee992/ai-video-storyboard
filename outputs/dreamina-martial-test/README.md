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

## Prompt

See `dreamina-prompt.md` for the original submitted prompt and full CLI plan.

See `dreamina-prompt-v2.md` for the corrected prompt that expands technique IDs such as `1.1` and `5.6` into concrete camera/blocking instructions. V2 has not been submitted to Dreamina yet.

See `dreamina-prompt-v3-ai-contact.md` for the AI-only contact revision. V3 removes live-action ideas such as "safe gap", "no real contact", and "miss behind the head"; it asks Dreamina for visible fictional contact with camera and performance impact.

See `dreamina-prompt-v4-multiframe.md` for the successful multiframe test. V4 changes the control method from one `multimodal2video` contact sheet to `multiframe2video` keyframes with one short transition prompt per movement segment.

## Storyboard Panel Crops

The original 9-panel storyboard has been split into individual panel crops under `panels/`. These are useful for selecting and repainting final-color keyframes, but they should not be sent directly as final video frames unless sketch-style output is acceptable.

## Diagnosis

See `improvement-analysis.md` for the control-method diagnosis and the recommended workflow for better storyboard restoration.
