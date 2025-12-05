print("Hoang Nguyen Tuan Tu")
print("245752021610129")
print("--------------------")
import math

# Nhập tọa độ điểm thứ nhất (x1, y1)
x1 = int(input("Enter x1 ---> "))
y1 = int(input("Enter y1 ---> "))

# Nhập tọa độ điểm thứ hai (x2, y2)
x2 = int(input("Enter x2 ---> "))
y2 = int(input("Enter y2 ---> "))

# Tính bình phương các hiệu tọa độ
d1 = (x2 - x1)**2  # (x2 - x1)^2
d2 = (y2 - y1)**2  # (y2 - y1)^2

# Tính căn bậc hai của tổng d1 + d2 để tìm khoảng cách
res = math.sqrt(d1 + d2)

# In kết quả khoảng cách
print("Distance between two points:", res)
