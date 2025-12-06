print("Hoang Nguyen Tuan Tu")
print("245752021610129")
print("--------------------")
import math

# Yêu cầu người dùng nhập bán kính r
# Sử dụng float() để đảm bảo bán kính có thể là số thập phân
try:
    r = float(input("Nhập bán kính r của hình tròn: "))
    
    # Kiểm tra bán kính phải là số dương
    if r <= 0:
        print("Bán kính phải là một số dương.")
    else:
        # Tính Diện tích
        # S = pi * r^2
        dien_tich = math.pi * (r ** 2)
        
        # Tính Chu vi
        # C = 2 * pi * r
        chu_vi = 2 * math.pi * r
        
        # In kết quả, làm tròn đến 2 chữ số thập phân cho dễ đọc
        print("-" * 30)
        print(f"Bán kính r: {r}")
        print(f"Hằng số Pi sử dụng: {math.pi}")
        print(f"Diện tích (S): {dien_tich:.2f}")
        print(f"Chu vi (C): {chu_vi:.2f}")
        print("-" * 30)
        
except ValueError:
    print("Đầu vào không hợp lệ. Vui lòng nhập một giá trị số.")
    
