print("Hoang Nguyen Tuan Tu")
print("245752021610129")
print("--------------------")
# Các danh sách (list) đầu vào đã cho
l = [1, 'python', 4, 7]
k = ['cse', 2, 'guntur', 8]
m = []

# 1. Nối (kết nối) các danh sách l và k vào danh sách m
# Thêm từng phần tử của danh sách l vào m
m.extend(l) 
# Thêm từng phần tử của danh sách k vào m
m.extend(k)

# In ra danh sách m đã được nối
print(f"Danh sách m sau khi nối l và k: {m}") 

# 2. Tạo từ điển (dictionary)
# Yêu cầu của bài tập là tạo từ điển từ 'l', 'k', 'combine_list':'m'
# Ta sẽ dùng các danh sách l và k làm giá trị (value) cho các khóa 'l' và 'k'
# Danh sách m đã nối sẽ là giá trị cho khóa 'combine_list'
d = {
    'l': l,
    'k': k,
    'combine_list': m
}

# In ra từ điển kết quả
print(f"Từ điển kết quả (d): {d}")
