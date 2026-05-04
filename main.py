import M5
from M5 import *
import sys, select, time, math

# --- 硬件初始化 ---
M5.begin()
time.sleep_ms(200) 
Lcd.setRotation(1) # 横屏 240x135

# --- 颜色常量 ---
BG      = 0x050510
GOLD    = 0xd4af37
PURPLE  = 0x6a5acd
WHITE   = 0xffffff
RED     = 0xff4466
CYAN    = 0x00ccff
DARK    = 0x1a1a2e

# --- 情绪配置 ---
MOODS = ["ANGRY", "SAD", "PEACE", "HAPPY"]
MOOD_COLORS = [RED, CYAN, PURPLE, GOLD]
mood_idx = 3 
mood_history = [0, 0, 0, 0, 0, 0, 0] 

# --- 💾 数据持久化逻辑 ---
DATA_FILE = "mood_history.txt"

def save_data():
    try:
        with open(DATA_FILE, "w") as f:
            f.write(",".join(map(str, mood_history)))
    except: pass

def load_data():
    global mood_history
    try:
        with open(DATA_FILE, "r") as f:
            data = f.read().strip().split(",")
            if len(data) == 7:
                mood_history = [int(x) for x in data]
    except: pass

# --- 手动打印函数 ---
def print_at(text, x, y, size, color):
    Lcd.setTextColor(color, BG)
    Lcd.setTextSize(size)
    Lcd.setCursor(x, y)
    Lcd.print(text)

# --- 绘图工具 ---
def draw_arc(cx, cy, r, a0, a1, color):
    steps = 8
    prev_x, prev_y = -1, -1
    for i in range(steps + 1):
        t = i / steps
        angle = math.radians(a0 + (a1 - a0) * t)
        px = int(cx + r * math.cos(angle))
        py = int(cy + r * math.sin(angle))
        if prev_x != -1:
            Lcd.drawLine(prev_x, prev_y, px, py, color)
        prev_x, prev_y = px, py

# --- 绘制表情 (优化坐标：中心点定在 40，确保不越界) ---
def draw_face(mood):
    # 脸部中心点
    lx, rx, ly, ry = 20, 60, 45, 45
    mx, my = 40, 70

    if mood == "HAPPY":
        draw_arc(lx, ly, 7, 200, 340, WHITE)
        draw_arc(rx, ry, 7, 200, 340, WHITE)
        draw_arc(mx, my, 10, 20, 160, GOLD)
    elif mood == "PEACE":
        Lcd.drawCircle(lx, ly, 6, WHITE)
        Lcd.drawCircle(rx, ry, 6, WHITE)
        Lcd.drawLine(mx - 8, my, mx + 8, my, GOLD)
    elif mood == "SAD":
        Lcd.drawLine(lx-5, ly-2, lx+5, ly+2, WHITE)
        Lcd.drawLine(rx+5, ry-2, rx-5, ry+2, WHITE)
        draw_arc(mx, my+6, 9, 200, 340, CYAN)
    elif mood == "ANGRY":
        Lcd.drawLine(lx-7, ly-1, lx+7, ly-5, RED)
        Lcd.drawLine(rx+7, ry-1, rx-7, ry-5, RED)
        Lcd.fillRect(mx-8, my, 16, 2, RED)

# --- 绘制趋势图 (优化坐标：从135px开始，宽度90px) ---
def draw_chart(x_s, y_s, w, h):
    Lcd.drawRect(x_s, y_s, w, h, 0x222233)
    # 刻度
    for i in range(1, 4):
        yy = y_s + h - int(i * (h/4))
        Lcd.drawLine(x_s, yy, x_s+3, yy, 0x333344)

    points = []
    for i in range(7):
        val = mood_history[i]
        if val > 0:
            px = x_s + int(i * (w / 6))
            py = y_s + h - int(val * (h / 4.5))
            points.append((px, py))
    
    for i in range(len(points) - 1):
        Lcd.drawLine(points[i][0], points[i][1], points[i+1][0], points[i+1][1], GOLD)
        Lcd.fillCircle(points[i][0], points[i][1], 2, PURPLE)
    if points:
        Lcd.fillCircle(points[-1][0], points[-1][1], 3, WHITE)

# --- 界面总刷新 ---
def refresh_ui():
    Lcd.clear(BG)
    current_mood = MOODS[mood_idx]
    
    # 1. 左侧：表情 + 文字 (中心控制在 40-50 像素内)
    draw_face(current_mood)
    print_at(current_mood, 15, 100, 2, MOOD_COLORS[mood_idx])
    
    # 2. 右侧：趋势图 (起始位置 135，彻底避开左侧)
    print_at("7D TREND", 140, 10, 1, 0x555555) 
    draw_chart(135, 30, 90, 80)
    
    # 3. 物理分割线 (在 105 处)
    Lcd.drawLine(105, 20, 105, 120, 0x222233)

def log_mood():
    global mood_history
    for i in range(6): mood_history[i] = mood_history[i+1]
    mood_history[6] = mood_idx + 1
    save_data() # 记录的同时保存到闪存
    print("EVT:MOOD:" + MOODS[mood_idx])
    
    Lcd.fillRect(0, 0, 240, 3, MOOD_COLORS[mood_idx]) # 顶边反馈
    M5.Speaker.tone(2000, 50)
    time.sleep_ms(100)
    refresh_ui()

# --- 启动 ---
load_data()
refresh_ui()
print("READY")

# --- 主循环 ---
rx_buffer = ""
while True:
    M5.update()
    if M5.BtnA.wasPressed():
        mood_idx = (mood_idx + 1) % 4
        refresh_ui()
    if M5.BtnB.wasPressed():
        log_mood()
    
    if select.select([sys.stdin], [], [], 0)[0]:
        char = sys.stdin.read(1)
        if char == '\n':
            if rx_buffer.strip() == "UI:REFRESH": refresh_ui()
            rx_buffer = ""
        else: rx_buffer += char
    time.sleep_ms(20)