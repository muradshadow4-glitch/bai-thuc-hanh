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
        # Trả về "Unknown" theo gợi ý
        return "Unknown" 

class Nam(Nguoi):
    """
    Class con Nam (kế thừa từ Nguoi)
    """
    def getGender(self):
        # Ghi đè (Override) method getGender()
        return "Nam" 

class Nu(Nguoi):
    """
    Class con Nu (kế thừa từ Nguoi)
    """
    def getGender(self):
        # Ghi đè (Override) method getGender()
        return "Nữ" 

# --- CHẠY THỬ NGHIỆM BÀI 3 ---
print("\n--- Bài 3: Định nghĩa Class Nguoi, Nam, Nu ---")
aNam = Nam()
aNu = Nu()
print("Giới tính của đối tượng Nam:", aNam.getGender())
print("Giới tính của đối tượng Nữ:", aNu.getGender())
print("Giới tính của đối tượng Nguoi:", Nguoi().getGender())
