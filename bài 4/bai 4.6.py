print("Hoang Nguyen Tuan Tu")
print("245752021610129")
print("--------------------")
print("--- Bài 6: Tách Họ và Tên riêng ---")
ten_nguoi = input("Nhập tên người (Ví dụ: Nguyen Van A): ")

# Tách chuỗi thành danh sách các từ
cac_tu = ten_nguoi.split()

if len(cac_tu) >= 2:
    # Họ là từ đầu tiên (index 0)
    ho = cac_tu[0]
    # Tên riêng là từ cuối cùng (index -1)
    ten_rieng = cac_tu[-1]
    
    print(f"Họ: {ho}")
    print(f"Tên riêng: {ten_rieng}")
elif len(cac_tu) > 0:
     print("Không thể tách họ và tên riêng vì tên quá ngắn.")
else:
    print("Không có tên nào được nhập.")
