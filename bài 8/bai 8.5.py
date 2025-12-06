print("Hoang Nguyen Tuan Tu")
print("245752021610129")
print("--------------------")
# =======================================================
# Bài 5 a): Xây dựng Radio Button Tkinter (Đã sửa lỗi NameError)
# =======================================================

from tkinter import * # Sử dụng import * nên KHÔNG dùng tiền tố tk.

# 1. Khởi tạo cửa sổ chính
root = Tk() # Đã sửa: dùng Tk() thay vì tk.Tk()
root.title("Bài 5a: Radio Button Tkinter")
root.geometry('400x300')

# 2. Định nghĩa biến điều khiển (Control Variable)
v = IntVar() # Đã sửa: dùng IntVar()
v.set(1) 

# 3. Định nghĩa danh sách các lựa chọn ngôn ngữ
languages = [
    ("Python", 1), 
    ("Perl", 2),
    ("Java", 3),
    ("C++", 4),
    ("C", 5)
]

# 4. Hàm xử lý khi lựa chọn thay đổi (command)
def ShowChoice():
    selected_value = v.get()
    selected_name = ""
    for name, value in languages:
        if value == selected_value:
            selected_name = name
            break
            
    # Hiển thị thông báo trong cửa sổ
    status_label.config(text=f"Bạn đã chọn: {selected_name} (Value: {selected_value})")

# 5. Thêm Label tiêu đề
Label( # Đã sửa: dùng Label() thay vì tk.Label()
    root,
    text="***Choose your favourite programming language***",
    justify=LEFT, # Đã sửa: dùng LEFT thay vì tk.LEFT
    padx=20
).pack()

# 6. Thêm các Radio Button
for language, val in languages:
    Radiobutton( # Đã sửa: dùng Radiobutton() thay vì tk.Radiobutton()
        root,
        text=language,
        padx=20,
        variable=v,
        command=ShowChoice,
        value=val,
        anchor=W # Đã sửa: dùng W thay vì tk.W
    ).pack(anchor=W)

# 7. Thêm Label trạng thái 
status_label = Label(root, text="Chưa chọn hoặc chọn Python (1)", fg="green", padx=20, pady=10)
status_label.pack()

# 8. Vòng lặp chính
root.mainloop()
