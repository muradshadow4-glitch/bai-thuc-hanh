print("Hoang Nguyen Tuan Tu")
print("245752021610129")
print("--------------------")
## === BÀI 9: CHƯƠNG TRÌNH MÁY TÍNH ĐƠN GIẢN ===

# --- Định nghĩa các hàm phép toán ---

def add(a, b):
    """Hàm này thực hiện phép cộng hai số."""
    return a + b

def subtract(a, b):
    """Hàm này thực hiện phép trừ hai số."""
    return a - b

def multiply(a, b):
    """Hàm này thực hiện phép nhân hai số."""
    return a * b

def divide(a, b):
    """Hàm này thực hiện phép chia hai số. Xử lý trường hợp chia cho 0."""
    if b == 0:
        # Trả về thông báo lỗi thay vì gây ra lỗi chương trình
        return "Lỗi: Không thể chia cho số 0!"
    return a / b

# --- Lấy đầu vào từ người dùng ---
print("--- MÁY TÍNH ĐƠN GIẢN ---")
print("1. Cộng (+)")
print("2. Trừ (-)")
print("3. Nhân (*)")
print("4. Chia (/)")

try:
    # Lấy lựa chọn phép toán
    choice = input("Chọn phép toán (nhập số 1/2/3/4 hoặc ký tự +-*/): ")
    
    # Lấy hai số đầu vào
    num1 = float(input("Nhập số thứ nhất: "))
    num2 = float(input("Nhập số thứ hai: "))

except ValueError:
    print("Lỗi: Đầu vào không hợp lệ. Vui lòng chỉ nhập số cho hai giá trị đầu tiên.")
    exit()

# --- Thực hiện phép tính và hiển thị kết quả ---
result = None
operator_symbol = ""

if choice in ('1', '+'):
    result = add(num1, num2)
    operator_symbol = "+"
elif choice in ('2', '-'):
    result = subtract(num1, num2)
    operator_symbol = "-"
elif choice in ('3', '*'):
    result = multiply(num1, num2)
    operator_symbol = "*"
elif choice in ('4', '/'):
    result = divide(num1, num2)
    operator_symbol = "/"
else:
    print("Lựa chọn phép toán không hợp lệ.")

print("\n=== KẾT QUẢ ===")
if result is not None:
    print(f"{num1} {operator_symbol} {num2} = {result}")
