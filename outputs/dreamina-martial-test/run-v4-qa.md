# V4 Multiframe Run QA

## Submission

- Command: `dreamina multiframe2video`
- Submit ID: `075a1c71-fa7a-47ab-97b3-78899786259f`
- Status: `success`
- Credits: `10`
- Output video: `results/075a1c71-fa7a-47ab-97b3-78899786259f_video_1.mp4`
- Output spec: `1248x704`, `24fps`, `5.209s`, `mp4`

## Inputs

- `keyframes/key_01_stance.png`: low wide stance, clear geography.
- `keyframes/key_02_circle_pressure.png`: male advances, female side-steps and guards.
- `keyframes/key_03_visible_kick_contact.png`: high kick visibly contacts the female fighter's arm/shoulder guard.
- `keyframes/key_04_counter_stop.png`: female counter visibly contacts the male fighter's chest/guard, ending in a power-shift freeze.

## What Improved

- The video follows the 4-keyframe sequence much better than the earlier contact-sheet approach.
- Character identity and rain-night dojo continuity are stable.
- The high-kick beat appears in the middle of the video rather than being fully ignored.
- The final counter and power shift are more readable than the previous multimodal prompt route.
- The prompt no longer contains "no real contact", "miss", or "safe gap" language.

## Remaining Issues

- Dreamina adds an AI-generation watermark in the upper-left corner.
- The high-kick contact beat is still brief; it appears but does not hold long enough to feel like a hero impact.
- The camera does not fully execute a strong 5.6-style synchronized pivot with the female fighter. It reads more as a conventional fight exchange than a decisive camera-and-actor turn.
- Because `multiframe2video` interpolates between stills, it preserves sequence better than the old route, but it still softens precise camera grammar.

## Next Iteration

For the next paid test, use a smaller first/last-frame segment focused only on the hard beat:

1. First frame: male high kick visibly contacting the female fighter's arm/shoulder guard.
2. Last frame: female pivot counter has landed; both fighters freeze in the power shift.

Use `dreamina frames2video` for this 1.1-to-5.6 beat. This should give the model fewer things to solve and more time to hold the contact/reversal moment.
