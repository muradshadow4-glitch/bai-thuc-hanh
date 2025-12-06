print("Hoang Nguyen Tuan Tu")
print("246752021610129")
print("----------------")
import numpy as np

print("Hoang Nguyen Tuan Tu")
print("246752021610129")
print("---------------------------------------")
print("--- Bài 9 (Dự đoán): Phép Nhân Ma Trận ---")

# 1. Định nghĩa Ma trận A (ví dụ: 2x3)
A = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print("\nMa trận A (2x3):")
print(A)

# 2. Định nghĩa Ma trận B (ví dụ: 3x2)
# Số cột của A (3) phải bằng số hàng của B (3)
B = np.array([
    [7, 8],
    [9, 10],
    [11, 12]
])

print("\nMa trận B (3x2):")
print(B)

# 3. Thực hiện Phép Nhân Ma Trận (A x B)
# Kết quả là ma trận C (2x2)
# C = (2x3) x (3x2) = (2x2)

# Cách 1: Sử dụng np.dot()
C_dot = np.dot(A, B)

# Cách 2: Sử dụng toán tử @ (cách viết hiện đại hơn)
C_at = A @ B

print("\nKết quả Phép Nhân Ma Trận C = A @ B (2x2):")
print(C_at)

# 4. Tìm Ma trận Chuyển vị (Transpose) của A
# Phép chuyển vị đảo ngược số hàng và số cột (2x3 -> 3x2)
A_transpose = A.T

print("\nMa trận Chuyển vị của A (A.T - 3x2):")
print(A_transpose)
