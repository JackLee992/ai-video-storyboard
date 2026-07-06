# Dreamina Martial Arts Test - Prompt V4 Multiframe

This is the recommended next paid test. It changes the control strategy from one `multimodal2video` contact sheet to a `multiframe2video` keyframe sequence.

Do not submit rough storyboard crops directly unless sketch-style output is acceptable. First regenerate or repaint these selected panels as final-color cinematic keyframes:

- `panels/panel_00.png` -> `keyframes/key_01_stance.png`
- `panels/panel_03.png` -> `keyframes/key_02_circle_pressure.png`
- `panels/panel_05.png` -> `keyframes/key_03_visible_kick_contact.png`
- `panels/panel_08.png` -> `keyframes/key_04_counter_stop.png`

## Transition Prompts

### Transition 1 - Stance To Circle Pressure

```text
中国武馆雨夜，保持同一男武者和女武者、同一木质武馆和湿润反光地板。男武者先启动绕圈压迫，沿弧线逼近；女武者侧步守位，胸口和视线始终正对对手。摄影机低机位中景轻微环绕并慢慢推进，背景木柱横向滑动，动作清楚、节奏克制。
```

### Transition 2 - Circle Pressure To Visible Kick Contact

```text
男武者从弧线步伐突然加速踢出高踢，脚真实接触女武者的上臂防守或肩侧护挡。使用长焦压缩和短促摄影机震动强化接触，接触点清楚可见；女武者手臂承受冲击、肩膀后震、脚步滑退半步，衣料和头发有运动反应。非血腥，无武器，身体结构正确。
```

### Transition 3 - Visible Kick Contact To Counter Stop

```text
女武者承受高踢后立刻用脚步 pivot 转身，由防守变反击；摄影机与她同步转向，形成角色和镜头同时改变方向的反击转折。她的掌法或肘部近身真实接触男武者胸前或手臂防线，男武者被迫退半步并停住。最后两人突然静止，女武者占据中心线优势，雨声氛围和地板反光明显。
```

## CLI Plan

```bash
dreamina multiframe2video \
  --images outputs/dreamina-martial-test/keyframes/key_01_stance.png,outputs/dreamina-martial-test/keyframes/key_02_circle_pressure.png,outputs/dreamina-martial-test/keyframes/key_03_visible_kick_contact.png,outputs/dreamina-martial-test/keyframes/key_04_counter_stop.png \
  --transition-prompt "中国武馆雨夜，保持同一男武者和女武者、同一木质武馆和湿润反光地板。男武者先启动绕圈压迫，沿弧线逼近；女武者侧步守位，胸口和视线始终正对对手。摄影机低机位中景轻微环绕并慢慢推进，背景木柱横向滑动，动作清楚、节奏克制。" \
  --transition-prompt "男武者从弧线步伐突然加速踢出高踢，脚真实接触女武者的上臂防守或肩侧护挡。使用长焦压缩和短促摄影机震动强化接触，接触点清楚可见；女武者手臂承受冲击、肩膀后震、脚步滑退半步，衣料和头发有运动反应。非血腥，无武器，身体结构正确。" \
  --transition-prompt "女武者承受高踢后立刻用脚步 pivot 转身，由防守变反击；摄影机与她同步转向，形成角色和镜头同时改变方向的反击转折。她的掌法或肘部近身真实接触男武者胸前或手臂防线，男武者被迫退半步并停住。最后两人突然静止，女武者占据中心线优势，雨声氛围和地板反光明显。" \
  --transition-duration 1.5 \
  --transition-duration 1.7 \
  --transition-duration 1.8 \
  --poll 180
```

## Smaller First/Last-Frame Test

Use this if the next goal is to validate only the kick-contact-to-counter reversal:

```bash
dreamina frames2video \
  --first outputs/dreamina-martial-test/keyframes/key_03_visible_kick_contact.png \
  --last outputs/dreamina-martial-test/keyframes/key_04_counter_stop.png \
  --prompt "中国武馆雨夜，两名武者保持同一身份和服装。男武者高踢真实接触女武者的上臂防守，女武者承受冲击后 pivot 转身反击，摄影机跟随她同步转向，最后两人停住，女武者占据中心线优势。非血腥，无武器，动作清楚，身体结构正确。" \
  --model_version seedance2.0fast \
  --duration 5 \
  --video_resolution 720p \
  --poll 180
```
