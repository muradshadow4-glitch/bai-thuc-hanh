print("Hoang Nguyen Tuan Tu")
print("245752021610129")
print("--------------------")
# 10. Cắt list: lấy những phần tử đầu (đến phần tử áp chót)
print("\n### Bài 10: Cắt list (ds[0:-1]) ###")

# Yêu cầu: List 'ds' phải có dữ liệu từ Bài 9.
if 'ds' not in locals():
    # Giả sử List gốc nếu Bài 9 chưa chạy
    ds = ['apple', 'banana', 'cherry', 'date', 'elderberry']
    print(f"*Sử dụng list mẫu: {ds}*")

x = ds[0:-1] 

print(f"List 'x' (kết quả của ds[0:-1]): {x}")

# In từng phần tử trong x
print("In từng phần tử trong x:")
for c in x:
    print(c)
