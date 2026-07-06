# V6 Positive-Contact Run QA

## Submission

- Command: `dreamina multiframe2video`
- Submit ID: `4008b6b8-aab1-4605-8295-e8de9aec2485`
- Status: `success`
- Credits: `10`
- Output video: `results/4008b6b8-aab1-4605-8295-e8de9aec2485_video_1.mp4`
- Output spec: `1248x704`, `24fps`, `5.209s`, `mp4`
- Preview sheets:
  - `results/preview_frames/v6-positive-contact-preview-4fps.jpg`
  - `results/preview_frames/v6-contact-window-8fps.jpg`

## Why This Version Exists

The previous prompt used negative terms such as "滑步", "假接触", "借位", "没打到", and "安全空隙" inside avoid clauses. Dreamina appeared to activate those concepts anyway. V6 removes negative action vocabulary from the generation prompt and describes only desired physical evidence:

- feet pressing into the wet floor
- hip rotation driving the leg
- sole and forearm sharing a locked contact point
- guard compression toward the shoulder
- shoulder recoil and hair/cloth response
- counter-force returning through the body

## Added Keyframes

- `keyframes/key_02b_weight_load.png`: male support foot planted, hip loading, knee rising, female shield forming.
- `keyframes/key_03b_contact_recoil.png`: foot pressed into the female guard, forearm compressed, female body beginning the pivot recoil.

## Visual QA

From the 4fps and 8fps previews:

- Contact visibility improved compared with V5.
- The high-kick phase has more body preparation and a clearer impact window.
- The female fighter's guard and shoulder read as receiving force more clearly.
- The final palm counter remains readable.

## Remaining Issue

The sequence still does not fully feel like hard full-contact martial action. The multiframe backend tends to smooth the interaction into a controlled screen fight and shortens the heavy contact hold. The next stronger approach should isolate the contact section as its own shot:

1. Generate a 2-3 second kick-contact shot from `key_02b_weight_load.png` to `key_03b_contact_recoil.png`.
2. Generate a second 2-3 second recoil-counter shot from `key_03b_contact_recoil.png` to `key_04_counter_stop.png`.
3. Stitch the two successful shots instead of asking one generation to solve the entire action phrase.

This keeps the model focused on one body-physics problem at a time.
