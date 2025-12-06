print("Hoang Nguyen Tuan Tu")
print("246752021610129")
print("----------------")
# =======================================================
# File: bai_6_vi_tri_min_max.py
# Code này sử dụng logic tìm Min/Max của Bài 5 và in ra vị trí (Bài 6)
# =======================================================

print("Hoang Nguyen Tuan Tu")
print("246752021610129")
print("---------------------------------")
print("--- Bài 6: In ra Vị trí Min/Max ---")


# --- PHẦN HÀM HỖ TRỢ (TỪ BÀI 5) ---

def get_user_list():
    """Nhận số lượng và các giá trị của list từ người dùng."""
    while True:
        try:
            so_luong = int(input("Nhập số lượng phần tử (> 0): "))
            if so_luong <= 0:
                print("Số lượng phải là số nguyên dương.")
                continue
            break
        except ValueError:
            print("Vui lòng nhập một số nguyên hợp lệ.")

    input_list = []
    print(f"Nhập {so_luong} giá trị (số) cho danh sách:")
    for i in range(so_luong):
        while True:
            try:
                gia_tri = float(input(f"Nhập giá trị thứ {i + 1}: "))
                input_list.append(gia_tri)
                break
            except ValueError:
                print("Vui lòng nhập một số hợp lệ.")
                
    return input_list

def find_min_max_by_sorting(data_list):
    """Tìm giá trị nhỏ nhất và lớn nhất bằng cách sắp xếp."""
    if not data_list:
        return None, None
    
    # Sắp xếp và lấy giá trị đầu/cuối
    sorted_list = sorted(data_list) 
    min_val = sorted_list[0]
    max_val = sorted_list[-1]
    
    return min_val, max_val


# --- HÀM CHO BÀI 6 ---

def find_all_indices(data_list, value_to_find):
    """Tìm tất cả các chỉ mục/vị trí của một giá trị trong danh sách gốc."""
    indices = []
    # Sử dụng enumerate để duyệt qua cả chỉ mục (i) và giá trị (x)
    for i, x in enumerate(data_list):
        if x == value_to_find:
            # Vị trí (chỉ mục) trong Python bắt đầu từ 0
            indices.append(i) 
    return indices

# --- CHẠY CHƯƠNG TRÌNH CHÍNH (BÀI 6) ---

# 1. Lấy danh sách từ người dùng
danh_sach_nhap = get_user_list()

if not danh_sach_nhap:
    print("Danh sách rỗng, không thể tìm vị trí Min/Max.")
else:
    # 2. Tìm giá trị Min và Max (từ Bài 5)
    min_val, max_val = find_min_max_by_sorting(danh_sach_nhap)

    # 3. Tìm vị trí của các giá trị Min và Max (từ Bài 6)
    min_indices = find_all_indices(danh_sach_nhap, min_val)
    max_indices = find_all_indices(danh_sach_nhap, max_val)

    # 4. In ra kết quả
    print("\n--- KẾT QUẢ VỊ TRÍ ---")
    print(f"Danh sách gốc: {danh_sach_nhap}")
    print("-------------------------")
    
    # In ra vị trí phần tử lớn nhất
    print(f"Phần tử LỚN NHẤT là: {max_val}")
    # Chuyển chỉ mục từ 0-based của Python sang 1-based (thân thiện với người dùng)
    print(f"Vị trí/Chỉ mục (0-based): {max_indices}")
    
    print("\n-------------------------")
    
    # In ra vị trí phần tử nhỏ nhất
    print(f"Phần tử NHỎ NHẤT là: {min_val}")
    print(f"Vị trí/Chỉ mục (0-based): {min_indices}")
