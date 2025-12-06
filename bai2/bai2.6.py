print("Hoang Nguyen Tuan Tu")
print("245752021610129")
print("--------------------")
# Khởi tạo một danh sách rỗng để lưu trữ các số thỏa mãn điều kiện
ket_qua = []

# Vòng lặp for để duyệt qua tất cả các số trong đoạn [2000, 3200]
# range(2000, 3201) sẽ bao gồm 2000 đến 3200
for so in range(2000, 3201):
    
    # Kiểm tra điều kiện 1: Số chia hết cho 7 (so % 7 == 0)
    # AND
    # Kiểm tra điều kiện 2: Số KHÔNG chia hết cho 5 (so % 5 != 0)
    if (so % 7 == 0) and (so % 5 != 0):
        # Nếu thỏa mãn cả hai điều kiện, chuyển số đó thành chuỗi và thêm vào danh sách
        ket_qua.append(str(so))

# In ra kết quả: nối tất cả các chuỗi trong danh sách lại với nhau, cách nhau bởi dấu phẩy và khoảng trắng
print(", ".join(ket_qua))
