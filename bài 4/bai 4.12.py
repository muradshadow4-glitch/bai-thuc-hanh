print("Hoang Nguyen Tuan Tu")
print("245752021610129")
print("--------------------")
# 12. Bỏ phần tử từ list
print("\n### Bài 12: Bỏ phần tử từ list (.remove) ###")

# Yêu cầu: List 'ds' phải có dữ liệu.
if 'ds' not in locals():
    # Giả sử List gốc nếu Bài 9 chưa chạy
    ds = ['red', 'green', 'blue', '123', 'yellow']
    print(f"*Sử dụng list mẫu: {ds}*")

phan_tu_can_xoa = '123'

try:
    ds.remove(phan_tu_can_xoa)
    print(f"Đã xóa thành công phần tử '{phan_tu_can_xoa}'")
except ValueError:
    print(f"Lỗi: Không tìm thấy phần tử '{phan_tu_can_xoa}' trong list để xóa.")

print(f"List 'ds' sau khi xóa: {ds}")

# In từng phần tử trong ds
print("In từng phần tử trong ds:")
for ch in ds:
    print(ch)
