import numpy as np

print("Hoang Nguyen Tuan Tu")
print("246752021610129")
print("---------------------------------------")
print("--- Bài 11: Sắp xếp Mảng Cấu Trúc theo Lớp và Chiều cao ---")

# 1. Định nghĩa kiểu dữ liệu cấu trúc (data type)
# ('name', 'S15'): Chuỗi 15 ký tự, ('class', 'int'): Số nguyên, ('height', 'float'): Số thực
data_type = [('name', 'S15'), ('class', 'int'), ('height', 'float')]

# 2. Định nghĩa dữ liệu sinh viên
# Dữ liệu bổ sung thêm 'Nail' để thấy rõ sự sắp xếp.
students_details = [
    ('James', 5, 48.5), 
    ('Paul', 5, 52.5), 
    ('Pit', 5, 40.1),
    ('Nail', 6, 52.5) # Thêm sinh viên lớp 6
] 

# 3. Tạo mảng có cấu trúc
students = np.array(students_details, dtype=data_type)

print("\nMảng gốc (Original Array):")
print(students)

# 4. Sắp xếp mảng theo cả hai trường: ('class', 'height')
# NumPy sẽ ưu tiên sắp xếp theo trường đầu tiên ('class'). 
# Nếu các giá trị của trường đó bằng nhau, nó sẽ sử dụng trường thứ hai ('height') để sắp xếp.
sorted_students = np.sort(students, order=['class', 'height'])

print("\nMảng sau khi sắp xếp theo LỚP, sau đó là CHIỀU CAO:")
print(sorted_students)
