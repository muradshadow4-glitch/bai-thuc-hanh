print("Hoang Nguyen Tuan Tu")
print("245752021610129")
print("--------------------")
# 1. Khai báo biến toàn cục (Global variable)
a = "Hello Guy!"

# Định nghĩa hàm say() với biến cục bộ (Local variable) trùng tên
def say():
    # 2. Khai báo biến cục bộ a. Biến này chỉ tồn tại trong hàm say()
    a = "Vinh University"
    print(a)

# --- Thực thi chương trình ---

# Lệnh 1: In biến a toàn cục
print(a) 

# Lệnh 2: Gọi hàm say()
# Khi gọi hàm, code bên trong chạy, biến a cục bộ được in ra
say()

# Lệnh 3: In biến a toàn cục một lần nữa
# Biến toàn cục a vẫn giữ nguyên giá trị ban đầu, không bị ảnh hưởng bởi hàm say()
print(a)
