# Dreamina Martial Arts Test Run

This folder records a real Dreamina CLI test using three inputs:

- `assets/character-reference.png`: character reference generated with built-in imageGen.
- `assets/dojo-environment-reference.png`: environment reference generated with built-in imageGen.
- `assets/storyboard-reference.png`: 9-panel storyboard generated earlier with built-in imageGen.

## Dreamina Submission

- Command: `dreamina multimodal2video`
- Model: `seedance2.0fast`
- Duration: `5`
- Ratio: `16:9`
- Resolution: `720p`
- Credit count reported by Dreamina: `25`
- Submit ID: `4b333123-b5cf-4465-acd7-17e4b9dbb68f`
- Log ID: `2026070610531001017203302173920CC`

## Current Status

The original task was successfully submitted, queued, and then failed during final generation:

- First query: `gen_status=querying`, `queue_status=Queueing`, `queue_idx=3157`
- Second query: `gen_status=querying`, `queue_status=Queueing`, `queue_idx=3115`
- Latest query: `gen_status=fail`, `fail_reason="generation failed: final generation failed"`

Use this command to continue checking and download the result when ready:

```bash
dreamina query_result \
  --submit_id=4b333123-b5cf-4465-acd7-17e4b9dbb68f \
  --download_dir outputs/dreamina-martial-test/results
```

## Prompt

See `dreamina-prompt.md` for the original submitted prompt and full CLI plan.

See `dreamina-prompt-v2.md` for the corrected prompt that expands technique IDs such as `1.1` and `5.6` into concrete camera/blocking instructions. V2 has not been submitted to Dreamina yet.

See `dreamina-prompt-v3-ai-contact.md` for the AI-only contact revision. V3 removes live-action ideas such as "safe gap", "no real contact", and "miss behind the head"; it asks Dreamina for visible fictional contact with camera and performance impact.

See `dreamina-prompt-v4-multiframe.md` for the recommended next test. V4 changes the control method from one `multimodal2video` contact sheet to `multiframe2video` keyframes with one short transition prompt per movement segment.

## Storyboard Panel Crops

The original 9-panel storyboard has been split into individual panel crops under `panels/`. These are useful for selecting and repainting final-color keyframes, but they should not be sent directly as final video frames unless sketch-style output is acceptable.

## Diagnosis

See `improvement-analysis.md` for the control-method diagnosis and the recommended workflow for better storyboard restoration.
