print("Hoang Nguyen Tuan Tu")
print("245752021610129")
print("--------------------")
# =======================================================
# Bài 2 (Trang 34): Vẽ đồ họa ngẫu nhiên sử dụng Turtle
# =======================================================

import turtle
import random

# 1. Định nghĩa các màu sắc
colors = ["red", "green", "blue", "orange", "purple", "pink", "yellow"]

# Thiết lập cửa sổ vẽ (Screen)
window = turtle.Screen()
window.bgcolor("lightgray") # Đặt màu nền là xám nhạt

# Thiết lập bút vẽ (Turtle object)
painter = turtle.Turtle()
painter.pensize(3) # Đặt kích thước nét vẽ là 3 pixels
painter.speed(0)   # Đặt tốc độ vẽ nhanh nhất (Fastest)

# 2. Vòng lặp chính để vẽ 10 hình tròn
for i in range(10): 
    # Chọn ngẫu nhiên một màu từ danh sách
    color = random.choice(colors) 
    
    # Đặt màu nét vẽ cho hình tròn tiếp theo
    painter.pencolor(color)
    
    # Vẽ một hình tròn có bán kính 100
    painter.circle(100) 
    
    # Xoay bút vẽ sang phải 30 độ
    painter.right(30) 
    
    # Xoay bút vẽ sang trái 60 độ
    painter.left(60) 
    
    # Đặt lại vị trí của bút vẽ về (0, 0)
    painter.setpos(0, 0) 

# 3. Kết thúc chương trình
window.exitonclick()
