# 🔮 Luckie-Bot · Arcanum Laboratory

<p align="center">
  <img src="https://img.shields.io/badge/AI-DeepSeek--V3-blue?style=for-the-badge&logo=openai" alt="AI">
  <img src="https://img.shields.io/badge/Hardware-M5StickC--Plus-ff6a00?style=for-the-badge&logo=espressif" alt="M5StickC">
  <img src="https://img.shields.io/badge/Tech-WebSerial-brightgreen?style=for-the-badge&logo=googlechrome" alt="WebSerial">
  <img src="https://img.shields.io/badge/UI-3D%20Transform-rebeccapurple?style=for-the-badge&logo=css3" alt="CSS3">
</p>

> **Luckie-Bot** 是一款融合了神秘学塔罗占卜与现代前沿技术的沉浸式 Web 应用程序。它不仅利用计算机视觉进行手势交互，更通过 M5StickC Plus 实体硬件实现了跨维度的联动体验。

---

## 📖 目录 (Table of Contents)
- [核心功能](#✨-核心功能-key-features)
- [技术栈](#🛠️-技术栈-tech-stack)
- [快速开始](#🚀-快速开始-quick-start)
- [硬件通信协议](#📡-硬件通信协议-hardware-protocol)
- [English Version](#-luckie-bot-en)

---

## ✨ 核心功能 (Key Features)

* **🖐️ 双模交互系统 (Dual-Mode Interaction)**
    * **手势控制**：基于 `MediaPipe Hands` 实现非接触式操控。挥手滚动牌堆，握拳锁定卡牌，赋予占卜仪式非凡的艺术感。
    * **实体精灵 (M5StickC Plus)**：通过实体按键同步选择算命类型（财运、学业、情感、综合），它就是你桌面的“命运守护者”。
* **🌈 氛围灯效联动 (Ambient Lighting)**
    * 连接外部 **WS2812B** 灯带，根据占卜阶段和所选领域实时切换光效：
        * 💰 财运 -> **黄金律法**（金色光芒）
        * 🎓 学业 -> **智慧星轨**（深蓝色调）
* **🤖 AI 神谕生成 (AI-Powered Oracle)**
    * 集成 **DeepSeek-V3** 大模型，生成包含深度解读、核心见解及“今日挑战”的个性化报告。
* **🌱 灵能花园养成系统 (Psionic Garden)**
    * 占卜积累的能量将使你的虚拟植物从“虚空种子”进化为“永恒树冠”。

---

## 🛠️ 技术栈 (Tech Stack)

| 模块 | 技术实现 |
| :--- | :--- |
| **前端 (Frontend)** | `HTML5`, `CSS3 (3D Transforms)`, `JavaScript (ES6+)`, `Marked.js` |
| **感知 (Vision)** | `MediaPipe Hands` (计算机视觉/手势识别) |
| **硬件 (Hardware)** | `M5StickC Plus (ESP32)`, `Arduino / UIFlow` |
| **连接 (Connectivity)** | `Web Serial API` (浏览器与串口双向通信) |
| **人工智能 (AI)** | `DeepSeek-V3` (via SiliconFlow API) |

---

## 🚀 快速开始 (Quick Start)

### 1. 硬件准备
* 将 **M5StickC Plus** 连接至电脑 USB 接口。
* 烧录串口通信程序（确保发送 `EVT:CAT:类别` 指令）。
* 外接灯带至 M5StickC Plus 的对应引脚（建议使用 **WS2812B**）。

### 2. 环境配置
* 使用支持 **Web Serial API** 的浏览器（强烈建议使用 **Google Chrome**）。
* 项目需在 **HTTPS** 或 **localhost** 环境下运行，以获取摄像头及串口访问权限。

### 3. 连接与使用
1.  启动网页，点击 **“连接灵能设备 (CONNECT DEVICE)”**。
2.  在弹出的串口列表中选择对应的 M5StickC Plus 端口。
3.  通过硬件按键切换领域，网页端将自动实时同步。

---

## 📡 硬件通信协议 (Hardware Protocol)

| 指令类型 | 发送方 | 指令格式 | 描述 |
| :--- | :--- | :--- | :--- |
| **选择领域** | M5StickC | `EVT:CAT:Fortune` | 网页同步跳转至对应占卜类别 |
| **灯带控制** | Web | `STRIP:212,175,55` | 同步灯带颜色（RGB） |
| **呼引导** | Web | `BREATHE:IN/OUT` | 引导灯带进行呼吸律动 |
| **交互反馈** | Web | `PICKED:1/2/3` | 选中卡牌时的物理/视觉反馈 |

---

## 🌍 Luckie-Bot (EN)

**Luckie-Bot** is an immersive web-based application that merges ancient Tarot mysticism with cutting-edge technology. It features a unique cross-dimensional experience powered by **M5StickC Plus** as a physical companion and computer vision for touchless gesture interaction.

- **Gesture Control**: Powered by MediaPipe.
- **AI Oracle**: Deep readings by DeepSeek-V3.
- **Physical Sync**: Real-time feedback via Web Serial API.

---

<p align="center">
  Designed by <b>Arcanum Laboratory</b>
</p>
