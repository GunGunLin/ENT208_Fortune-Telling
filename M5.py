import sys
import socket
import threading
import requests
import json
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QInputDialog, QMessageBox
from PySide6.QtCore import Qt, Signal, QPoint, QSettings
from PySide6.QtGui import QPixmap

# --- 配置区 ---
UDP_IP = "0.0.0.0"
UDP_PORT = 12345
# 建议确认你的 Key 是否有效
SiliconFlow_KEY = "Your api KEY"
API_URL = "https://api.siliconflow.cn/v1/chat/completions"


class LuckiePet(QWidget):
    new_quote_signal = Signal(str)

    def __init__(self):
        super().__init__()
        self.drag_position = QPoint()
        self.init_ui()

        # 启动后稍作延迟弹出算命窗口，避免 UI 还没加载完
        self.check_first_run()

        # 启动 UDP 监听
        self.new_quote_signal.connect(self.display_quote)
        self.udp_thread = threading.Thread(target=self.udp_listener, daemon=True)
        self.udp_thread.start()

    def init_ui(self):
        # 无边框、置顶、任务栏隐藏
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.Tool)
        self.setAttribute(Qt.WA_TranslucentBackground)

        layout = QVBoxLayout()

        # 1. 像素精灵图层
        self.pet_label = QLabel(self)
        self.pet_label.setText("🤖")  # 你可以后期换成 self.pet_label.setPixmap(QPixmap("sprite.png"))
        self.pet_label.setStyleSheet("font-size: 50px;")
        self.pet_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.pet_label)

        # 2. 语录气泡图层
        self.quote_label = QLabel("Waiting for M5...", self)
        self.quote_label.setStyleSheet("""
            QLabel {
                color: white; 
                background-color: rgba(187, 0, 255, 180); 
                border-radius: 12px; 
                padding: 10px;
                font-family: 'Microsoft YaHei';
                font-size: 14px;
            }
        """)
        self.quote_label.setWordWrap(True)
        self.quote_label.setAlignment(Qt.AlignCenter)
        self.quote_label.setFixedWidth(200)
        layout.addWidget(self.quote_label)

        self.setLayout(layout)
        self.move(100, 100)

    # --- 修复后的 UDP 监听 ---
    def udp_listener(self):
        # 核心修复：直接使用 socket.AF_INET
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.bind((UDP_IP, UDP_PORT))
            print(f"✅ Desktop Pet is listening on port {UDP_PORT}...")

            while True:
                data, addr = sock.recvfrom(1024)
                message = data.decode('utf-8')
                if message.startswith("QUOTE:"):
                    self.new_quote_signal.emit(message[6:])
        except Exception as e:
            print(f"❌ UDP Error: {e}")

    def display_quote(self, quote):
        self.quote_label.setText(quote)
        self.adjustSize()

    # --- 鼠标拖动逻辑 ---
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drag_position = event.globalPosition().toPoint() - self.frameGeometry().topLeft()
            event.accept()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.move(event.globalPosition().toPoint() - self.drag_position)
            event.accept()

    # --- 生辰八字 AI 算命 ---
    def check_first_run(self):
        settings = QSettings("LuckieBot", "PCPet")
        if not settings.value("first_run_complete", False):
            # 使用 timer 确保主窗口显示后弹出
            from PySide6.QtCore import QTimer
            QTimer.singleShot(1000, lambda: self.show_bazi_dialog(settings))

    def show_bazi_dialog(self, settings):
        bazi, ok = QInputDialog.getText(self, "Luckie-Bot 初次见面",
                                        "我是你的守护精灵。\n请输入你的生辰八字（如：1995年10月1日 10:00）")
        if ok and bazi:
            fortune = self.get_ai_bazi_fortune(bazi)
            QMessageBox.information(self, "您的专属命理", fortune)
            settings.setValue("first_run_complete", True)

    def get_ai_bazi_fortune(self, bazi):
        # 核心修复：禁用系统代理，防止 VPN 干扰
        session = requests.Session()
        session.trust_env = False

        payload = {
            "model": "deepseek-ai/DeepSeek-V3",
            "messages": [
                {"role": "system", "content": "你是一个温暖的桌面精灵。请根据八字给出一句50字以内的治愈系运势简评。"},
                {"role": "user", "content": f"我的生辰八字是：{bazi}"}
            ]
        }
        headers = {
            "Authorization": f"Bearer {SiliconFlow_KEY}",
            "Content-Type": "application/json"
        }
        try:
            response = session.post(API_URL, headers=headers, json=payload, timeout=12)
            if response.status_code == 200:
                return response.json()['choices'][0]['message']['content'].strip()
            return f"暂时算不出来呢 (错误码: {response.status_code})"
        except Exception as e:
            return f"测算失败，请检查网络连接。\n错误详情: {type(e).__name__}"


if __name__ == "__main__":
    app = QApplication(sys.argv)
    pet = LuckiePet()
    pet.show()
    sys.exit(app.exec())
