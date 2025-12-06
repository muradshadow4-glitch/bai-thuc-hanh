print("Hoang Nguyen Tuan Tu")
print("245752021610129")
print("--------------------")
# Thiết lập giới hạn tối đa
GIOI_HAN = 4000000

# Khởi tạo hai số đầu tiên của dãy Fibonacci
# (Lưu ý: Ví dụ code mẫu trong hình bắt đầu với a=1, b=2, nên tôi sẽ dùng 1, 2)
a = 1
b = 2

# Tổng các số chẵn
total = 0

# In ra thông báo và bắt đầu in dãy
print("Dãy số Fibonacci nhỏ hơn 4,000,000:")
print(f"{a}, {b}", end="") # In hai số đầu tiên

# Vòng lặp while để tính và kiểm tra các số Fibonacci tiếp theo
# Vòng lặp chạy khi số Fibonacci hiện tại (b) vẫn nhỏ hơn giới hạn
while b < GIOI_HAN:
    # Kiểm tra nếu số hiện tại (b) là số chẵn
    if b % 2 == 0:
        # Cộng số chẵn vào tổng
        total = total + b
        
    # Tính số Fibonacci tiếp theo: next_fib = a + b
    # Cập nhật a và b cho lần lặp tiếp theo:
    # a trở thành b cũ
    # b trở thành next_fib
    a, b = b, a + b
    
    # In số mới (b) nếu nó vẫn nhỏ hơn giới hạn
    if b < GIOI_HAN:
        print(f", {b}", end="") # Tiếp tục in trên cùng một hàng

print("\n") # Xuống dòng sau khi in hết dãy
print(f"Tổng các số chẵn trong dãy Fibonacci (nhỏ hơn {GIOI_HAN:,}): {total}")

# Lưu ý: Nếu bắt đầu dãy là 1, 1, 2, 3, 5, 8... thì code cần điều chỉnh lại.
# Dựa theo code mẫu (a=1, b=2), tổng các số chẵn sẽ là: 2 + 8 + 34 + 144 + ...
# Trong trường hợp này, kết quả là 4613732 nếu giới hạn là 4,000,000 (bao gồm cả số cuối cùng)
# Tuy nhiên, đề bài nói "nhỏ hơn 4.000.000", vậy số lớn nhất là 3524578.
# Nếu tính toán đúng theo giới hạn < 4,000,000:
# Dãy: 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229, 832040, 1346269, 2178309, 3524578
# Các số chẵn: 2, 8, 34, 144, 610, 2584, 10946, 46368, 196418, 832040, 3524578
# Tổng: 4613732
