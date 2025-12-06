print("Hoang Nguyen Tuan Tu")
print("245752021610129")
print("--------------------")
# 13. Tìm kiếm phần tử trong list
print("\n### Bài 13: Tìm kiếm phần tử trong list (.index) ###")

# Yêu cầu: List 'ds' phải có dữ liệu.
if 'ds' not in locals():
    # Giả sử List gốc nếu Bài 9 chưa chạy
    ds = ['alpha', 'beta', 'abc', 'gamma']
    print(f"*Sử dụng list mẫu: {ds}*")

phan_tu_tim_kiem = 'abc'

try:
    vi_tri = ds.index(phan_tu_tim_kiem)
    # Cú pháp in theo hình
    print(f"vị trí của {phan_tu_tim_kiem} là {vi_tri}")
except ValueError:
    print(f"Lỗi: Không tìm thấy phần tử '{phan_tu_tim_kiem}' trong list.")
