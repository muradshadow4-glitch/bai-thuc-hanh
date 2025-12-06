print("Hoang Nguyen Tuan Tu")
print("246752021610129")
print("----------------")
# =======================================================
# Bài 10: Xây dựng hàm bubblesort(list) (Sắp xếp Nổi bọt)
# =======================================================

def bubblesort(input_list):
    """
    Sắp xếp danh sách bằng thuật toán Sắp xếp Nổi bọt.
    """
    list_counts = len(input_list)
    
    # Lặp qua tất cả các phần tử của mảng
    for i in range(list_counts - 1): 
        swapped = False # Cờ tối ưu hóa
        
        # Vòng lặp bên trong: So sánh các cặp phần tử liền kề
        for j in range(list_counts - 1 - i): 
            
            # Nếu phần tử hiện tại lớn hơn phần tử tiếp theo, thực hiện hoán đổi
            if input_list[j] > input_list[j + 1]:
                
                # Thực hiện hoán đổi vị trí
                input_list[j], input_list[j + 1] = input_list[j + 1], input_list[j]
                
                swapped = True
        
        # Nếu không có hoán đổi nào xảy ra, thoát vòng lặp (tối ưu hóa)
        if not swapped:
            break
            
    return input_list

# --- CHẠY THỬ NGHIỆM BÀI 10 ---
print("\n--- Bài 10: Sắp xếp Nổi bọt (Bubble Sort) ---")

sample_data = [14, 46, 27, 57, 41, 45, 21, 70] # Sample Data
print("Danh sách gốc:", sample_data)

sorted_list = bubblesort(sample_data)
print("Danh sách sau khi sắp xếp:", sorted_list) 
# Expected Result: [14, 21, 27, 41, 45, 46, 57, 70]
