print("Hoang Nguyen Tuan Tu")
print("246752021610129")
print("----------------")
# =======================================================
# Bài 7: Kiểm tra Chuỗi Chứa Tất cả Chữ cái (Pangram)
# =======================================================
import string

class PangramChecker(object):
    """
    Class kiểm tra xem một chuỗi có phải là một Pangram hay không.
    (Pangram: Chuỗi chứa tất cả 26 chữ cái từ A đến Z)
    """
    def check_pangram(self, text):
        """
        Thực hiện kiểm tra Pangram.
        """
        # 1. Định nghĩa tất cả 26 chữ cái tiếng Anh (lowercase)
        alphabet = set(string.ascii_lowercase)
        
        # 2. Chuyển chuỗi đầu vào sang chữ thường và tạo một set các ký tự duy nhất
        text_chars = set(text.lower())
        
        # 3. Loại bỏ các ký tự không phải chữ cái khỏi set của chuỗi
        # Dùng phép giao (intersection) với tập hợp tất cả chữ cái.
        # Hoặc dùng phép trừ để loại bỏ: text_chars.difference(alphabet)
        
        # Cách đơn giản: Chỉ lấy ra các ký tự chữ cái trong chuỗi
        present_letters = {char for char in text_chars if 'a' <= char <= 'z'}
        
        # 4. So sánh tập hợp các chữ cái hiện có với tập hợp chữ cái chuẩn
        # Nếu hai set bằng nhau, chuỗi là một Pangram.
        return present_letters == alphabet

# --- CHẠY CHƯƠNG TRÌNH ---
print("\n--- Bài 7: Kiểm tra Pangram ---")

# Khởi tạo đối tượng
checker = PangramChecker()

# Ví dụ 1: Pangram (Chứa đủ 26 chữ cái)
pangram_ex = "The quick brown fox jumps over the lazy dog"
result_1 = checker.check_pangram(pangram_ex)

print(f"\nChuỗi 1: '{pangram_ex}'")
print(f"Kết quả (Pangram?): {result_1}") # Expected: True

# Ví dụ 2: Không phải Pangram
non_pangram_ex = "Hello World"
result_2 = checker.check_pangram(non_pangram_ex)

print(f"\nChuỗi 2: '{non_pangram_ex}'")
print(f"Kết quả (Pangram?): {result_2}") # Expected: False
