# =======================================================
# BÀI 1: Định nghĩa Class Circle
# =======================================================

class Circle(object): # <--- CẦN ĐẶT ĐỊNH NGHĨA CLASS TẠI ĐÂY
    """
    Class Circle được xây dựng từ bán kính (r) và có method tính diện tích.
    """
    
    def __init__(self, r):
        self.radius = r

    def area(self):
        # Công thức tính diện tích hình tròn: bán kính^2 * Pi (sử dụng 3.14)
        return self.radius**2 * 3.14

# --- CHẠY CHƯƠNG TRÌNH ---

print("Hoang Nguyen Tuan Tu")
print("246752021610129")
print("----------------")
print("--- Bài 1: Định nghĩa Class Circle ---")

# Tạo một đối tượng aCircle từ class Circle với bán kính là 2
aCircle = Circle(2)

# Gọi method area() của đối tượng aCircle và in ra kết quả
print("\nBán kính đã nhập: 2")
print("Diện tích hình tròn là:")
print(aCircle.area())

# Expected Result: 2**2 * 3.14 = 12.56
