print("Hoang Nguyen Tuan Tu")
print("245752021610129")
print("--------------------")
# Xác định khoảng (a, b). Ví dụ: (10, 20)
a = 10
b = 20

# Dãy số tự nhiên trong khoảng (a, b) là từ a+1 đến b-1.
# range(b, a, -1) sẽ lặp từ b-1 xuống a+1.
# Ví dụ: nếu a=10, b=20, range(20, 10, -1) sẽ lặp 19, 18, ..., 11.

print(f"Dãy số tự nhiên ngược lại trong khoảng ({a}, {b}):")
# Vòng lặp in dãy số ngược
for i in range(b, a, -1):
    # In ra số hiện tại
    print(f"Số: {i}")

    # In ra kết quả phép chia i/2 dưới dạng thập phân
    # (Nếu dùng i/i, kết quả luôn là 1.0)
    ket_qua_chia = i / 2
    print(f"Kết quả phép chia i/2: {ket_qua_chia:.2f}") # Làm tròn 2 chữ số thập phân

    print("---") # Đường ngăn cách cho dễ nhìn
