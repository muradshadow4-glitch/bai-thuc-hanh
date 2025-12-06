print("Hoang Nguyen Tuan Tu")
print("245752021610129")
print("--------------------")
def bai_21(chuoi_dau_vao):
    """
    Tìm các số nhị phân 4 chữ số chia hết cho 5.
    """
    # 1. Phân tách chuỗi đầu vào thành danh sách các chuỗi nhị phân
    danh_sach_nhi_phan = chuoi_dau_vao.split(',')
    
    ket_qua = []
    
    # 2. Duyệt qua từng chuỗi nhị phân
    for so_nhi_phan in danh_sach_nhi_phan:
        # 3. Chuyển chuỗi nhị phân thành số nguyên (cơ số 2)
        try:
            so_nguyen = int(so_nhi_phan, 2)
        except ValueError:
            # Bỏ qua nếu chuỗi không hợp lệ (mặc dù đề bài giả định là 4 chữ số nhị phân)
            continue
            
        # 4. Kiểm tra xem số nguyên có chia hết cho 5 không
        if so_nguyen % 5 == 0:
            # 5. Nếu chia hết, thêm chuỗi nhị phân gốc vào danh sách kết quả
            ket_qua.append(so_nhi_phan)
            
    # 6. Nối danh sách kết quả lại thành chuỗi, phân tách bằng dấu phẩy
    return ','.join(ket_qua)

# Ví dụ kiểm tra
chuoi_test = "0100,0011,1010,1001"
ket_qua = bai_21(chuoi_test)
print(f"Đầu vào: {chuoi_test}")
print(f"Đầu ra: {ket_qua}") 
# 1010 là 10 trong hệ thập phân, 10 chia hết cho 5
