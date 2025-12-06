print("Hoang Nguyen Tuan Tu")
print("245752021610129")
print("--------------------")
    # =======================================================
# Bài 5 b): Radio Button dạng Indicator (Đã sửa lỗi TclError)
# =======================================================

from tkinter import *

# 1. Khởi tạo cửa sổ chính
root = Tk()
root.title("Bài 5b: Radio Button dạng Indicator (Fixed)")
root.geometry('400x350')

# 2. Định nghĩa biến điều khiển
v = IntVar() 
v.set(1) 

# 3. Định nghĩa danh sách các lựa chọn ngôn ngữ
languages = [
    ("Python", 1), ("Perl", 2), ("Java", 3), ("C++", 4), ("C", 5)
]

# 4. Hàm xử lý khi lựa chọn thay đổi
def ShowChoice():
    selected_value = v.get()
    selected_name = ""
    for name, value in languages:
        if value == selected_value:
            selected_name = name
            break
            
    status_label.config(text=f"Bạn đã chọn: {selected_name}")

# 5. Thêm Label tiêu đề
Label(
    root,
    text="***Choose your favourite programming language***",
    justify=LEFT, 
    padx=20
).pack(pady=(10, 5))

# 6. Thêm các Radio Button dạng Indicator
for language, val in languages:
    Radiobutton(
        root,
        text=language,
        padx=10, 
        width=15,
        bd=2,
        
        # --- THAY ĐỔI ĐỂ SỬA LỖI ---
        indicatoron=0,     # Tắt biểu tượng radio button tròn
        relief=RAISED,     # Dùng thuộc tính relief tiêu chuẩn (RAISED/FLAT)
        # selectrelief=SUNKEN, # LỖI: Thuộc tính này không tồn tại cho Radiobutton
        selectcolor="lightblue", # Màu nền khi được chọn
        
        # --- THUỘC TÍNH CHUẨN ---
        variable=v,
        command=ShowChoice,
        value=val, 
        anchor=W
    ).pack(anchor=N) 

# 7. Thêm Label trạng thái 
status_label = Label(root, text="Chưa chọn hoặc chọn Python", fg="green", padx=20, pady=10)
status_label.pack(pady=10)

# 8. Vòng lặp chính
root.mainloop()
