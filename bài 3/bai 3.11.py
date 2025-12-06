print("Hoang Nguyen Tuan Tu")
print("245752021610129")
print("--------------------")
def benefit(t, n, k):
    """
    Hàm tính tổng số tiền nhận được sau k tháng gửi tiết kiệm (lãi kép hàng tháng).
    
    Tham số:
    t (float): Lãi suất (đơn vị: %, ví dụ: 0.8 cho 0.8%)
    n (float): Số vốn ban đầu
    k (int): Số tháng gửi tiết kiệm
    
    Trả về:
    float: Tổng số tiền nhận được.
    """
    # Chuyển lãi suất t% thành tỷ lệ (r) cho mỗi tháng
    # Giả sử t là lãi suất hàng tháng
    r = t / 100.0 
    
    # Công thức lãi kép: A = P * (1 + r)^k
    total_amount = n * ((1 + r) ** k)
    
    return total_amount

# --- Lấy đầu vào và kiểm tra dữ liệu ---
print("\n--- TÍNH TIỀN LÃI TIẾT KIỆM (Lãi kép hàng tháng) ---")

try:
    # Lãi suất (t%)
    t_percent = float(input("Nhập lãi suất hàng tháng t% (ví dụ: 0.8 cho 0.8%): "))
    
    # Vốn ban đầu (n)
    n_capital = float(input("Nhập số vốn ban đầu n (đồng): "))
    
    # Số tháng (k)
    k_months = int(input("Nhập số tháng gửi tiết kiệm k: "))

    if n_capital <= 0 or k_months <= 0 or t_percent < 0:
        print("\nLỗi: Số vốn, số tháng phải dương và lãi suất không âm.")
    else:
        # Tính toán kết quả
        final_benefit = benefit(t_percent, n_capital, k_months)
        
        # In kết quả
        print("\n=== KẾT QUẢ ===")
        print(f"Vốn ban đầu: {n_capital:,.0f} đồng")
        print(f"Lãi suất hàng tháng: {t_percent}%")
        print(f"Số tháng gửi: {k_months} tháng")
        print(f"Tổng số tiền nhận được sau {k_months} tháng: {final_benefit:,.0f} đồng")

except ValueError:
    print("\nLỗi: Đầu vào không hợp lệ. Vui lòng nhập đúng định dạng số.")
