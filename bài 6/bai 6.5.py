print("Hoang Nguyen Tuan Tu")
print("246752021610129")
print("----------------")
# =======================================================
# Bài 5: Đảo Ngược Chuỗi từ Từng Chữ (Class)
# =======================================================

class ReverseString(object):
    """
    Class đảo ngược thứ tự các từ trong một chuỗi.
    """
    def reverse_words(self, input_string):
        """
        Thực hiện đảo ngược chuỗi từ từng chữ.
        Ví dụ: "hello .py" -> ".py hello"
        """
        # 1. Tách chuỗi thành một danh sách các từ
        words = input_string.split()
        
        # 2. Đảo ngược danh sách các từ (sử dụng slicing [::-1])
        reversed_words = words[::-1]
        
        # 3. Nối các từ đã đảo ngược lại thành một chuỗi, cách nhau bởi dấu cách
        return " ".join(reversed_words)

# --- CHẠY CHƯƠNG TRÌNH ---
print("\n--- Bài 5: Đảo Ngược Chuỗi từ Từng Chữ ---")

# Khởi tạo đối tượng
reverser = ReverseString()

# Ví dụ thử nghiệm
input_data = "hello .py"
result = reverser.reverse_words(input_data)

print(f"Dữ liệu vào: '{input_data}'")
print(f"Đầu ra: '{result}'") # Expected: .py hello

# Ví dụ khác
input_data_2 = "Viết code bài 5"
result_2 = reverser.reverse_words(input_data_2)
print(f"\nDữ liệu vào: '{input_data_2}'")
print(f"Đầu ra: '{result_2}'") # Expected: 5 bài code Viết
