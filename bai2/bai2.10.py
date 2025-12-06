print("Hoang Nguyen Tuan Tu")
print("245752021610129")
print("--------------------")
# Chuỗi ban đầu
a = "hi i am python programmer"

# 1. Tách chuỗi (split)
# Phương thức split() mặc định sẽ tách chuỗi dựa trên khoảng trắng 
# và trả về một danh sách các từ (list)
b = a.split()

# In ra danh sách sau khi tách để kiểm tra
print(f"Danh sách các từ (b) sau khi split: {b}")

# 2. Nối chuỗi (join)
# Phương thức join() được gọi trên ký tự/chuỗi phân tách 
# để nối các phần tử của danh sách (b) lại với nhau.
# Ở đây, ta dùng " * " làm ký tự phân tách
c = " * ".join(b)

# In ra chuỗi mới sau khi join
print(f"Chuỗi mới (c) sau khi join: {c}")
