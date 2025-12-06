print("Hoang Nguyen Tuan Tu")
print("245752021610129")
print("--------------------")
# Yêu cầu người dùng nhập số nguyên n
# n = int(input("Nhập vào một số nguyên n: "))

# Để tiện chạy thử, tôi sẽ đặt n = 8 như ví dụ:
n = 8 
print(f"Nhập n = {n}")

# Khởi tạo một dictionary rỗng
d = dict()

# Vòng lặp for để duyệt qua các số nguyên i từ 1 đến n
# range(1, n + 1) sẽ bao gồm n
for i in range(1, n + 1):
    # Thêm cặp (key, value) vào dictionary: key là i, value là i*i (i^2)
    d[i] = i * i

# In ra dictionary đã tạo
print(d)

# Kết quả (với n=8): {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
