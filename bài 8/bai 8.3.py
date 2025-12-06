print("Hoang Nguyen Tuan Tu")
print("245752021610129")
print("--------------------")
# =======================================================
# Bài 3 (Trang 34): Vẽ hình đồ họa nhiều hình tròn lồng nhau
# =======================================================

import turtle
import random

# Thiết lập cửa sổ vẽ (Screen)
window = turtle.Screen()
window.bgcolor("white") 

# Thiết lập bút vẽ (Turtle object)
painter = turtle.Turtle()
painter.pensize(2) 
painter.speed(0) # Tốc độ vẽ nhanh nhất

# 1. Định nghĩa các màu sắc sẽ được sử dụng luân phiên
# Ta sử dụng một danh sách màu lớn hơn để tạo ra hiệu ứng nhiều màu như trong hình.
colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet", "cyan"]

# 2. Vòng lặp chính để vẽ các hình tròn
# Để tạo ra hình dạng phức tạp có 8 cánh hoa và nhiều vòng tròn,
# ta cần lặp lại một số lần đủ lớn (ví dụ 72 lần) và xoay góc nhỏ.
num_circles = 72
rotation_angle = 360 / num_circles  # Tính góc xoay cần thiết: 5 độ

for i in range(num_circles): 
    # Chọn màu luân phiên dựa trên chỉ số i
    color = colors[i % len(colors)] 
    
    # Đặt màu nét vẽ
    painter.pencolor(color)
    
    # Vẽ một hình tròn có bán kính cố định (ví dụ: 100)
    painter.circle(100) 
    
    # Xoay bút vẽ 5 độ
    painter.right(rotation_angle) 
    
# 3. Kết thúc chương trình
window.exitonclick()
