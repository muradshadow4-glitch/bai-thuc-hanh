print("Hoang Nguyen Tuan Tu")
print("246752021610129")
print("---------------------------------------")
# =======================================================
# Bài 8: Form Thông Tin Cá Nhân và Radio Button
# =======================================================

from tkinter import *
from tkinter import messagebox

# Hàm xử lý khi nút 'Click Me' được nhấn (Phần b)
def show_radio_choice():
    """
    Lấy giá trị từ Radio Button được chọn và hiển thị trong hộp thoại thông báo.
    """
    # Lấy giá trị số (1, 2, hoặc 3)
    selected_value = radio_var.get()
    
    # Tìm tên tương ứng với giá trị
    choice_name = ""
    if selected_value == 1:
        choice_name = "First"
    elif selected_value == 2:
        choice_name = "Second"
    elif selected_value == 3:
        choice_name = "Third"
    else:
        choice_name = "None"
        
    # Hiển thị kết quả trong messagebox
    messagebox.showinfo("Radio Button Result", 
                        f"Bạn đã chọn lựa chọn: {choice_name} (Value: {selected_value})")

# Khởi tạo cửa sổ chính
root = Tk()
root.title("Bài 8: Form Thông Tin và Lựa Chọn")
root.geometry('450x450')

# Sử dụng Frame để tổ chức form thông tin cá nhân (Phần a)
info_frame = LabelFrame(root, text="A. Thông Tin Cá Nhân", padx=10, pady=10)
info_frame.grid(row=0, column=0, padx=20, pady=10, sticky="ew") # sticky="ew" giúp frame giãn ngang

# --- Phần a: Xây dựng Form Thông tin Cá nhân ---
# Tạo list các Label
labels_text = ["Họ và Tên:", "Ngày tháng năm sinh:", "Mã số sinh viên (MSSV):", "Ngành học:"]
# Tạo list các Entry (ô nhập)
entries = {}
# Vòng lặp để tạo và đặt vị trí các Label và Entry
for i, text in enumerate(labels_text):
    Label(info_frame, text=text, anchor="w", width=20).grid(row=i, column=0, sticky="w", pady=5)
    entry = Entry(info_frame, width=30)
    entry.grid(row=i, column=1, padx=10, pady=5)
    entries[text] = entry # Lưu entry để có thể lấy giá trị sau này (nếu cần)

# --- Phần b: Xây dựng Radio Button và Button ---
radio_frame = LabelFrame(root, text="B. Lựa Chọn Radio", padx=10, pady=10)
radio_frame.grid(row=1, column=0, padx=20, pady=10, sticky="ew")

# Biến điều khiển cho Radio Button
radio_var = IntVar()
radio_var.set(1) # Thiết lập giá trị mặc định là First (1)

# Tạo và đặt vị trí các Radio Button
# Lựa chọn 1
Radiobutton(radio_frame, text="First", variable=radio_var, value=1).pack(side=LEFT, padx=5)
# Lựa chọn 2
Radiobutton(radio_frame, text="Second", variable=radio_var, value=2).pack(side=LEFT, padx=5)
# Lựa chọn 3
Radiobutton(radio_frame, text="Third", variable=radio_var, value=3).pack(side=LEFT, padx=5)

# Nút 'Click Me'
Button(radio_frame, text="Click Me", command=show_radio_choice).pack(side=LEFT, padx=20)

# Vòng lặp chính
root.mainloop()
