print("Hoang Nguyen Tuan Tu")
print("246752021610129")
print("----------------")
# =======================================================
# Bài 3: Định nghĩa Class Nguoi, Nam, Nu (Kế thừa)
# =======================================================

class Nguoi(object):
    """
    Class cha cơ sở (Base Class)
    """
    def getGender(self):
        return "Unknown" # Trả về "Unknown" theo gợi ý

class Nam(Nguoi):
    """
    Class con Nam (kế thừa từ Nguoi)
    """
    def getGender(self):
        return "Nam" # Ghi đè (Override) method getGender()

class Nu(Nguoi):
    """
    Class con Nu (kế thừa từ Nguoi)
    """
    def getGender(self):
        return "Nữ" # Ghi đè (Override) method getGender()

# --- CHẠY CHƯƠNG TRÌNH ---

print("\n--- Bài 3: Định nghĩa Class Nguoi, Nam, Nu ---")

# Tạo các đối tượng
aNam = Nam()
aNu = Nu()
aNguoi = Nguoi()

# Gọi method getGender() và in ra kết quả
print("\nGiới tính của đối tượng Nam:")
print(aNam.getGender())

print("\nGiới tính của đối tượng Nữ:")
print(aNu.getGender())

print("\nGiới tính của đối tượng Nguoi (Không xác định):")
print(aNguoi.getGender())
