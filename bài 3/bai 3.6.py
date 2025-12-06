print("Hoang Nguyen Tuan Tu")
print("245752021610129")
print("--------------------")
# Định nghĩa hàm get_sum(*num)
# Dấu * (dấu sao) biến các tham số truyền vào thành một tuple (num)
def get_sum(*num):
    tmp = 0
    
    # 1. Duyệt qua từng số (tham số) trong tuple 'num'
    for i in num:
        # 2. Cộng dồn vào biến tmp
        tmp += i
        
    # 3. Trả về kết quả tổng
    return tmp

# --- Thực thi chương trình ---

# Gọi hàm get_sum với 4 đối số: 1, 2, 3, 4, 5
# result sẽ lưu giá trị trả về (tổng = 15)
result = get_sum(1, 2, 3, 4, 5)

# In kết quả
print(f"Tổng của các số (1, 2, 3, 4, 5) là: {result}")
