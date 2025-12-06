print("Hoang Nguyen Tuan Tu")
print("245752021610129")
print("--------------------")
def bai_25():
    """
    Nhận một chuỗi số phân tách bởi dấu phẩy và in ra các số lẻ.
    """
    # 1. Yêu cầu người dùng nhập chuỗi số
    chuoi_dau_vao = input("Nhập danh sách các số, phân tách bởi dấu phẩy (ví dụ: 1,2,3,4,5): ")
    
    # 2. Tách chuỗi thành danh sách các chuỗi ký tự số
    danh_sach_chuoi = chuoi_dau_vao.split(',')
    
    so_le_ket_qua = []
    
    # 3. Duyệt qua từng phần tử trong danh sách
    for phan_tu in danh_sach_chuoi:
        # Loại bỏ khoảng trắng thừa và cố gắng chuyển sang số nguyên
        try:
            so = int(phan_tu.strip()) 
        except ValueError:
            # Bỏ qua nếu phần tử không phải là số hợp lệ
            continue
        
        # 4. Kiểm tra điều kiện số lẻ (số chia cho 2 có số dư khác 0)
        if so % 2 != 0:
            # 5. Thêm số lẻ vào danh sách kết quả
            so_le_ket_qua.append(str(so)) # Chuyển lại thành chuỗi để dễ dàng in ra
            
    # 6. Nối danh sách kết quả lại thành chuỗi, phân tách bằng dấu phẩy và in ra
    print("Đầu ra:", ','.join(so_le_ket_qua))

# Chạy chương trình
print("--- Bài 25 ---")
# Bạn sẽ cần nhập dữ liệu khi chạy hàm này, ví dụ: 1,2,3,4,5,6,7,8,9
bai_25()
