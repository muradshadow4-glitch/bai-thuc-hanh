print("Hoang Nguyen Tuan Tu")
print("245752021610129")
print("--------------------")
# Yêu cầu người dùng nhập một chuỗi
str_input = input("Enter a String: ")

# Khởi tạo một từ điển rỗng để lưu trữ số lần xuất hiện của các ký tự
char_count_dict = {}

# Lặp qua từng ký tự trong chuỗi
for char in str_input:
    # Lấy ký tự hiện tại và chuyển thành chữ thường để không phân biệt hoa/thường 
    # (Tùy chọn, nếu muốn phân biệt hoa/thường thì bỏ `.lower()`)
    char = char.lower() 
    
    # Kiểm tra xem ký tự đã có trong từ điển chưa
    if char in char_count_dict:
        # Nếu có, tăng giá trị đếm lên 1
        char_count_dict[char] += 1
    else:
        # Nếu chưa có, thêm ký tự vào từ điển với giá trị đếm là 1
        char_count_dict[char] = 1

# In ra từ điển kết quả
print(char_count_dict)

# Ví dụ khi chạy:
# Nhập: Hello World!
# Output: {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1, '!': 1}
