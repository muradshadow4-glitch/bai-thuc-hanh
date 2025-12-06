print("Hoang Nguyen Tuan Tu")
print("245752021610129")
print("--------------------")
# 1. Khai báo biến toàn cục (Global variable)
a = "Hello Guy!"

# Định nghĩa hàm say()
def say():
    # 2. Sử dụng từ khóa global để chỉ ra rằng
    # biến 'a' trong hàm này là biến toàn cục
    global a
    
    # 3. Thay đổi giá trị của biến toàn cục 'a'
    # Sự thay đổi này sẽ có hiệu lực bên ngoài hàm
    a = "Vinh University"
    print(f"Bên trong hàm say(): {a}")

# --- Thực thi chương trình và quan sát thay đổi ---

# Lệnh 1: In biến a toàn cục (Trước khi gọi hàm)
print(f"Lệnh 1 - Trước khi gọi say(): {a}") 

# Lệnh 2: Gọi hàm say()
# Hàm chạy và thay đổi giá trị của biến 'a' toàn cục thành "Vinh University"
say()

# Lệnh 3: In biến a toàn cục một lần nữa (Sau khi gọi hàm)
# Giá trị của biến 'a' đã bị thay đổi vĩnh viễn
print(f"Lệnh 3 - Sau khi gọi say(): {a}")
