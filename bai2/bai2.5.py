print("Hoang Nguyen Tuan Tu")
print("245752021610129")
print("--------------------")
# Yêu cầu người dùng nhập một số nguyên n
n = int(input("Enter A Number ---> "))

# Vòng lặp while để xử lý từng chữ số của n
# Vòng lặp chạy cho đến khi n bằng 0 (không còn chữ số nào)
while n > 0:
    # 1. Lấy chữ số cuối cùng (số dư khi chia cho 10)
    chu_so = n % 10
    
    # 2. In chữ số đó ra màn hình
    print(chu_so)
    
    # 3. Loại bỏ chữ số cuối cùng (chia lấy phần nguyên cho 10)
    n = n // 10

# Ví dụ: Nếu n = 123
# Lần 1: print(3), n = 12
# Lần 2: print(2), n = 1
# Lần 3: print(1), n = 0. Vòng lặp kết thúc.
