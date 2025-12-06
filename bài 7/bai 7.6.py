# =======================================================
# Bài 6: Đọc n dòng cuối cùng của tệp
# =======================================================
import os
import sys
from collections import deque

def file_read_from_tail(fname, nlines):
    """
    Đọc và in n dòng cuối cùng của tệp.
    Sử dụng deque (double-ended queue) để lưu trữ hiệu quả.
    """
    try:
        # Mở tệp ở chế độ đọc văn bản ('r')
        with open(fname, 'r') as f:
            # deque(maxlen=nlines) chỉ giữ lại tối đa nlines phần tử.
            # Khi thêm phần tử mới, nó tự động loại bỏ phần tử cũ nhất ở đầu.
            # Điều này giúp hiệu quả hơn nhiều so với việc đọc toàn bộ tệp vào list.
            last_lines = deque(f, nlines)
            
            # last_lines lúc này chứa nlines cuối cùng
            print(f"\n--- {nlines} dòng cuối cùng của tệp '{fname}' ---")
            for line in last_lines:
                # In dòng, loại bỏ ký tự xuống dòng thừa
                print(line.rstrip('\n'))

    except FileNotFoundError:
        print(f"Lỗi: Không tìm thấy tệp {fname}")
    except Exception as e:
        print(f"Lỗi xảy ra: {e}")

# --- CHẠY THỬ NGHIỆM BÀI 6 ---
print("Hoang Nguyen Tuan Tu")
print("246752021610129")
print("246752021610129")
print("----------------")

# Tạo tệp dummy.txt để kiểm tra
temp_file_name = 'test_file_b6.txt'
if not os.path.exists(temp_file_name):
    with open(temp_file_name, 'w') as f:
        f.write("Dong 1\n")
        f.write("Dong 2\n")
        f.write("Dong 3\n")
        f.write("Dong 4\n")
        f.write("Dong 5\n")
        f.write("Dong 6\n")

# Thử nghiệm đọc 3 dòng cuối cùng
file_read_from_tail(temp_file_name, 3)
