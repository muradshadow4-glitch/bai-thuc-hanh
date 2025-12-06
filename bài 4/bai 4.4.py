print("Hoang Nguyen Tuan Tu")
print("245752021610129")
print("--------------------")
print("--- Bài 4: Nhập và in danh sách từ một dòng ---")

# .split() mặc định sẽ tách chuỗi theo bất kỳ khoảng trắng nào (space, tab)
# và trả về một list (danh sách) các chuỗi con.
ds = input("# Nhập dãy vừa nhập (cách nhau bởi khoảng trắng hoặc tab): ").split()

print(f"# In dãy vừa nhập: {ds}")
for phan_tu in ds:
    print(phan_tu)
