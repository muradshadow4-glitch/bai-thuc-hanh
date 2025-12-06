print("Hoang Nguyen Tuan Tu")
print("246752021610129")
print("----------------")
# =======================================================
# Bài 5: Tìm phần tử lớn nhất và nhỏ nhất bằng phương thức sắp xếp
# =======================================================

def get_user_list():
    """
    Hàm nhận số lượng và các giá trị của list (danh sách) từ người dùng.
    """
    print("--- NHẬP DỮ LIỆU ---")
    
    # Nhập số lượng phần tử
    while True:
        try:
            so_luong = int(input("Nhập số lượng phần tử (> 0): "))
            if so_luong <= 0:
                print("Số lượng phải là số nguyên dương.")
                continue
            break
        except ValueError:
            print("Vui lòng nhập một số nguyên hợp lệ.")

    # Nhập các giá trị
    input_list = []
    print(f"Nhập {so_luong} giá trị (số) cho danh sách:")
    for i in range(so_luong):
        while True:
            try:
                gia_tri = float(input(f"Nhập giá trị thứ {i + 1}: "))
                input_list.append(gia_tri)
                break
            except ValueError:
                print("Vui lòng nhập một số hợp lệ (nguyên hoặc thực).")
                
    return input_list

def find_min_max_by_sorting(data_list):
    """
    Tìm giá trị nhỏ nhất và lớn nhất bằng cách sắp xếp danh sách.
    (Đóng vai trò là module/hàm thực hiện yêu cầu)
    """
    if not data_list:
        return None, None
    
    # Sao chép và sắp xếp danh sách theo thứ tự tăng dần
    # sorted() trả về một danh sách mới, không làm thay đổi danh sách gốc.
    sorted_list = sorted(data_list) 
    
    # Phần tử nhỏ nhất là phần tử đầu tiên của danh sách đã sắp xếp (index 0)
    min_val = sorted_list[0]
    
    # Phần tử lớn nhất là phần tử cuối cùng của danh sách đã sắp xếp (index -1)
    max_val = sorted_list[-1]
    
    return min_val, max_val

# --- CHẠY CHƯƠNG TRÌNH ---
print("Hoang Nguyen Tuan Tu")
print("246752021610129")
print("---------------------------------")
print("--- Bài 5: Tìm Min/Max bằng Sắp xếp ---")

# 1. Lấy danh sách từ người dùng
danh_sach_nhap = get_user_list()

# 2. Tìm Min/Max
min_result, max_result = find_min_max_by_sorting(danh_sach_nhap)

# 3. In kết quả (Đây là phần liên quan đến Bài 6)
print("\n--- KẾT QUẢ ---")
print(f"Danh sách đã nhập: {danh_sach_nhap}")

if min_result is not None:
    print(f"Phần tử LỚN NHẤT tìm được: {max_result}")
    print(f"Phần tử NHỎ NHẤT tìm được: {min_result}")
else:
    print("Danh sách rỗng.")
