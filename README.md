Luckie-Bot: AI Desktop Sprite / 元气算命小精灵 🤖✨

🌟 Project Vision

In high-pressure academic and professional environments, prolonged digital work often leads to isolation and burnout. Luckie-Bot is an interactive desktop companion designed to break "screen fatigue" through physical rituals and embodied interaction, transforming a cold workspace into a source of positive energy and comfort.

🛠️ Hardware List (BOM)

Component

Model

Primary Function

Brain

M5StickC PLUS

Logic, Wi-Fi, Sprite expressions, and fortune display.

Presence

PIR Sensor (AS312)

Senses user proximity to trigger proactive greetings.

Ritual

ToF Sensor (VL53L0X)

Recognizes "hand-petting" gestures for energy sync.

Tuning

Mini Angle Unit

Physical rotary dial to select fortune categories (Career, Luck, etc.).

Aura

RGB LED Strip

SK6812 strip for dynamic emotional lighting feedback.

Hub

PaHub (I2C)

Manages multiple sensors through a single I2C bus.

🔄 Interaction Workflow

Proactive Greeting: When the PIR sensor detects the user, Luckie-Bot wakes up and shakes to say hello.

Category Selection: The user rotates the Angle dial to choose a focus (e.g., Daily Energy, Career Luck).

Energy Sync Ritual: The user hovers their hand over the ToF sensor. LEDs pulse and a progress bar fills up, simulating an "energy transfer."

AI Insight: The hardware calls the AI API via Wi-Fi. The AI generates a warm, encouraging, and healing message.

Positive Feedback: The screen displays the fortune, while the LED strip glows (e.g., gold for great luck) and the sprite smiles.

🚀 Key Features

Embodied Interaction: Uses laser sensing (ToF) for "non-contact petting," adding a sense of mystery and ritual.

Emotion-driven AI: Prompts are optimized to ensure only positive, healing, and morale-boosting outputs.

Physical Presence: Unlike a mobile app, it provides a tangible "alive" companion on your desk.

🌟 项目愿景

在高压的学术和职业环境中，长期的数字化办公容易导致心理孤立和职业倦怠。Luckie-Bot 是一款互动式桌面精灵，旨在通过物理仪式和具身交互打破“屏幕疲劳”，将冰冷的桌面转化为一个充满温情与正能量的治愈空间。

🛠️ 硬件清单

组件

型号

核心功能

主控大脑

M5StickC PLUS

处理逻辑、Wi-Fi 连接、显示精灵表情与运势。

存在感应

PIR 传感器 (AS312)

感知用户靠近，实现小精灵的主动唤醒。

交互仪式

ToF 传感器 (VL53L0X)

激光测距，识别“摸摸头”手势进行能量同步。

主题调频

Mini Angle 单元

物理旋钮，让用户旋转选择不同的运势维度（事业、学业等）。

情绪气场

RGB LED 灯带

SK6812 灯带，通过流光特效展示精灵的实时心情。

神经中枢

PaHub (I2C 扩展)

扩展 I2C 接口，确保多个传感器稳定运行。

🔄 运行流程

主动唤醒: 当 PIR 传感器检测到用户回到座位，Luckie-Bot 睁开眼并抖动身体打招呼。

命运调频: 用户旋转 Angle 旋钮，在屏幕上切换关注领域（例如：今日元气、职场锦鲤、恋爱上岸）。

能量同步: 用户将手悬停在 ToF 传感器 上方（模拟摸头）。LED 灯带开始汇聚光芒，屏幕显示进度条。

天机解密: 硬件通过 Wi-Fi 调用 AI API，生成一段温暖、鼓励且不含负面信息的文字。

正向反馈: 屏幕显示运势，灯带根据结果变换颜色（如好运时闪烁金光），精灵显示开心的表情。

🚀 核心特色

非接触式交互: 利用激光雷达（ToF）实现的“隔空抚摸”，增加了互动中的神秘感与仪式感。

情感驱动 API: 所有的反馈都经过 Prompt 优化，确保只输出正向、治愈的内容，有效缓解焦虑。

物理实体感: 不同于手机 App，Luckie-Bot 作为一个真实的桌面摆件，提供了更长久的陪伴感。

🔧 Development / 开发说明

This project is developed using MicroPython / Arduino (C++). The backend connects to an AI Language Model API for generating healing content.

本项目使用 MicroPython / Arduino (C++) 进行固件开发，后端接入 AI 模型 API 生成治愈语录。

