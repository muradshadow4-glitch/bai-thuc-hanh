print("Hoang Nguyen Tuan Tu")
print("245752021610129")
print("--------------------")
print("--- Bài 7: Loại bỏ chữ số khỏi chuỗi ---")
chuoi_goc = input("Nhập chuỗi (Ví dụ: ab1c2d3): ")
chuoi_moi = ""

for ky_tu in chuoi_goc:
    # Phương thức .isdigit() kiểm tra xem kí tự có phải là chữ số không (0-9)
    if not ky_tu.isdigit():
        chuoi_moi += ky_tu

print(f"Chuỗi sau khi loại bỏ chữ số: {chuoi_moi}")
