print("Hoang Nguyen Tuan Tu")
print("246752021610129")
print("----------------")
import numpy as np

print("Hoang Nguyen Tuan Tu")
print("246752021610129")
print("---------------------------------------")
print("--- Bài 7: Sắp xếp Mảng Cấu Trúc NumPy ---")

# 1. Định nghĩa kiểu dữ liệu cấu trúc (data type)
# <S15: Chuỗi 15 ký tự, int: Số nguyên, float: Số thực)
data_type = [('name', 'S15'), ('class', 'int'), ('height', 'float')]

# 2. Định nghĩa dữ liệu sinh viên
students_details = [
    ('James', 5, 48.5), 
    ('Paul', 5, 52.5), 
    ('Pit', 5, 40.1)] 

# 3. Tạo mảng có cấu trúc (structured array)
students = np.array(students_details, dtype=data_type)

print("\nOriginal array (Mảng gốc):")
print(students)

# 4. Sắp xếp mảng theo trường 'height'
# numpy.sort trả về một mảng mới đã được sắp xếp.
# order='height' chỉ định cột cần sắp xếp.
sorted_students = np.sort(students, order='height')

print("\nSorted by height (Sắp xếp theo chiều cao):")
print(sorted_students)
