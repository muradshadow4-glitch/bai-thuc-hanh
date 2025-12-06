print("Hoang Nguyen Tuan Tu")
print("246752021610129")
print("---------------------------------------")
import numpy as np

print("\n---------------------------------------")
print("--- Bài 12: Sắp xếp ID theo Chiều cao bằng lexsort ---")

# 1. Định nghĩa dữ liệu đầu vào (từ đề bài)
student_id = np.array([1023, 5202, 6230, 1671, 1682, 5241, 4532])
student_height = np.array([40, 42, 45, 41, 38, 42.0, 41])

print(f"\nID sinh viên:       {student_id}")
print(f"Chiều cao (m):     {student_height}")

# 2. Sử dụng np.lexsort() để sắp xếp
# lexsort sắp xếp dựa trên mảng cuối cùng LÀM KHÓA CHÍNH.
# Vì ta muốn sắp xếp theo CHIỀU CAO, nên student_height phải là đối số cuối cùng.
# Lệnh này trả về chỉ mục (indices) đã được sắp xếp.
indices = np.lexsort((student_id, student_height)) 

print(f"\nChỉ số (indices) sắp xếp được: {indices}")

# 3. Áp dụng các chỉ mục (indices) đã sắp xếp cho cả hai mảng
# Kết quả là ID và Chiều cao đã được sắp xếp đồng bộ theo chiều cao.

sorted_id = student_id[indices]
sorted_height = student_height[indices]

print("\n--- Dữ liệu đã sắp xếp (Theo Chiều cao tăng dần) ---")
# Hiển thị kết quả tương tự như yêu cầu của đề bài (ID và Chiều cao tương ứng)
print("ID sinh viên | Chiều cao (m)")
print("-----------------------------")
for id, h in zip(sorted_id, sorted_height):
    print(f"{id:<12} | {h:.1f}")
