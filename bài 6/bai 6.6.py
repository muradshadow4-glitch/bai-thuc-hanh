# =======================================================
# Bài 6: Chuyển đổi Số Nguyên thành Số La Mã (Class)
# =======================================================

class IntegerToRoman(object):
    """
    Class chuyển đổi một số nguyên (trong phạm vi 1 đến 3999) thành số La Mã.
    """
    def __init__(self):
        # Định nghĩa ánh xạ giá trị La Mã và số nguyên tương ứng (từ lớn đến nhỏ)
        self.val_map = {
            1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 
            50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'
        }

    def convert(self, num):
        """
        Thực hiện logic chuyển đổi số nguyên sang số La Mã.
        """
        if not 1 <= num <= 3999:
            return "Số nguyên phải nằm trong khoảng 1 đến 3999"
        
        roman = ""
        # Duyệt qua các cặp giá trị/ký tự trong ánh xạ
        for value, symbol in self.val_map.items():
            # Lấy số lần ký tự hiện tại có thể được lặp lại
            count = num // value
            roman += symbol * count
            # Cập nhật số nguyên còn lại
            num %= value
            
        return roman

# --- CHẠY CHƯƠNG TRÌNH ---
print("Hoang Nguyen Tuan Tu")
print("246752021610129")
print("----------------")
print("--- Bài 6: Chuyển đổi Số Nguyên thành Số La Mã ---")

# Khởi tạo đối tượng
converter = IntegerToRoman()

# Các ví dụ thử nghiệm
print("94 ->", converter.convert(94))   # Expected: XCIV
print("58 ->", converter.convert(58))   # Expected: LVIII
print("1994 ->", converter.convert(1994)) # Expected: MCMXCIV
