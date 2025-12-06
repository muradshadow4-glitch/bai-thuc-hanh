# =======================================================
# Bài 8 (Dự đoán): Kế thừa Class và tính Diện tích Tam giác
# =======================================================

class Polygon(object):
    """
    Class cơ sở cho Đa giác.
    Constructor nhận số cạnh (n) và khởi tạo các cạnh (sides).
    """
    def __init__(self, no_of_sides):
        self.n = no_of_sides
        # Khởi tạo danh sách chứa độ dài các cạnh (sẽ được cập nhật trong lớp con)
        self.sides = [0 for i in range(no_of_sides)] 

    def inputSides(self):
        """
        Phương thức cho phép nhập độ dài các cạnh.
        """
        self.sides = [float(input("Nhập độ dài cạnh " + str(i+1) + ": ")) for i in range(self.n)]

    def dispSides(self):
        """
        Phương thức hiển thị độ dài các cạnh.
        """
        for i in range(self.n):
            print("Cạnh", i+1, "là", self.sides[i])

class Triangle(Polygon):
    """
    Class con Tam giác (kế thừa từ Polygon, n=3).
    Method getArea() sử dụng công thức Heron để tính diện tích.
    """
    def __init__(self):
        # Gọi constructor của lớp cha để khởi tạo n=3 và 3 cạnh
        Polygon.__init__(self, 3) 

    def getArea(self):
        """
        Tính diện tích tam giác bằng công thức Heron.
        Area = sqrt(s * (s-a) * (s-b) * (s-c))
        Với s là nửa chu vi.
        """
        # Gán độ dài các cạnh vào a, b, c
        a, b, c = self.sides 
        
        # Tính nửa chu vi (s)
        s = (a + b + c) / 2
        
        # Tính diện tích
        area = (s*(s-a)*(s-b)*(s-c)) ** 0.5 
        return area

# --- CHẠY CHƯƠNG TRÌNH ---
print("Hoang Nguyen Tuan Tu")
print("246752021610129")
print("----------------")
print("--- Bài 8: Tính diện tích Tam giác (Kế thừa) ---")

# 1. Tạo đối tượng Triangle
t = Triangle()

# 2. Nhập độ dài 3 cạnh (sử dụng method của lớp cha)
# Ví dụ: Nhập 3, 4, 5
t.inputSides()

# 3. Hiển thị độ dài cạnh
t.dispSides()

# 4. Tính và in ra diện tích
print("\nDiện tích của tam giác là:")
print(t.getArea())
