# =======================================================
# Bài 1: Định nghĩa Class Circle
# =======================================================

class Circle(object):
    """
    Class Circle được xây dựng từ bán kính (r) và có method tính diện tích.
    """
    
    # Method khởi tạo (Constructor)
    def __init__(self, r):
        # Lưu bán kính vào thuộc tính self.radius
        self.radius = r

    # Method tính diện tích (Area method)
    def area(self):
        # Công thức tính diện tích hình tròn: bán kính^2 * Pi (sử dụng 3.14)
        return self.radius**2 * 3.14

# --- CHẠY THỬ NGHIỆM BÀI 1 ---
print("Hoang Nguyen Tuan Tu")
print("246752021610129")
print("----------------")
print("--- Bài 1: Định nghĩa Class Circle ---")
aCircle = Circle(2)
print("Diện tích hình tròn (bán kính=2):")
print(aCircle.area())
