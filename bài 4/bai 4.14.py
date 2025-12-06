print("Hoang Nguyen Tuan Tu")
print("245752021610129")
print("--------------------")
## Bài 14: Sắp xếp các phần tử trong list
print("### Bài 14: Sắp xếp các phần tử trong list ###")

# Khởi tạo list mẫu
ds = ["banana", "apple", "cherry", "date"]
print(f"List gốc: {ds}")

ds.sort() # Sắp xếp list tại chỗ (in-place)

print(f"List sau khi sắp xếp: {ds}")

# In từng phần tử theo yêu cầu trong hình
print("In từng phần tử sau khi sắp xếp:")
for ch in ds:
    print(ch)
