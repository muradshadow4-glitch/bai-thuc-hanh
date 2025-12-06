print("Hoang Nguyen Tuan Tu")
print("245752021610129")
print("--------------------")
# =======================================================
# Bài 4: Xây dựng ứng dụng đồ họa Tkinter cơ bản
# =======================================================

from tkinter import *

# 1. Khởi tạo Cửa sổ và Thiết lập (a)
window = Tk()
window.title("Welcome to LikeGeeks app")
window.geometry('350x200') # Thiết lập kích thước cửa sổ (Width x Height)

# 2. Xử lý sự kiện bàn phím (c)
def key_pressed(event):
    """
    Hàm xử lý sự kiện khi một phím được nhấn trên bàn phím.
    """
    # Lấy thông tin về phím được nhấn
    key = event.keysym
    lbl.config(text=f"Phím được nhấn: {key}")

# Gắn sự kiện nhấn phím (<Key>) với hàm key_pressed cho toàn bộ cửa sổ
window.bind('<Key>', key_pressed)

# 3. Widget Label
lbl = Label(window, text="Hello. Nhấn phím bất kỳ...", fg="blue", font=("Arial", 12))
# Sử dụng grid để định vị (hàng 0, cột 0)
lbl.grid(column=0, row=0, padx=10, pady=10)


# 4. Thêm widget Button và xử lý sự kiện click (b)
def clicked():
    """
    Hàm xử lý sự kiện khi nút được nhấn.
    """
    # Cập nhật văn bản của Label khi nút được nhấn
    lbl.configure(text="Button was clicked!")
    
# Thêm nút bấm
btn = Button(window, text="Click Me", bg="yellow", fg="red", command=clicked)
# Định vị nút bấm (hàng 1, cột 0)
btn.grid(column=0, row=1, padx=10, pady=10)

# 5. Vòng lặp chính để hiển thị cửa sổ
window.mainloop()
