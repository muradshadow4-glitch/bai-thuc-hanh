print("Hoang Nguyen Tuan Tu")
print("245752021610129")
print("--------------------")
import re

def check_password_validity(password):
    """
    Kiểm tra xem mật khẩu có hợp lệ theo các tiêu chí đã định không.
    Trả về True nếu hợp lệ, ngược lại trả về False.
    """
    
    # 1. Kiểm tra độ dài: Tối thiểu 6, Tối đa 16 ký tự
    if len(password) < 6 or len(password) > 16:
        print("Mật khẩu phải có độ dài từ 6 đến 16 ký tự.")
        return False
    
    # 2. Kiểm tra ít nhất 1 chữ cái thường [a-z]
    if not re.search("[a-z]", password):
        print("Mật khẩu phải chứa ít nhất 1 chữ cái thường (a-z).")
        return False
        
    # 3. Kiểm tra ít nhất 1 số [0-9]
    if not re.search("[0-9]", password):
        print("Mật khẩu phải chứa ít nhất 1 chữ số (0-9).")
        return False
        
    # 4. Kiểm tra ít nhất 1 chữ cái hoa [A-Z]
    if not re.search("[A-Z]", password):
        print("Mật khẩu phải chứa ít nhất 1 chữ cái hoa (A-Z).")
        return False

    # 5. Kiểm tra ít nhất 1 ký tự đặc biệt [$, #, @]
    # Lưu ý: Các ký tự đặc biệt trong RegEx cần được thoát (`\`) nếu chúng có ý nghĩa đặc biệt,
    # nhưng với $, #, @ trong ngoặc vuông, chúng thường không cần.
    if not re.search("[$#@]", password):
        print("Mật khẩu phải chứa ít nhất 1 ký tự đặc biệt ($, #, @).")
        return False
        
    # Nếu vượt qua tất cả các kiểm tra
    return True

# Yêu cầu người dùng nhập mật khẩu
user_password = input("Nhập mật khẩu của bạn: ")

# Thực hiện kiểm tra
if check_password_validity(user_password):
    print("\n✅ Mật khẩu hợp lệ.")
else:
    print("\n❌ Mật khẩu không hợp lệ.")

# --- Ví dụ kiểm tra ---
# Mật khẩu hợp lệ: Abcde1$
# Mật khẩu không hợp lệ: Abc1$ (quá ngắn), abcde1$ (thiếu chữ hoa), ABCDE1$ (thiếu chữ thường)
