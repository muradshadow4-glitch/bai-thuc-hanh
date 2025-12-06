print("Hoang Nguyen Tuan Tu")
print("245752021610129")
print("--------------------")
## Bài 15: Nhập chuỗi từ, tách và sắp xếp
print("\n### Bài 15: Tách và sắp xếp từ điển ###")

chuoi_tu = input("15. Hãy nhập chuỗi từ tiếng Anh viết tách nhau bởi dấu cách: ")
# Mặc định split() sẽ tách chuỗi dựa trên khoảng trắng
list_tu = chuoi_tu.split() 

list_tu.sort() # Sắp xếp theo thứ tự từ điển

print("Các từ sau khi sắp xếp:")
for tu in list_tu:
    print(tu)
