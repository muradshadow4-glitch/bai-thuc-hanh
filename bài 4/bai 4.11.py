print("Hoang Nguyen Tuan Tu")
print("245752021610129")
print("--------------------")
# 11. Thêm phần tử vào list
print("\n### Bài 11: Thêm phần tử vào list (.append) ###")

# Yêu cầu: List 'ds' phải có dữ liệu.
if 'ds' not in locals():
    # Giả sử List gốc nếu Bài 9 chưa chạy
    ds = ['A', 'B', 'C']
    print(f"*Sử dụng list mẫu: {ds}*")

phan_tu_moi = 'abc'
ds.append(phan_tu_moi)

print(f"List 'ds' sau khi thêm '{phan_tu_moi}': {ds}")

# In từng phần tử trong ds
print("In từng phần tử trong ds:")
for ch in ds:
    print(ch)
