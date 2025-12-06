print("Hoang Nguyen Tuan Tu")
print("246752021610129")
print("----------------")
# =======================================================
# Bài 2: Định nghĩa Class Hinhchunhat
# =======================================================

class Hinhchunhat(object):
    """
    Class Hinhchunhat được xây dựng từ chiều dài (l) và chiều rộng (w).
    """
    
    # Method khởi tạo (Constructor)
    def __init__(self, l, w):
        # Lưu chiều dài và chiều rộng
        self.length = l
        self.width = w

    # Method tính diện tích (Area method)
    def area(self):
        # Công thức tính diện tích hình chữ nhật: chiều dài * chiều rộng
        return self.length * self.width

# --- CHẠY CHƯƠNG TRÌNH ---

print("Hoang Nguyen Tuan Tu")
print("246752021610129")
print("----------------")
print("--- Bài 2: Định nghĩa Class Hinhchunhat ---")

# Tạo một đối tượng hcn1 từ class Hinhchunhat với chiều dài=5, chiều rộng=3
hcn1 = Hinhchunhat(5, 3)

# Gọi method area() và in ra kết quả
print("\nChiều dài đã nhập: 5")
print("Chiều rộng đã nhập: 3")
print("Diện tích hình chữ nhật là:")
print(hcn1.area()) # Expected: 15
