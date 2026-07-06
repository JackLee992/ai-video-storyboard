# Dreamina Martial Arts Test - Prompt V3 AI Contact

This prompt reflects the revised `$ai-action-director` rule: for AI-only video generation, martial arts action should use visible fictional contact rather than live-action stunt-safe "misses" or "hidden gaps". It still avoids gore, injury tutorials, broken anatomy, and real-world harm instructions.

## Action Technique Glossary For The Model

- `11.1 Circle / 绕圈压迫`: the dominant fighter starts circling first; the defender side-steps to keep chest and face oriented toward the threat. Camera orbits slightly or uses partial over-shoulder pressure to show predator-versus-defender tension.
- `5.3 Pan plus step / 摇拍加移步`: one fighter walks a half-circle while the camera pans with the face and upper body; background pillars slide or rotate behind them, building martial aura and signaling a rhythm change.
- `1.3 Track with the actor / 紧跟演员拍摄`: the camera attaches to one fighter at shoulder or hip height, preserving constant distance, height, and side angle as that fighter moves. Follow one body rather than the whole pair so speed and pressure stay readable.
- `1.1 Long-lens contact effect / 长焦压缩真实接触`: for AI-only action, the strike visibly connects. Use long-lens compression, foreground overlap, motion blur, body recoil, cloth/hair movement, and camera impulse to make actual contact feel heavier. Do not describe a miss, hidden gap, or "appears to connect".
- `5.6 Actor and camera turn together / 人机同时转向`: the defender changes from retreat to attack; at the exact pivot, the camera pivots with the defender, so body direction and camera direction change together as one reversal beat.
- `8.5 Stop walking / 停下脚步`: after continuous motion, both fighters freeze for a short breath so the audience registers the new power relation.

## Dreamina Prompt V3

```text
参考图1是角色设定，请保持两位武术演员的身份、服装和体型一致：黑色训练服红腰带的男武者，深靛蓝训练服白色护腕的女武者。参考图2是场景设定，请保持雨夜木质武馆、湿润反光地板、两根木柱、窗外冷蓝雨光和室内暖灯。参考图3是九宫格分镜，只用于理解镜头顺序、人物走位、运动方向、节奏变化和胜负转折；最终视频不要出现九宫格、分镜边框、编号、箭头、标注、黑白草图风格或任何文字。

生成一段5秒、16:9、电影质感的中国武术短视频。注意：这是AI生成视频，不是真人现场拍摄，所以动作可以真实接触、真实击中、真实碰撞；不要使用“借位、没打到、安全空隙、假接触”的拍法。所有接触都保持电影化、非血腥、身体结构正确，不要展示现实伤害教程。

动作目标：清楚展示对峙、绕圈压迫、贴身跟拍、长焦压缩真实高踢接触、转向反击、停顿定格。动作要有节奏，不要连续乱打。

请按以下镜头技术执行，编号只作为创作来源，不要把编号或文字显示在视频里：

1）11.1「绕圈压迫」：男武者先启动绕圈，慢慢沿弧线逼近；女武者用侧步调整位置，始终保持胸口和视线正对男武者。摄影机轻微环绕，或从女武者肩后保留男武者的压迫感，明确表现“进攻者像猎手，防守者在守位”。

2）5.3「摇拍加移步」：男武者继续走半圆弧线，摄影机跟着他的脸和上半身摇拍，让背景木柱和雨窗在他身后横向滑动、旋转，形成气场增强的效果。这个镜头不是普通走路，而是用演员移步加摄影机摇拍制造开战前的蓄势。

3）1.3「紧跟演员拍摄」：摄影机切到女武者肩侧或腰侧，保持固定高度、固定距离、固定侧后角度，紧跟她的脚步、手型和呼吸移动。不要把两个人拍成混乱的一团；镜头贴住女武者，让观众感觉跟着她闪避和判断节奏。

4）1.1「长焦压缩真实接触」：男武者从画面侧面踢出一记高踢，这一脚要真实接触女武者的上臂防守或肩侧护挡，而不是踢空。使用长焦压缩空间，让接触点显得更有力量；接触瞬间要有脚部运动模糊、衣料摆动、女武者手臂承受冲击、肩膀后震、脚步滑退半步、摄影机轻微震动和短促停顿。不要血腥，不要骨折，不要夸张击飞；重点是电影化真实接触和可读反应。

5）5.6「人机同时转向」：女武者承受这一击后不继续后退，而是用脚步 pivot 转身面对男武者，同时用掌法或肘部近身反击男武者胸前或手臂防线。摄影机在同一瞬间跟着她同步转向，角色转向和摄影机转向必须同时发生，让观众感到她从防守变成反击，这是整段的胜负转折点。

6）8.5「停下脚步」：反击真实接触后，两人突然停住。女武者掌势稳定，占据中心线；男武者被击退半步、收住攻势，呼吸变重，意识到节奏被截断。留一个短暂停顿，看到呼吸、雨声氛围和地板反光，让观众读懂权力关系已经改变。

最终画面：女武者占据优势，男武者被迫停住但没有严重受伤。低机位或中近景定格在克制、非血腥的胜负瞬间。保持全彩真实电影风格，使用参考图3的动作逻辑但不要复制其分镜格式。

避免：分镜格子、文字、编号、箭头、黑白草图、字幕、水印、武器、第三个人、借位、没打到、安全空隙、假接触、血腥、骨折、夸张击飞、身体穿模、瞬移、多余肢体、角色服装漂移、武馆空间漂移、把参考图中的九宫格当成最终画面。
```

## Dreamina CLI Plan

```bash
PROMPT="$(python3 - <<'PY'
from pathlib import Path
text = Path('outputs/dreamina-martial-test/dreamina-prompt-v3-ai-contact.md').read_text(encoding='utf-8')
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
