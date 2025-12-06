print("Hoang Nguyen Tuan Tu")
print("246752021610129")
print("----------------")
# =======================================================
# Bài 7: Chuyển đổi và Nối chuỗi
# =======================================================

def convert_and_join(data_list):
    """
    Chuyển đổi các phần tử trong danh sách thành chuỗi và nối chúng lại.
    """
    # Sử dụng list comprehension để gọi str() trên từng phần tử
    str_list = [str(item) for item in data_list]
    
    # Nối các chuỗi lại với nhau bằng dấu gạch ngang làm dấu phân cách
    return "-".join(str_list)

# --- CHẠY THỬ NGHIỆM BÀI 7 ---
print("\n--- Bài 7: Chuyển đổi và Nối chuỗi ---")

data = [10, "apple", 3.14, True]
result = convert_and_join(data)

print(f"Danh sách đầu vào: {data}")
print(f"Chuỗi đầu ra sau khi chuyển đổi và nối: {result}")
# Expected: 10-apple-3.14-True
