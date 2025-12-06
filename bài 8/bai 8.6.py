print("Hoang Nguyen Tuan Tu")
print("246752021610129")
print("---------------------------------------")
# =======================================================
# BÀI 6 (TKINTER): Viết chương trình thực hiện tạo menu
# =======================================================

from tkinter import *
from tkinter import messagebox

# Hàm xử lý khi mục menu được chọn
def exit_program():
    """Xử lý sự kiện Exit: Thoát khỏi chương trình."""
    root.quit()

def show_about():
    """Xử lý sự kiện About: Hiển thị hộp thoại thông tin."""
    messagebox.showinfo("About", "Đây là một ví dụ đơn giản về Menu Tkinter.")

# Hàm chính để chạy chương trình Tkinter
def run_menu_program():
    global root
    root = Tk()
    root.title("Bài 6: Menu Tkinter")
    root.geometry('300x200')

    # 1. Tạo Thanh Menu (Menu Bar)
    menu_bar = Menu(root)
    root.config(menu=menu_bar) # Đính kèm menu bar vào cửa sổ chính

    # 2. Tạo Menu 'File'
    file_menu = Menu(menu_bar, tearoff=0) # tearoff=0 loại bỏ gạch ngang ở đầu menu
    menu_bar.add_cascade(label="File", menu=file_menu) # Gán menu 'File' vào thanh menu

    # Thêm các mục menu vào File
    file_menu.add_command(label="New")
    file_menu.add_command(label="Open")
    file_menu.add_separator() # Thêm đường phân cách
    file_menu.add_command(label="Exit", command=exit_program) # Gắn lệnh thoát

    # 3. Tạo Menu 'Help'
    help_menu = Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label="Help", menu=help_menu) # Gán menu 'Help' vào thanh menu
    
    # Thêm các mục menu vào Help
    help_menu.add_command(label="About", command=show_about)

    # Label hiển thị thông báo
    Label(root, text="Menu đã được tạo thành công!", padx=20, pady=20).pack()

    # Vòng lặp chính
    root.mainloop()

# Chạy chương trình Tkinter
run_menu_program()
