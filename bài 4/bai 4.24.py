print("Hoang Nguyen Tuan Tu")
print("245752021610129")
print("--------------------")
def bai_24(cau_dau_vao):
    """
    Đếm số lượng chữ cái in hoa và in thường trong một chuỗi.
    """
    so_chu_hoa = 0
    so_chu_thuong = 0
    
    # Duyệt qua từng ký tự trong chuỗi đầu vào
    for ky_tu in cau_dau_vao:
        # Kiểm tra xem ký tự có phải là chữ cái in hoa không (A-Z)
        if ky_tu.isupper():
            so_chu_hoa += 1
        # Kiểm tra xem ký tự có phải là chữ cái in thường không (a-z)
        elif ky_tu.islower():
            so_chu_thuong += 1
        # Các ký tự khác (khoảng trắng, dấu câu, chữ số, v.v.) sẽ bị bỏ qua
        
    print(f"Chữ hoa: {so_chu_hoa}")
    print(f"Chữ thường: {so_chu_thuong}")

# Ví dụ kiểm tra
cau_test = "Dai Hoc Vinh"
print(f"Đầu vào: {cau_test}")
bai_24(cau_test) 
# Chữ hoa: D, H, V -> 3
# Chữ thường: a, i, o, c, i, n, h -> 7
