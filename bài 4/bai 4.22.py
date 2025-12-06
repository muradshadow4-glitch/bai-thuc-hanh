print("Hoang Nguyen Tuan Tu")
print("245752021610129")
print("--------------------")
def bai_22():
    """
    Tìm các số trong đoạn [1000, 3000] mà tất cả các chữ số đều là số chẵn.
    """
    ket_qua = []
    
    # Duyệt qua tất cả các số từ 1000 đến 3000
    for so in range(1000, 3001):
        # Chuyển số thành chuỗi để dễ dàng kiểm tra từng chữ số
        chuoi_so = str(so)
        
        # Biến cờ để kiểm tra điều kiện
        tat_ca_chan = True 
        
        # Duyệt qua từng chữ số trong chuỗi
        for chu_so in chuoi_so:
            # Chuyển chữ số thành số nguyên để kiểm tra tính chẵn lẻ
            digit = int(chu_so)
            
            # Kiểm tra xem chữ số có phải là số lẻ không
            if digit % 2 != 0:
                # Nếu là số lẻ (1, 3, 5, 7, 9) thì đặt cờ thành False và thoát khỏi vòng lặp kiểm tra chữ số
                tat_ca_chan = False
                break
                
        # Nếu cờ vẫn là True (nghĩa là tất cả chữ số đều là số chẵn)
        if tat_ca_chan:
            # Thêm chuỗi số vào danh sách kết quả
            ket_qua.append(chuoi_so)
            
    # Nối danh sách kết quả lại thành chuỗi, phân tách bằng dấu phẩy
    return ','.join(ket_qua)

ket_qua = bai_22()
print(f"Các số thỏa mãn: {ket_qua}") 
# Ví dụ: 2000, 2002, 2004, 2006, 2008, 2020, ...
