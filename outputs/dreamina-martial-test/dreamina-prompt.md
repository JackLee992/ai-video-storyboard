# Dreamina Martial Arts Test

## Reference Assets

- `assets/character-reference.png`: two recurring martial artists. Fighter A wears charcoal black with a muted red waist sash. Fighter B wears deep indigo with white wrist wraps.
- `assets/dojo-environment-reference.png`: old wooden training hall at night, wet floor, rain-lit windows, warm lanterns, pillars, open central fighting lane.
- `assets/storyboard-reference.png`: 9-panel storyboard reference for shot order, camera rhythm, action geography, and power shift.

## Action Director Route

- Route: martial arts duel, staged non-graphic action
- Primary techniques: `11.1 Circle`, `5.3 Pan plus step`, `1.3 Track with the actor`
- Support techniques: `1.1 Long-lens effect`, `5.6 Actor and camera turn together`, `8.5 Stop walking`

## Dreamina Prompt

```text
参考图1是角色设定，请保持两位武术演员的身份、服装和体型一致：黑色训练服红腰带的男武者，深靛蓝训练服白色护腕的女武者。参考图2是场景设定，请保持雨夜木质武馆、湿润反光地板、两根木柱、窗外冷蓝雨光和室内暖灯。参考图3是九宫格分镜，只用于理解镜头顺序、人物走位、运动方向、节奏变化和胜负转折；最终视频不要出现九宫格、分镜边框、编号、箭头、标注、黑白草图风格或任何文字。

生成一段5秒、16:9、电影质感的中国武术短视频。两名角色在武馆中央安全对练，无武器、无血腥、无真实接触。

镜头从低机位中远景开始，先建立两人左右对峙和完整空间。男武者先以慢弧线逼近，女武者侧步保持正面对手，形成11.1式绕圈压迫。摄影机轻微环绕并向前推进，背景木柱产生5.3式旋转动势。随后切入贴近女武者肩侧的跟拍，展示脚步、手型和呼吸，保持1.3式贴身运动感。男武者一记高踢从画面侧面掠过，利用长焦压缩和肩部遮挡制造1.1式借位冲击，脚看似擦过但没有接触；女武者顺势后撤半步、转身、以掌势截住节奏，摄影机与她一起转向，形成5.6式反击转折。最后两人停在安全距离，雨声和呼吸感明显，女武者占据优势，画面停在克制、非血腥的胜负瞬间。

画面要求：全彩真实电影风格，使用参考图3的动作逻辑但不要复制其分镜格式。不要分镜格子，不要文字，不要箭头，不要黑白草图。保持角色服装一致，保持武馆空间一致，动作清晰可读，身体结构正确，避免多余肢体、瞬移、穿模、真实打中、夸张血腥、武器、第三个人、字幕和水印。
```

## Dreamina CLI Plan

```bash
dreamina multimodal2video \
  --image outputs/dreamina-martial-test/assets/character-reference.png \
  --image outputs/dreamina-martial-test/assets/dojo-environment-reference.png \
  --image outputs/dreamina-martial-test/assets/storyboard-reference.png \
  --prompt "<prompt above>" \
  --model_version seedance2.0fast \
  --duration 5 \
  --ratio 16:9 \
  --video_resolution 720p \
  --poll 120
```
