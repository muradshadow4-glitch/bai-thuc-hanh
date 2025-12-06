print("Hoang Nguyen Tuan Tu")
print("246752021610129")
print("----------------")
# =======================================================
# Bài 9 (Từ Bài tập 5, trang 32): Nối văn bản và hiển thị
# =======================================================
import os

def file_read(fname):
    """ Đọc và in toàn bộ nội dung tệp. """
    try:
        with open(fname, 'r') as f:
            print(f.read())
    except FileNotFoundError:
        print(f"Lỗi: Không tìm thấy tệp {fname}")

def write_and_display(fname):
    """
    Nối văn bản vào tệp, sau đó đọc và hiển thị nội dung tệp.
    """
    try:
        # 1. Mở tệp ở chế độ nối thêm ('a' - append) và ghi dữ liệu
        with open(fname, "a") as myfile:
            myfile.write("\nPython Exercises")
            myfile.write("\nNew Data Added.")

        print(f"\n--- Đã ghi thêm dữ liệu vào tệp '{fname}' ---")

        # 2. Đọc và hiển thị nội dung tệp (Yêu cầu hiển thị)
        print(f"\n--- Nội dung của tệp '{fname}' sau khi nối ---")
        file_read(fname)

    except Exception as e:
        print(f"Lỗi xảy ra: {e}")

# --- CHẠY THỬ NGHIỆM BÀI 9 ---
temp_file_name_9 = 'abc.txt'

# Tạo tệp mới nếu chưa tồn tại
if not os.path.exists(temp_file_name_9):
    with open(temp_file_name_9, 'w') as f:
        f.write("Initial data.")

write_and_display(temp_file_name_9)
