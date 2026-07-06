# Dreamina Martial Arts Test - Improvement Analysis

## What Happened

The recorded Dreamina task `4b333123-b5cf-4465-acd7-17e4b9dbb68f` ended with:

```json
{
  "gen_status": "fail",
  "fail_reason": "generation failed: final generation failed"
}
```

The submitted prompt was also the old safety-oriented version. It said "无真实接触", "脚看似擦过但没有接触", and "避免真实打中", which conflicts with the current AI-only martial-arts direction rule: visible fictional contact should be allowed and clearly performed.

## Diagnosis

This is not only a prompt problem. The larger issue is control-method mismatch.

1. **A 9-panel contact sheet is a weak temporal control input.** It is readable to humans, but a video model may treat it as style/composition reference instead of an executable shot list.
2. **5 seconds is too short for 9 panels or 6 techniques.** Nine storyboard beats in 5 seconds gives roughly 0.55 seconds per panel, before any time for anticipation, contact, recoil, or pause.
3. **The original prompt contradicted the action goal.** It asked for martial impact but also banned real contact, so the model had reason to avoid the exact contact/reaction we wanted.
4. **The prompt was overloaded.** One generation request tried to preserve character identity, environment, a contact sheet, shot order, six technique IDs, safe sparring language, negative constraints, and final cinematic style at once.

## External Research Notes

- BytePlus ModelArk lists Dreamina Seedance 2.0 workflows that include text-to-video, image-to-video first frame, and first-and-last-frame generation. Its public docs also describe Seedance 2.0 as supporting multimodal input for images, videos, and audio.
- Dreamina CLI exposes this same distinction locally:
  - `multimodal2video`: all-around reference / 全能参考.
  - `frames2video`: first-and-last-frame video.
  - `multiframe2video`: 2-20 images, with one transition prompt per segment when using 3+ images.
- Runway's official image-to-video guidance says the input image defines composition, subject, lighting, and style, while the prompt should focus on motion, camera work, and temporal progression.
- Google Veo's official first/last-frame workflow explicitly lets the user provide a start image and optional end image for a video.
- Kling's official O1/Omni docs separate element/reference consistency from interaction/action prompts, reinforcing the same pattern: references help identity and scene consistency, while frame/keyframe workflows are better for exact story progression.

## Recommended V4 Workflow

For a 5-second martial-arts test, do not ask the model to perform all 9 storyboard panels. Use 4 final-color keyframes:

1. **Keyframe 1:** duel stance and dojo geography.
2. **Keyframe 2:** circle pressure and defender footwork.
3. **Keyframe 3:** high kick visibly connects with the defender's arm/shoulder guard.
4. **Keyframe 4:** defender pivot counter lands, both fighters stop in a readable power shift.

Then use `dreamina multiframe2video` with 4 images and 3 transition prompts. Each transition should describe only one motion segment.

For strict 1.1 and 5.6 testing, use `dreamina frames2video` with:

- first frame: high kick just before visible contact.
- last frame: defender has pivoted and countered, with both fighters stopped.

This reduces the problem to one controllable interpolation instead of a multi-shot fight.

## Asset Status

The original contact sheet has been split into:

- `panels/panel_00.png` through `panels/panel_08.png`

These crops are rough storyboard panels. For the best next paid run, repaint or regenerate the selected panels as final-color cinematic keyframes before sending them to `multiframe2video`; otherwise the video model may preserve sketch lines, text, panel borders, or annotation artifacts.

## Prompt Rules For Next Run

- Use positive motion instructions first; keep negative constraints short.
- One transition prompt equals one action segment.
- Do not mention "借位", "没打到", "安全空隙", or "假接触" for AI-only output.
- For 5 seconds, limit to 3-4 beats.
- Use visible contact plus reaction: contact point, recoil, foot skid, cloth motion, camera impulse, short pause.
- Keep technique IDs out of the final video prompt unless each ID is expanded into concrete camera/blocking language.
