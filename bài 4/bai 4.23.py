print("Hoang Nguyen Tuan Tu")
print("245752021610129")
print("--------------------")
def bai_23(cau_dau_vao):
    """
    Đếm số chữ cái và chữ số trong một chuỗi.
    """
    so_chu_cai = 0
    so_chu_so = 0
    
    # Duyệt qua từng ký tự trong chuỗi đầu vào
    for ky_tu in cau_dau_vao:
        # Kiểm tra xem ký tự có phải là chữ cái không (A-Z, a-z)
        if ky_tu.isalpha():
            so_chu_cai += 1
        # Kiểm tra xem ký tự có phải là chữ số không (0-9)
        elif ky_tu.isdigit():
            so_chu_so += 1
        # Các ký tự khác (khoảng trắng, dấu câu, v.v.) sẽ bị bỏ qua
        
    print(f"Số chữ cái là: {so_chu_cai}")
    print(f"Số chữ số là: {so_chu_so}")
    
# Ví dụ kiểm tra
cau_test = "hello world! 123"
print(f"Đầu vào: {cau_test}")
bai_23(cau_test) 
# Chữ cái: h, e, l, l, o, w, o, r, l, d -> 10
# Chữ số: 1, 2, 3 -> 3
