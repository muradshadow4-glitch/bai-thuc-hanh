# =======================================================
# Bài 7: Tạo mảng có cấu trúc NumPy và Sắp xếp theo chiều cao
# =======================================================

import numpy as np

print("Hoang Nguyen Tuan Tu")
print("246752021610129")
print("---------------------------------------")
print("--- Bài 7: Mảng Có Cấu Trúc NumPy ---")

# 1. Định nghĩa kiểu dữ liệu (dtype) cho mảng có cấu trúc
data_type = [
    ('name', 'S15'),    # Tên (String, max 15 ký tự)
    ('class', int),     # Lớp (Integer)
    ('height', float)   # Chiều cao (Float)
]

# 2. Định nghĩa dữ liệu đầu vào
# Dữ liệu mẫu đã được cung cấp trong tài liệu
students_details = [
    ('James', 5, 48.5),
    ('Nail', 6, 52.5),
    ('Paul', 5, 42.10),
    ('Pir', 5, 40.11)
]

# 3. Tạo Mảng Có Cấu Trúc (Structured Array)
# Tạo mảng NumPy từ dữ liệu và kiểu dữ liệu đã định nghĩa
students = np.array(students_details, dtype=data_type)

print("\nMảng Sinh viên Gốc (Chưa sắp xếp):")
print(students)

# 4. Sắp xếp Mảng theo cột 'height'
# np.sort() sẽ tạo ra một bản sao đã sắp xếp của mảng
# order='height' chỉ định tên cột (trường) để sắp xếp
sorted_students = np.sort(students, order='height')

print("\nKết quả sắp xếp theo chiều cao ('height'):")
print(sorted_students)

# Kết quả mong đợi:
# [('Pir', 5, 40.11)]
# [('Paul', 5, 42.1)]
# [('James', 5, 48.5)]
# [('Nail', 6, 52.5)]
