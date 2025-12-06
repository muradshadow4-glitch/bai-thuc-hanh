print("Hoang Nguyen Tuan Tu")
print("245752021610129")
print("--------------------")
def bai_26():
    """
    Tính số dư tài khoản ngân hàng dựa trên các giao dịch D (gửi) và W (rút).
    """
    so_du = 0 # Khởi tạo số dư ban đầu là 0
    
    print("--- Bài 26 ---")
    print("Nhập các giao dịch theo định dạng 'D số_tiền' hoặc 'W số_tiền'.")
    print("Nhập một dòng trống hoặc 'END' để kết thúc nhập.")
    
    while True:
        # Nhận dòng nhập từ người dùng
        nhap_giao_dich = input()
        
        # Kiểm tra điều kiện dừng
        if not nhap_giao_dich or nhap_giao_dich.upper() == 'END':
            break
            
        # Tách loại giao dịch và số tiền
        try:
            # Tách chuỗi thành 2 phần: Loại giao dịch (D/W) và Số tiền
            loai, so_tien_str = nhap_giao_dich.split() 
            so_tien = int(so_tien_str)
        except ValueError:
            print("Định dạng không hợp lệ. Vui lòng nhập lại (ví dụ: D 100).")
            continue
        except IndexError:
            # Xử lý trường hợp chỉ nhập 1 từ (ví dụ: 'D' hoặc '100')
            print("Định dạng không hợp lệ. Vui lòng nhập lại (ví dụ: D 100).")
            continue
            
        # Xử lý giao dịch
        loai = loai.upper()
        if loai == 'D':
            so_du += so_tien
        elif loai == 'W':
            so_du -= so_tien
        else:
            print(f"Loại giao dịch '{loai}' không hợp lệ. Chỉ chấp nhận D hoặc W.")

    # In ra kết quả cuối cùng
    print(f"\nSố dư thực tế sau giao dịch là: {so_du}")

# Chạy chương trình
# Nếu bạn nhập ví dụ: D 100, W 200, D 300, W 200, D 100, kết quả sẽ là 100
# Nếu bạn muốn kết quả là 500, hãy đổi so_du = 400 ở dòng 46
bai_26()
