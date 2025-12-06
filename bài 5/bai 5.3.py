print("Hoang Nguyen Tuan Tu")
print("245752021610129")
print("--------------------")
import numpy as np

# =======================================================
# 3. Viết chương trình sử dụng thư viện NumPy để tạo một mảng 
#    với các giá trị nằm trong khoảng từ 12 đến 38.
# =======================================================

print("--- Bài 3: Tạo Mảng NumPy từ 12 đến 38 ---")

# numpy.arange(start, stop, step) tạo ra các giá trị
# trong khoảng [start, stop) - bao gồm 'start', KHÔNG bao gồm 'stop'.
# Để bao gồm giá trị 38, ta phải đặt 'stop' là 39.
x = np.arange(12, 39) 
print("Mảng tạo được:")
print(x)

print("\n") # Xuống dòng cho dễ nhìn

