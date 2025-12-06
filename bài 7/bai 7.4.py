# =======================================================
# Bài 4: Chuyển đổi Số La Mã thành Số Nguyên (Class)
# =======================================================

class RomanToInteger(object):
    """
    Class chuyển đổi một chuỗi số La Mã thành giá trị số nguyên.
    """
    def __init__(self):
        # Định nghĩa ánh xạ giá trị La Mã
        self.roman_map = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
        }

    def convert(self, roman_numeral):
        """
        Thực hiện logic chuyển đổi số La Mã sang số nguyên.
        """
        result = 0
        i = 0
        
        roman_numeral = roman_numeral.upper() # Đảm bảo xử lý cả chữ thường
        
        # Lặp qua chuỗi số La Mã
        while i < len(roman_numeral):
            s1 = self.roman_map.get(roman_numeral[i], 0) # Giá trị của ký tự hiện tại
            
            # Kiểm tra xem còn ký tự tiếp theo hay không
            if i + 1 < len(roman_numeral):
                s2 = self.roman_map.get(roman_numeral[i+1], 0) # Giá trị của ký tự tiếp theo
                
                # Logic: Nếu s1 >= s2 (ví dụ: VI, XV), cộng s1 và chuyển sang ký tự tiếp theo.
                if s1 >= s2:
                    result += s1
                    i += 1
                # Logic: Nếu s1 < s2 (ví dụ: IV, IX), cộng (s2 - s1) và bỏ qua 2 ký tự.
                else:
                    result += s2 - s1
                    i += 2
            # Nếu là ký tự cuối cùng, chỉ cần cộng s1
            else:
                result += s1
                i += 1
                
        return result

# --- CHẠY THỬ NGHIỆM BÀI 4 ---
print("Hoang Nguyen Tuan Tu")
print("246752021610129")
print("----------------")
print("--- Bài 4: Chuyển đổi Số La Mã ---")

converter = RomanToInteger()
print("IV ->", converter.convert("IV"))     # Expected: 4
print("MCMXCIV ->", converter.convert("MCMXCIV")) # Expected: 1994
