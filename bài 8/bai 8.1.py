print("Hoang Nguyen Tuan Tu")
print("246752021610129")
print("----------------")
# =======================================================
# Bài 1 (Trang 33): Vẽ đồ họa sử dụng thư viện Turtle
# =======================================================

import turtle

# Thiết lập cửa sổ vẽ (Screen)
window = turtle.Screen()
window.bgcolor("lightgreen") # Đặt màu nền là xanh lá nhạt

# Thiết lập bút vẽ (Turtle object)
painter = turtle.Turtle()
painter.fillcolor('blue') # Đặt màu tô là xanh dương
painter.pencolor('blue')  # Đặt màu nét vẽ là xanh dương
painter.pensize(3)        # Đặt kích thước nét vẽ là 3 pixels

# Định nghĩa hàm vẽ hình vuông (drawsq)
def drawsq(t, s):
    """
    Hàm vẽ một hình vuông với bút vẽ t và độ dài cạnh s.
    Vẽ 4 cạnh, mỗi cạnh rẽ trái 90 độ.
    """
    for i in range(4):
        t.forward(s)
        t.left(90)

# Bắt đầu vòng lặp chính để tạo ra hình dạng phức tạp
# Vòng lặp này lặp lại 180 lần
for i in range(1, 180): 
    painter.left(2)         # Xoay bút vẽ sang trái 2 độ
    drawsq(painter, 200)    # Gọi hàm vẽ hình vuông với cạnh 200

# Giữ cửa sổ mở cho đến khi người dùng nhấp chuột
window.exitonclick()
