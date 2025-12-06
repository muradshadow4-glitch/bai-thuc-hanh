print("Hoang Nguyen Tuan Tu")
print("246752021610129")
print("----------------")
# =======================================================
# Bài 8 (Từ Bài tập 2, trang 31): Đọc tệp, tính số ký tự, số từ và số dòng
# =======================================================

def analyze_file(fname):
    """
    Đọc tệp và tính số ký tự, số từ, và số dòng.
    """
    char_count = 0
    word_count = 0
    line_count = 0
    
    try:
        with open(fname, 'r') as f:
            for line in f:
                line_count += 1
                char_count += len(line)
                word_count += len(line.split())
        
        print(f"\n--- Kết quả Phân tích Tệp '{fname}' ---")
        print(f"Số ký tự (No.of chars): {char_count}")
        print(f"Số từ (No.of words): {word_count}")
        print(f"Số dòng (No.of lines): {line_count}")

    except FileNotFoundError:
        print(f"Lỗi: Không tìm thấy tệp {fname}")

# --- CHẠY THỬ NGHIỆM BÀI 8 ---
# Sử dụng lại tệp dummy đã tạo ở Bài 6
temp_file_name_8 = 'test_file_b6.txt'
analyze_file(temp_file_name_8)
