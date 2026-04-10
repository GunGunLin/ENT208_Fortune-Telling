# Luckie-Bot: AI Desktop Sprite / 元气算命小精灵 🤖✨

---

## 🌟 Project Vision / 项目愿景

> **"We are not building a tool to predict the future, but a companion that senses your presence and cheers you up through physical interaction."**

**English:** In high-pressure academic and professional environments, prolonged digital work often leads to isolation and burnout. **Luckie-Bot** is an interactive desktop companion designed to break "screen fatigue" through physical rituals and embodied interaction, transforming a cold workspace into a source of positive energy and comfort.

**中文：** 在高压的学术和职业环境中，长期的数字化办公容易导致心理孤立和职业倦怠。**Luckie-Bot** 是一款互动式桌面精灵，旨在通过物理仪式和具身交互打破“屏幕疲劳”，将冰冷的桌面转化为一个充满温情与正能量的治愈空间。

---

## 🛠️ Hardware List (BOM) / 硬件清单

| Component / 组件 | Model / 型号 | Primary Function / 核心功能 |
| :--- | :--- | :--- |
| **Brain / 大脑** | `M5StickC PLUS` | Logic, Wi-Fi, Sprite expressions & fortune display. / 处理逻辑、Wi-Fi、显示表情与运势。 |
| **Presence / 存在感应** | `PIR (AS312)` | Senses user proximity to trigger proactive greetings. / 感知用户靠近，实现主动唤醒。 |
| **Ritual / 交互仪式** | `ToF (VL53L0X)` | Recognizes "hand-petting" for energy sync. / 激光测距，识别“摸摸头”手势进行能量同步。 |
| **Tuning / 主题调频** | `Mini Angle Unit` | Physical rotary dial to select categories (Career, Luck, etc.). / 物理旋钮，选择不同的运势维度。 |
| **Aura / 情绪气场** | `RGB LED Strip` | SK6812 strip for dynamic emotional lighting feedback. / SK6812 灯带，展示实时心情。 |
| **Hub / 神经中枢** | `PaHub (I2C)` | Manages multiple sensors through a single I2C bus. / 扩展接口，确保多个传感器稳定运行。 |

> **[TIP]** For prototyping, the ToF sensor can be substituted with an **Ultrasound sensor** if laser ranging is unavailable.  
> 在原型开发阶段，如果激光测距模块不可用，ToF 传感器可由**超声波传感器**替代。

---

## 🔄 Interaction Workflow / 运行流程

1.  **Proactive Greeting / 主动唤醒** When the PIR sensor detects the user, Luckie-Bot wakes up and shakes its "body" to say hello.  
    当 PIR 传感器检测到用户回到座位，Luckie-Bot 睁开眼并在屏幕上抖动身体打招呼。
2.  **Category Selection / 命运调频** Rotate the Angle dial to choose a focus area (e.g., Daily Energy, Career Luck).  
    用户旋转 Angle 旋钮，在屏幕上切换关注领域（例如：今日元气、职场锦鲤）。
3.  **Energy Sync Ritual / 能量同步** Hover hand over the ToF sensor. LEDs pulse and a progress bar fills up, simulating a "spiritual energy transfer."  
    将手悬停在 ToF 传感器上方。LED 灯带汇聚光芒，模拟“同步能量”的过程。
4.  **AI Insight / 天机解密** Calls the AI API via Wi-Fi to generate a warm, encouraging, and healing message.  
    通过 Wi-Fi 调用 AI API，生成一段温暖、鼓励且不含负面信息的治愈系文字。
5.  **Positive Feedback / 正向反馈** The screen displays the fortune, the LED glows (e.g., gold for luck), and the sprite smiles.  
    屏幕显示运势结果，灯带变换颜色（如金光），精灵显示开心的表情。

---

## 🚀 Key Features / 核心特色

* **Embodied Interaction / 非接触式交互** Uses laser sensing (ToF) for "non-contact petting," adding a sense of mystery and ritual.  
    利用激光雷达（ToF）实现的“隔空抚摸”，增加了互动中的神秘感与仪式感。
* **Emotion-driven AI / 情感驱动 API** Prompts are optimized to ensure only positive, healing, and morale-boosting outputs.  
    所有的反馈都经过 Prompt 优化，确保只输出正向、治愈的内容，有效缓解焦虑。
* **Physical Presence / 物理实体感** Unlike a mobile app, it provides a tangible, "alive" companion on your desk.  
    不同于手机 App，Luckie-Bot 作为一个真实的桌面摆件，提供了更长久的陪伴感。

---

## 🔧 Development / 开发说明

This project is developed using **MicroPython / Arduino (C++)**. The backend connects to an AI Language Model API for generating healing content.

本项目使用 **MicroPython** 进行固件开发，后端接入 **AI 模型 API** 生成治愈语录。

---

<p align="center">Made with ❤️ for a better workspace.</p>
