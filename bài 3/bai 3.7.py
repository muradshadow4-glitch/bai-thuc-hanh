print("Hoang Nguyen Tuan Tu")
print("245752021610129")
print("--------------------")
# 1. Định nghĩa hàm checkValue(n)
# Hàm này nhận một tham số là số nguyên n
def checkValue(n):
    
    # Sử dụng toán tử modulo (%) để kiểm tra số dư khi chia n cho 2.
    # Nếu số dư là 0, đó là số chẵn.
    if n % 2 == 0:
        print(f"Số {n}: Đây là một số chẵn")
    # Ngược lại, đó là số lẻ.
    else:
        print(f"Số {n}: Đây là một số lẻ")

# --- Phần Gợi ý và Gọi hàm (Testing) ---

print("--- Kiểm tra số chẵn/lẻ ---")

# Gọi hàm với số chẵn (Ví dụ 4)
checkValue(4)

# Gọi hàm với số lẻ (Ví dụ 7)
checkValue(7)

# Có thể lấy input từ người dùng để kiểm tra
try:
    so_nguyen = int(input("\nNhập một số nguyên để kiểm tra: "))
    checkValue(so_nguyen)
except ValueError:
    print("Lỗi: Vui lòng nhập một số nguyên hợp lệ.")
