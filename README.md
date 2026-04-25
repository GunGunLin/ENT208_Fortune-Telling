# 🔮 Luckie-Bot · Arcanum Laboratory

<p align="center">
  <img src="https://img.shields.io/badge/AI-DeepSeek--V3-blue?style=for-the-badge&logo=openai" alt="AI">
  <img src="https://img.shields.io/badge/Hardware-M5StickC--Plus-ff6a00?style=for-the-badge&logo=espressif" alt="M5StickC">
  <img src="https://img.shields.io/badge/Tech-WebSerial-brightgreen?style=for-the-badge&logo=googlechrome" alt="WebSerial">
</p>

---

## 🌟 Overview / 项目简介

**Luckie-Bot** is an immersive web-based application that merges ancient Tarot mysticism with cutting-edge technology. It creates a unique cross-dimensional experience by combining **MediaPipe** computer vision for gesture interaction and **M5StickC Plus** hardware as a physical spiritual companion.

**Luckie-Bot** 是一款融合了神秘学塔罗占卜与现代前沿技术的沉浸式 Web 应用程序。它不仅利用计算机视觉进行手势交互，更通过 **M5StickC Plus** 实体硬件实现了跨维度的联动体验。

---

## ✨ Key Features / 核心功能

### 🖐️ Dual-Mode Interaction / 双模交互
* **EN:** **Gesture Control:** Touchless interaction via `MediaPipe Hands`—wave to scroll the deck and clench to lock your cards.
* **CN:** **手势控制：** 基于 `MediaPipe Hands` 实现非接触式操控，通过挥手滚动牌堆，握拳锁定卡牌。
* **EN:** **Physical Sprite (M5StickC Plus):** Use physical buttons to sync and select divination categories (Fortune, Academic, Romance, General).
* **CN:** **实体精灵：** 通过 M5StickC Plus 实体按键同步选择算命类型（财运、学业、情感、综合）。

### 🌈 Immersive Experience / 沉浸式体验
* **EN:** **Ambient Lighting Sync:** Integrated LED strip (WS2812B) support that changes colors based on the domain (e.g., Golden for Fortune, Blue for Academic).
* **CN:** **氛围灯效联动：** 连接外部 LED 灯带，根据占卜阶段和所选领域实时切换光效（如黄金律法对应金光，智慧星轨对应蓝光）。
* **EN:** **AI-Powered Oracle:** Powered by `DeepSeek-V3` to generate personalized fate reports, including deep interpretations and "Daily Quests."
* **CN:** **AI 神谕生成：** 集成 DeepSeek-V3 大模型，生成包含深度解读、核心见解及“今日挑战”的个性化报告。

### 🌱 Progression / 养成系统
* **EN:** **Psionic Garden:** A gamified system where your virtual plant evolves from a "Void Seed" to an "Eternal Canopy" as you accumulate energy.
* **CN:** **灵能花园养成：** 占卜积累的能量将使你的虚拟植物从“虚空种子”进化为“永恒树冠”。

---

## 🛠️ Tech Stack / 技术栈

| Category | Technologies |
| :--- | :--- |
| **Software** | HTML5, CSS3 (3D Transforms), JavaScript (ES6+), Marked.js |
| **Vision** | MediaPipe Hands |
| **Hardware** | M5StickC Plus (ESP32), Arduino/UIFlow |
| **Protocol** | Web Serial API (Bi-directional communication) |
| **AI Model** | DeepSeek-V3 (via SiliconFlow API) |

---

## 🚀 Quick Start / 快速开始

### 1. Hardware Setup / 硬件准备
1.  Connect **M5StickC Plus** to your computer via USB.
2.  Flash the serial firmware (ensure it sends `EVT:CAT:Category` strings).
3.  Connect the LED strip to the corresponding pins (WS2812B recommended).

### 2. Environment / 环境配置
* Use a browser supporting **Web Serial API** (e.g., Google Chrome).
* Host the project under **HTTPS** or **localhost** for camera and serial permissions.

### 3. Connection / 连接与使用
1.  Launch the site and click **"CONNECT DEVICE"**.
2.  Select M5StickC Plus from the serial port list.
3.  Press physical buttons on the device to select a domain; the web UI will sync automatically.

---

## 📡 Hardware Protocol / 硬件通信协议

| Type / 类型 | From / 发送方 | Format / 格式 | Description / 描述 |
| :--- | :--- | :--- | :--- |
| **Category** | M5StickC | `EVT:CAT:Fortune` | Sync UI to selected domain / 同步网页分类 |
| **Lighting** | Web | `STRIP:212,175,55` | Sync LED color with theme / 同步灯带颜色 |
| **Breathing** | Web | `BREATHE:IN/OUT` | Guide LED pulsation / 引导灯带呼吸律动 |
| **Feedback** | Web | `PICKED:1/2/3` | Haptic/Visual feedback / 选中卡牌时的反馈 |

---

<p align="center">
  Built with ✨ by <b>Arcanum Laboratory</b>
</p>
