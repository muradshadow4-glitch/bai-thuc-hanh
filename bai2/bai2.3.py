print("Hoang Nguyen Tuan Tu")
print("245752021610129")
print("--------------------")
# Yêu cầu người dùng nhập một số nguyên
n = int(input("Enter a number ---> "))

# Kiểm tra số đó là chẵn hay lẻ
# Một số là chẵn nếu chia hết cho 2 (số dư bằng 0)
if n % 2 == 0:
    print("EVEN Number")
else:
    # Nếu không chia hết cho 2 (số dư là 1), thì là số lẻ
    print("ODD Number")
