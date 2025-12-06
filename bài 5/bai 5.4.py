print("Hoang Nguyen Tuan Tu")
print("246752021610129")
print("----------------")
print("--- Bài 4: Tạo Mảng và Đảo Ngược ---")
import numpy as np
# 1. Tạo mảng với các giá trị từ 12 đến 38
# np.arange(12, 39) tạo ra mảng [12, 13, ..., 38] 
# (Lưu ý: 39 là điểm dừng, không được bao gồm)
mang_xuoi = np.arange(12, 39)

print("\nMảng được tạo (Xuôi):")
print(mang_xuoi)

# 2. Đảo ngược mảng
# Sử dụng slicing [::-1] để đảo ngược thứ tự các phần tử.
# [-1] trong slicing nghĩa là bước nhảy (step) lùi 1 đơn vị.
mang_nguoc = mang_xuoi[::-1]

print("\nMảng được đảo ngược (Ngược):")
print(mang_nguoc)
