
# =======================================================
# Bài 10: Xây dựng hàm bubblesort(list) (Sắp xếp Nổi bọt)
# =======================================================

print("Hoang Nguyen Tuan Tu")
print("246752021610129")
print("---------------------------------")
print("--- Bài 10: Sắp xếp Nổi bọt (Bubble Sort) ---")

def bubblesort(input_list):
    """
    Sắp xếp danh sách bằng thuật toán Sắp xếp Nổi bọt.
    Sử dụng cờ 'swapped' để tối ưu hóa (thoát sớm nếu danh sách đã sắp xếp).
    """
    list_counts = len(input_list)
    
    # Lặp qua tất cả các phần tử của mảng
    # i là số lần lặp, mỗi lần lặp sẽ đẩy phần tử lớn nhất về cuối
    for i in range(list_counts - 1): 
        # Giả định ban đầu là không có sự trao đổi nào xảy ra trong lần lặp này
        swapped = False
        
        # Vòng lặp bên trong: So sánh các cặp phần tử liền kề
        # list_counts - 1 - i: Giảm phạm vi tìm kiếm vì i phần tử cuối cùng đã được sắp xếp
        for j in range(list_counts - 1 - i): 
            
            # So sánh hai phần tử liền kề (j và j+1)
            # Nếu phần tử hiện tại lớn hơn phần tử tiếp theo, thực hiện hoán đổi
            if input_list[j] > input_list[j + 1]:
                
                # Thực hiện hoán đổi vị trí
                # Đây là cách viết hoán đổi ngắn gọn (Pythonic swap)
                input_list[j], input_list[j + 1] = input_list[j + 1], input_list[j]
                
                swapped = True # Đánh dấu rằng đã có hoán đổi xảy ra
        
        # Nếu không có hai phần tử nào được hoán đổi trong vòng lặp bên trong,
        # tức là danh sách đã được sắp xếp. Thoát khỏi vòng lặp bên ngoài (tối ưu hóa).
        if not swapped:
            break
            
    return input_list

# --- VIẾT CHƯƠNG TRÌNH NHẬP/HIỂN THỊ DỮ LIỆU ---

def bai_10_main():
    """
    Chương trình chính để nhập dữ liệu và sử dụng module bubblesort.
    """
    # Dữ liệu mẫu (Sample Data) từ tài liệu: [14, 46, 27, 57, 41, 45, 21, 70]
    sample_data = [14, 46, 27, 57, 41, 45, 21, 70]
    
    print("\nDanh sách gốc (Sample Data):")
    print(sample_data)
    
    # Gọi hàm/module bubblesort để sắp xếp danh sách
    sorted_list = bubblesort(sample_data)
    
    print("\nDanh sách sau khi sắp xếp bằng Bubble Sort:")
    print(sorted_list)
    # Expected Result: [14, 21, 27, 41, 45, 46, 57, 70]
    
# Chạy chương trình chính
bai_10_main()
