print("Hoang Nguyen Tuan Tu")
print("245752021610129")
print("--------------------")
import math

def TinhCvDt():
    """
    Hàm này yêu cầu người dùng nhập bán kính R, kiểm tra tính hợp lệ 
    (R phải là số dương), sau đó tính và in ra Chu vi và Diện tích hình tròn.
    """
    print("--- TÍNH CHU VI VÀ DIỆN TÍCH HÌNH TRÒN ---")
    
    # 1. Nhập và kiểm tra tính hợp lệ của bán kính R
    while True:
        try:
            R = float(input("Nhập bán kính R của hình tròn: "))
            
            if R <= 0:
                print("Bán kính R phải là số dương. Vui lòng nhập lại.")
            else:
                break # Thoát khỏi vòng lặp nếu R hợp lệ
        except ValueError:
            print("Đầu vào không hợp lệ. Vui lòng nhập một giá trị số.")

    # 2. Tính toán
    # Chu vi C = 2 * pi * R
    C = 2 * math.pi * R
    
    # Diện tích S = pi * R^2
    S = math.pi * (R ** 2)
    
    # 3. In kết quả
    print("\n=== KẾT QUẢ ===")
    print(f"Bán kính R đã nhập: {R}")
    print(f"Chu vi hình tròn C: {C:.2f}") # Làm tròn 2 chữ số thập phân
    print(f"Diện tích hình tròn S: {S:.2f}") # Làm tròn 2 chữ số thập phân

# Chạy hàm
# TinhCvDt()
