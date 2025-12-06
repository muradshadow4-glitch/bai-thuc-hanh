print("Hoang Nguyen Tuan Tu")
print("246752021610129")
print("----------------")
import numpy as np

print("Hoang Nguyen Tuan Tu")
print("246752021610129")
print("---------------------------------------")
print("--- Bài 8 (Dự đoán): Thao tác với Mảng 2D ---")

# 1. Tạo một mảng 2D (Ma trận) 3x4
# Mảng chứa các giá trị từ 1 đến 12
print("\n1. Tạo Ma trận 3x4:")
arr_1d = np.arange(1, 13)
matrix = arr_1d.reshape(3, 4) # reshape() chuyển mảng 1D thành ma trận 3 hàng, 4 cột

print(matrix)

# 2. Tính Tổng các phần tử
print("\n2. Tính tổng tất cả các phần tử:")
total_sum = np.sum(matrix)
print(f"Tổng tất cả các phần tử: {total_sum}")

# 3. Tính Tổng theo Cột (Trục dọc - axis=0)
# Kết quả là một mảng 1D, mỗi phần tử là tổng của một cột
print("\n3. Tính tổng theo CỘT (axis=0):")
sum_by_column = np.sum(matrix, axis=0)
print(f"Tổng theo cột: {sum_by_column}")

# 4. Tính Tổng theo Hàng (Trục ngang - axis=1)
# Kết quả là một mảng 1D, mỗi phần tử là tổng của một hàng
print("\n4. Tính tổng theo HÀNG (axis=1):")
sum_by_row = np.sum(matrix, axis=1)
print(f"Tổng theo hàng: {sum_by_row}")
