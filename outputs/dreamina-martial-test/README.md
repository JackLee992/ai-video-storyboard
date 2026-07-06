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

The task was successfully submitted and is currently queued:

- First query: `gen_status=querying`, `queue_status=Queueing`, `queue_idx=3157`
- Second query: `gen_status=querying`, `queue_status=Queueing`, `queue_idx=3115`

Use this command to continue checking and download the result when ready:

```bash
dreamina query_result \
  --submit_id=4b333123-b5cf-4465-acd7-17e4b9dbb68f \
  --download_dir outputs/dreamina-martial-test/results
```

## Prompt

See `dreamina-prompt.md` for the routed action prompt and full CLI plan.
