print("Hoang Nguyen Tuan Tu")
print("245752021610129")
print("--------------------")
import math

# Khởi tạo vị trí ban đầu của robot tại (0, 0)
# pos[0] là tọa độ x (ngang, LEFT/RIGHT)
# pos[1] là tọa độ y (dọc, UP/DOWN)
pos = [0, 0] 

print("--- CHƯƠNG TRÌNH MÔ PHỎNG ROBOT ---")
print("Nhập các lệnh di chuyển (ví dụ: UP 5).")
print("Nhập dòng trống (hoặc EOF) để kết thúc và tính kết quả.")

while True:
    try:
        s = input()
    except EOFError:
        # Xử lý khi kết thúc input (ví dụ: trong môi trường dòng lệnh)
        break
        
    if not s: 
        # Dừng vòng lặp khi người dùng nhập dòng trống
        break
    
    try:
        # Phân tích cú pháp lệnh (ví dụ: "UP 5" -> ["UP", "5"])
        parts = s.split()
        if len(parts) != 2:
            print(f"Lệnh không đúng định dạng: {s}")
            continue
            
        direction = parts[0].upper() # Lấy hướng và chuyển thành chữ hoa
        steps = int(parts[1])        # Lấy số bước
        
    except ValueError:
        print("Đầu vào không hợp lệ. Vui lòng nhập đúng định dạng 'HƯỚNG SỐ_BƯỚC'.")
        continue
        
    # Xử lý di chuyển
    if direction == "UP":
        pos[1] += steps
    elif direction == "DOWN":
        pos[1] -= steps
    elif direction == "LEFT":
        pos[0] -= steps
    elif direction == "RIGHT":
        pos[0] += steps
    else:
        print(f"Hướng di chuyển không hợp lệ: {direction}. Bỏ qua lệnh.")

# --- Tính toán kết quả ---
x = pos[0]
y = pos[1]

# Công thức tính khoảng cách Euclidean từ (0, 0) đến (x, y)
# D = sqrt(x^2 + y^2)
distance = math.sqrt(x**2 + y**2)

# Làm tròn khoảng cách về số nguyên gần nhất
final_distance = round(distance)

print("\n--- KẾT QUẢ CUỐI CÙNG ---")
print(f"Vị trí cuối cùng của Robot: ({x}, {y})")
print(f"Khoảng cách từ điểm bắt đầu (0,0) (làm tròn): {final_distance}")
