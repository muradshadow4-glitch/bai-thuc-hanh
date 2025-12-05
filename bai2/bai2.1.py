print("Hoang nguyen tuan tu")
print("mssv:245752021610129")
print("--------------------")
# Yêu cầu người dùng nhập hai giá trị n1 và n2
n1 = int(input("Enter n1 value: "))
n2 = int(input("Enter n2 value: "))

# So sánh n1 và n2
if n1 > n2:
    # Nếu n1 lớn hơn n2, in ra n1 là số lớn hơn
    print("n1 is big")
elif n2 > n1:
    # Nếu n2 lớn hơn n1, in ra n2 là số lớn hơn
    print("n2 is big")
else:
    # Trường hợp n1 bằng n2 (bổ sung cho trường hợp còn thiếu trong code mẫu)
    print("n1 is equal to n2")
