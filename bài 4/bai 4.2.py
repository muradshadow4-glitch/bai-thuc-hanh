print("Hoang Nguyen Tuan Tu")
print("245752021610129")
print("--------------------")
print("--- Bài 2: Bỏ qua kí tự không nhìn thấy (space, tab) ---")
S_bai2 = input("Nhập chuỗi S (có dấu cách/tab): ")

for ch in S_bai2:
    # Điều kiện kiểm tra: nếu kí tự KHÔNG phải là dấu cách ' ' VÀ KHÔNG phải là dấu tab '\t'
    if ch != ' ' and ch != '\t':
        print(ch)
