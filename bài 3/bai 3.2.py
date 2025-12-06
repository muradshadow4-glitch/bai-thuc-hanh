print("Hoang Nguyen Tuan Tu")
print("245752021610129")
print("--------------------")
# Định nghĩa lại hàm sum(a, b) để trả về tổng
def sum(a, b):
    return a + b  # Hàm trả về giá trị tổng

# --- Các lệnh gọi hàm ---

# Tính tổng 4 và 5 và lưu vào biến c
c = sum(4, 5)

# In ra kết quả sử dụng biến c
# Lưu ý: Hàm str(c) được sử dụng để chuyển số thành chuỗi để nối với chuỗi khác
print(f"Tổng của 4 và 5 = {c}")

# Ví dụ thêm với giá trị khác
d = sum(10, 20)
print(f"Tổng của 10 và 20 = {d}")
