# Dreamina Martial Arts Test - Prompt V2

This is the corrected prompt. It expands the master-shot IDs into executable visual instructions instead of relying on opaque labels such as `1.1` or `5.6`.

## Why V2

V1 used terms like `1.1式借位冲击` and `5.6式反击转折`, but a video model cannot know what those IDs mean. V2 keeps the IDs for traceability, then immediately explains each technique in concrete camera, blocking, lens, and motion language.

## Action Technique Glossary For The Model

- `11.1 Circle / 绕圈压迫`: the dominant fighter starts the circling movement first; the defender side-steps to keep their chest and face oriented toward the threat. Camera may orbit slightly or use partial over-shoulder framing to show predator-versus-defender pressure.
- `5.3 Pan plus step / 摇拍加移步`: one fighter walks a half-circle or arc while the camera pans with their face and upper body, making the background pillars slide or rotate behind them. The point is to build martial aura and signal that the fight rhythm is about to change.
- `1.3 Track with the actor / 紧跟演员拍摄`: the camera attaches to one fighter, usually near shoulder or hip height, and keeps a constant distance, angle, and height as that fighter moves. Do not treat both fighters as one tangled mass; follow one body so speed and pressure stay readable.
- `1.1 Long-lens effect / 长焦借位冲击`: use compressed perspective, foreground shoulder/head blocking, motion blur, and reaction timing to make a kick or strike appear close to impact while leaving a safe visible gap. The hit is staged and non-contact; the receiver sells the near miss through head turn, torso recoil, and footwork.
- `5.6 Actor and camera turn together / 人机同时转向`: the retreating defender suddenly decides to face the challenge. At the exact pivot, the camera pivots with the defender, so the character's change of direction and the camera's change of direction happen together as one reversal beat.
- `8.5 Stop walking / 停下脚步`: after continuous movement, both fighters stop or freeze for a short breath. The pause makes the audience register that the power relation changed.

## Dreamina Prompt V2

```text
参考图1是角色设定，请保持两位武术演员的身份、服装和体型一致：黑色训练服红腰带的男武者，深靛蓝训练服白色护腕的女武者。参考图2是场景设定，请保持雨夜木质武馆、湿润反光地板、两根木柱、窗外冷蓝雨光和室内暖灯。参考图3是九宫格分镜，只用于理解镜头顺序、人物走位、运动方向、节奏变化和胜负转折；最终视频不要出现九宫格、分镜边框、编号、箭头、标注、黑白草图风格或任何文字。

生成一段5秒、16:9、电影质感的中国武术短视频。两名角色在武馆中央安全对练，无武器、无血腥、无真实接触。重点不是连续乱打，而是清楚展示：对峙、绕圈压迫、贴身跟拍、借位高踢、转向反击、停顿定格。

请按以下镜头技术执行，编号只作为创作来源，不要把编号或文字显示在视频里：

1）11.1「绕圈压迫」：男武者先启动绕圈，慢慢沿弧线逼近；女武者用侧步调整位置，始终保持胸口和视线正对男武者。摄影机轻微环绕，或从女武者肩后保留男武者的压迫感，明确表现“进攻者像猎手，防守者在守位”。

2）5.3「摇拍加移步」：男武者继续走半圆弧线，摄影机跟着他的脸和上半身摇拍，让背景木柱和雨窗在他身后横向滑动、旋转，形成气场增强的效果。这个镜头不是普通走路，而是用演员移步加摄影机摇拍制造开战前的蓄势。

3）1.3「紧跟演员拍摄」：随后摄影机切到女武者肩侧或腰侧，保持固定高度、固定距离、固定侧后角度，紧跟女武者的脚步、手型和呼吸移动。不要把两个人拍成混乱的一团；镜头贴住女武者，让观众感觉跟着她闪避和判断节奏。

4）1.1「长焦借位冲击」：男武者从画面侧面踢出一记高踢。使用长焦压缩空间，让脚看起来非常接近女武者头侧；用女武者肩膀或头部边缘遮住真实空隙，同时加入脚部运动模糊、衣料摆动和女武者同步转头/后撤反应，制造“几乎踢中”的冲击感。必须保持安全距离，不要真实打中，不要出现受伤或血腥。

5）5.6「人机同时转向」：女武者从后撤瞬间改变方向，不再继续退，而是以脚步 pivot 转身面对男武者；摄影机在同一瞬间跟着她同步转向。角色转向和摄影机转向必须同时发生，让观众感到她从防守变成反击，这是整段的胜负转折点。

6）8.5「停下脚步」：动作结束后，两人突然停在安全距离。女武者掌势稳定，男武者收住攻势并意识到节奏被截断。留一个短暂停顿，能看到呼吸、雨声氛围和地板反光，让观众读懂权力关系已经改变。

最终画面：女武者占据优势但不伤害对手，男武者被迫停住。低机位或中近景定格在克制、非血腥的胜负瞬间。保持全彩真实电影风格，使用参考图3的动作逻辑但不要复制其分镜格式。

避免：分镜格子、文字、编号、箭头、黑白草图、字幕、水印、武器、第三个人、真实接触、血腥、骨折、夸张击飞、身体穿模、瞬移、多余肢体、角色服装漂移、武馆空间漂移、把参考图中的九宫格当成最终画面。
```

## Dreamina CLI Plan

```bash
PROMPT="$(python3 - <<'PY'
from pathlib import Path
text = Path('outputs/dreamina-martial-test/dreamina-prompt-v2.md').read_text(encoding='utf-8')
print(text.split('```text', 1)[1].split('```', 1)[0].strip())
PY
)"

dreamina multimodal2video \
  --image outputs/dreamina-martial-test/assets/character-reference.png \
  --image outputs/dreamina-martial-test/assets/dojo-environment-reference.png \
  --image outputs/dreamina-martial-test/assets/storyboard-reference.png \
  --prompt "$PROMPT" \
  --model_version seedance2.0fast \
  --duration 5 \
  --ratio 16:9 \
  --video_resolution 720p \
  --poll 180
```
