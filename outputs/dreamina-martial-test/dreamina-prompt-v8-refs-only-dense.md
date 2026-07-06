# Dreamina Martial Arts Test - Prompt V8 Refs Only Dense Exchange

V8 uses only:

- `assets/character-reference.png`
- `assets/dojo-environment-reference.png`

It tests whether a richer action prompt can create a denser back-and-forth exchange without storyboard panels, keyframes, or previous video input.

## Submitted Prompt

```text
参考图一固定两位武者身份：男武者黑色训练服红腰带，女武者深蓝训练服白色护手。参考图二固定场地：雨夜木质武馆，湿木地板反光，暖灯和蓝色雨光交织。生成一段6秒16:9电影武术短打，动作密集，有来有回，双方都展示攻防判断和身体重量。开场两人已在武馆中央近距离守架，脚掌压住湿木地板，呼吸带动肩背起伏。第一个回合：男武者前脚踏入，左掌压向女武者肩线，右拳贴近中线推进；女武者用白色护手拍开左掌，前臂架住右拳，肘部贴身切进，双方前臂碰撞，衣袖震动。第二个回合：男武者转髋换角度，低位扫腿碰到女武者小腿外侧，女武者提膝挡住，脚底落回地板时溅起水光，同时右掌打在男武者手臂防线上。第三个回合：男武者贴身进半步，用肩背和前臂挤压女武者中心线，女武者沉胯后坐，双手扣住他的手腕和肘线，把力量引到侧面，男武者腰带和衣摆随转身甩动。第四个回合：女武者借侧身空位连续反击，一掌贴上男武者胸前防线，一肘压住他的前臂，接触点在画面中央停留一个重拍；男武者胸口后收，后脚踩实地板稳住身体，立刻用护臂挡回。收束：两人最后一次前臂相撞后同时停住，女武者占据中心线，男武者侧身蓄势，雨声、呼吸、脚底摩擦和衣料震动形成真实打斗质感。镜头低机位中近景，围绕两人半圈移动，跟随每次重心转移，接触瞬间有短促镜头震动，动作连贯、身体结构稳定、每一次攻防都让距离和重心发生变化。
```

## CLI Command

```bash
dreamina multimodal2video \
  --image outputs/dreamina-martial-test/assets/character-reference.png \
  --image outputs/dreamina-martial-test/assets/dojo-environment-reference.png \
  --prompt "$PROMPT" \
  --model_version seedance2.0mini \
  --duration 6 \
  --ratio 16:9 \
  --video_resolution 720p \
  --poll 180
```
