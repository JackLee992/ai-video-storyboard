# V5 Flow Multiframe Run QA

## Submission

- Command: `dreamina multiframe2video`
- Submit ID: `52ddbfce-9875-4ae8-bc4c-62e0e6ed4ee4`
- Status: `success`
- Credits: `12`
- Output video: `results/52ddbfce-9875-4ae8-bc4c-62e0e6ed4ee4_video_1.mp4`
- Output spec: `1248x704`, `24fps`, `6.209s`, `mp4`
- Preview sheet: `results/preview_frames/v5-flow-preview-4fps.jpg`

## What Changed From V4

- Segment duration changed from `1.5 + 1.7 + 1.8` to `2 + 2 + 2`.
- Transition prompts now tell the model that each keyframe is a pass-through point, not a pose to stop on.
- Prompts emphasize weight transfer, footwork, hip/waist drive, recoil, recovery, and flowing defense-to-counter movement.
- The language avoids overloading the model with technique IDs or shot jargon during generation.

## Visual QA

From the 4fps preview:

- The approach and circle-pressure phase reads more continuously than V4.
- The high-kick contact beat is still visible in the middle of the video.
- The final counter pose is reached cleanly and preserves the female fighter's advantage.
- Character identity, costume, dojo lighting, and rain-night mood remain stable.

## Remaining Issues

- The kick-to-counter transition is improved but still not fully "martial arts master" fluid; the pivot lacks some waist/hip continuity.
- Contact is visible, but the hit could hold one or two more frames for stronger impact.
- Dreamina still adds an AI-generated watermark.
- The current CLI does not expose a true Seedance 2.0 multiframe model switch.

## Next Best Move

For more "行云流水" choreography, generate two additional in-between keyframes:

1. `key_02b_weight_load.png`: male compresses stance and loads the hip before the high kick.
2. `key_03b_recoil_pivot.png`: female absorbs the kick and begins the pivot counter before the final palm contact.

Then run multiframe with 6 keyframes and shorter, smoother transition durations around `1.1-1.3s` per segment. This should reduce large pose jumps while preserving the reliable multiframe backend.
