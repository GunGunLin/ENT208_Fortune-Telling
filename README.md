# 🔮 Luckie-Bot · Arcanum Lab (神秘学实验室)

[English](#english) | [中文](#中文)

---

<h2 id="english">English</h2>

Luckie-Bot is a fully immersive intelligent tarot divination system integrating **AI Large Language Models, MediaPipe spatial gesture interaction, a 2D physics engine**, and **IoT hardware (M5StickC)**. 

Through a visually striking "cyber-occult" UI, non-contact gesture card drawing, and external hardware lighting synchronization, this project breaks the boundary between the digital and physical worlds, providing users with a unique "destiny exploration" experience.

### ✨ Core Features

- **🌌 Immersive Gesture Control (MediaPipe)**: Say goodbye to traditional mouse clicks. By capturing gestures via webcam, users can "swipe" through the tarot deck in the void and "make a fist" to channel spiritual energy and lock their card of destiny.
- **🧠 Deep AI Destiny Calculus (DeepSeek-V3)**: Powered by the SiliconFlow API, the system weaves a personalized "Tapestry of Fate" (including deep interpretations, driving insights, and daily challenges) based on the user's birthdate, chosen domain, and the drawn [Past-Present-Future] cards.
- **🔌 Cross-Dimensional Hardware Resonance (M5StickC + LED)**:
  - **Atmosphere Rendering**: Communicates with M5StickC via Web Serial API. When a user selects a domain (e.g., gold for wealth, blue for academic) or enters the meditation phase, the M5StickC drives external RGB LED strips to display synchronized breathing rhythms and color transitions.
  - **Two-Way Synchronization**: The M5StickC hardware can also act as an independent controller to physically synchronize/select the current divination domain.
- **🔮 Vessel of Memories (Matter.js)**: Every divination result is encapsulated into a physical "memory glass orb" that drops into the corner of the screen. Users can flick and click these orbs to trace back their past destiny trajectories.
- **🎨 Ultimate Web Aesthetics**: Features dynamic particle force fields (responsive to mouse/gesture repulsion), a 3D depth-of-field card roulette, and Glassmorphism UI panels.

### 🛠️ Tech Stack

#### Web Interface
- **Core**: Vanilla HTML / CSS / JavaScript
- **Gesture Recognition**: [MediaPipe Hands](https://google.github.io/mediapipe/solutions/hands.html)
- **Physics Engine**: [Matter.js](https://brm.io/matter-js/) (for the Vessel of Memories)
- **Rendering**: HTML5 Canvas (Particle System), CSS 3D Transforms
- **Markdown Parser**: Marked.js (for elegant AI output rendering)
- **AI Interface**: SiliconFlow API (DeepSeek-V3 Model)

#### IoT Companion
- **Microcontroller**: M5StickC / M5StickC Plus
- **Peripherals**: WS2812B / similar RGB LED strips
- **Communication Protocol**: Web Serial API (Baud rate: 115200)

### 🚀 Getting Started

#### 1. Hardware Preparation (M5StickC)
1. Flash your M5StickC with the corresponding serial listening program (C++ / MicroPython).
2. The program must listen for the following serial commands to drive the LEDs:
   - `STRIP:212,175,55` -> Switch LED color (RGB format)
   - `PICKED:1/2/3` -> Card draw progress visual effects
   - `BREATHE:IN` / `BREATHE:OUT` / `BREATHE:DONE` -> Breathing light effects for the meditation phase
3. Ensure the M5StickC is connected to your PC via USB.

#### 2. Software Deployment
1. Clone or download this repository.
2. Prepare Tarot image assets: Create a folder named `taroy` in the root directory and place 22 Major Arcana images named `ar00.jpg` through `ar21.jpg`.
3. Since it uses a webcam and Web Serial API, **it must be run in a local server environment** (e.g., VS Code Live Server, or `python -m http.server`).
4. Open the page using a browser that supports the Web Serial API (Google Chrome or Microsoft Edge recommended).

#### 3. Arcane Connection & Configuration
1. Click **[⚙ Settings]** in the top right corner.
2. Enter your **SiliconFlow API Key** and **Birthdate** (to enhance AI personalization).
3. Click **[✦ Connect Psi-Device]**, select your M5StickC device in the browser's serial prompt, and connect.
4. If the status bar shows `PSI-DEVICE CONNECTED` and the indicator turns gold, the connection is successful!

### ⚠️ Notes
- **Web Serial API Limits**: Only available under `localhost` or secure `HTTPS` contexts.
- **Hardware Compatibility**: The program functions perfectly as a standalone Web App even without the M5StickC (serial failures will automatically fallback gracefully).

---

<h2 id="中文">中文</h2>

Luckie-Bot 是一套融合了 **AI 大语言模型、MediaPipe 空间手势交互、2D物理引擎** 与 **IoT 硬件 (M5StickC)** 的全沉浸式智能塔罗占卜系统。

本项目通过极具视觉张力的“赛博神秘学” UI、非接触式的手势抽卡体验，以及外置硬件的灯光氛围同步，打破了数字与现实的边界，为用户提供独一无二的“命运探知”体验。

### ✨ 核心特性

- **🌌 沉浸式手势操控 (MediaPipe)**: 告别传统的鼠标点击。通过摄像头捕捉手势，用户可以在虚空中“滑动”检视塔罗牌阵，并通过“握拳”动作向牌面注入灵力并锁定命运之牌。
- **🧠 深度 AI 命理演算 (DeepSeek-V3)**: 接入 SiliconFlow API，结合用户的生辰、选择的领域以及抽出的【过去-现在-未来】三张牌面，生成专属的“命运织锦”（包含深度解读、驱动见解与今日挑战）。
- **🔌 跨次元硬件共振 (M5StickC + LED)**:
  - **氛围渲染**: 通过 Web Serial API 与 M5StickC 通信。当用户在网页端选择领域（如财运的金色、学业的蓝色）或进入冥想呼吸阶段时，M5StickC 会驱动外接 LED 灯带展现同步的呼吸律动与色彩更迭。
  - **双向同步**: M5StickC 硬件端也可作为独立控制器，物理同步/选择当前的占卜算命方向。
- **🔮 记忆之器 (Matter.js)**: 每次占卜的结果会被封装成一颗拥有真实物理碰撞效果的“记忆玻璃球”掉落在界面的角落。拨动、点击这些小球，即可回溯过往的命运轨迹。
- **🎨 极致的 Web 美学**: 动态粒子力场（响应鼠标/手势排斥力）、3D 景深卡牌轮盘、毛玻璃拟态面板 (Glassmorphism)。

### 🛠️ 技术栈

#### 软件端 (Web Interface)
- **前端核心**: 原生 HTML / CSS / Vanilla JavaScript
- **手势识别**: [MediaPipe Hands](https://google.github.io/mediapipe/solutions/hands.html)
- **物理引擎**: [Matter.js](https://brm.io/matter-js/) (用于记忆之器)
- **渲染工具**: HTML5 Canvas (粒子系统), CSS 3D Transforms
- **Markdown解析**: Marked.js (用于优雅渲染 AI 输出)
- **AI 接口**: SiliconFlow API (DeepSeek-V3 模型)

#### 硬件端 (IoT Companion)
- **主控板**: M5StickC / M5StickC Plus
- **外设**: WS2812B / 类似 RGB LED 灯带
- **通信协议**: Web Serial API (串口通信，波特率 115200)

### 🚀 快速开始

#### 1. 硬件端准备 (M5StickC)
1. 将你的 M5StickC 烧录对应的串口监听程序（C++ / MicroPython）。
2. 程序需监听以下串口指令以驱动灯带：
   - `STRIP:212,175,55` -> 切换灯带颜色（RGB格式）
   - `PICKED:1/2/3` -> 抽卡进度提示特效
   - `BREATHE:IN` / `BREATHE:OUT` / `BREATHE:DONE` -> 冥想阶段的呼吸灯效
3. 确保 M5StickC 通过 USB 连接至电脑。

#### 2. 软件端部署
1. 克隆或下载本仓库。
2. 准备塔罗牌图片素材：在根目录创建 `taroy` 文件夹，放入 `ar00.jpg` 到 `ar21.jpg`（共22张大阿尔卡那牌）。
3. 由于调用了摄像头和 Web Serial API，**必须在本地服务器环境下运行**（如 VS Code 的 Live Server 插件，或使用 `python -m http.server`）。
4. 使用支持 Web Serial API 的浏览器（推荐 **Google Chrome** 或 **Microsoft Edge**）打开页面。

#### 3. 奥术连接与配置
1. 点击页面右上角 **[⚙ 设置]**。
2. 填入你的 **SiliconFlow API Key** 以及 **出生日期**（用于增强 AI 解读的个性化）。
3. 点击 **[✦ 连接灵能设备]**，在弹出的浏览器串口选择框中，选中你的 M5StickC 设备并连接。
4. 状态栏显示 `PSI-DEVICE CONNECTED` 且指示灯变金，即代表连接成功！

### ⚠️ 注意事项
- **Web Serial API 限制**: 仅在 `localhost` 或 `HTTPS` 协议下可用。
- **硬件兼容**: 若没有连接 M5StickC，程序依然可以完美作为纯 Web 应用运行（串口通信失败会自动 fallback 保底处理）。

---
> *"In the shadow of the moonlight, only by facing the mist within can one touch true abundance."*
> 
> *“在月光的阴影下，唯有直面内心的迷雾，才能触摸真实的丰盛。” —— Arcanum Lab*
