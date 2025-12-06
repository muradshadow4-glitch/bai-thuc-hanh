print("Hoang Nguyen Tuan Tu")
print("245752021610129")
print("--------------------")
print("--- Bài 5: In danh sách theo thứ tự ngược lại ---")
ds_bai5 = input("# Nhập dãy các từ (cách nhau bởi khoảng trắng): ").split()

# Sử dụng slicing [::-1] để tạo ra một danh sách mới là bản đảo ngược của ds_bai5
ds_nguoc = ds_bai5[::-1]

print(f"# Danh sách đảo ngược: {ds_nguoc}")
for tu in ds_nguoc:
    print(tu)
