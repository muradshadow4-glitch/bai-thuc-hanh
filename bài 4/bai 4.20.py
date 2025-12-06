print("Hoang Nguyen Tuan Tu")
print("245752021610129")
print("--------------------")
## Bài 20: Nhập n, in ra dòng pascal
print("\n### Bài 20: In ra Tam giác Pascal ###")

try:
    n = int(input("20. Nhập n (số lượng dòng Tam giác Pascal): "))
    
    if n <= 0:
        print("Số dòng phải là số nguyên dương.")
    else:
        print(f"Tam giác Pascal {n} dòng:")
        pascal = []
        for i in range(n):
            hang_hien_tai = [1] # Phần tử đầu tiên luôn là 1
            if i > 0:
                hang_truoc = pascal[-1]
                # Tính các phần tử ở giữa: tổng hai phần tử liền kề hàng trên
                for j in range(len(hang_truoc) - 1):
                    hang_hien_tai.append(hang_truoc[j] + hang_truoc[j+1])
                hang_hien_tai.append(1) # Phần tử cuối cùng luôn là 1
            
            pascal.append(hang_hien_tai)
            # In hàng hiện tại với khoảng cách phù hợp
            print(' '.join(map(str, hang_hien_tai)).center(n * 4))

except ValueError:
    print("Giá trị nhập vào không phải là số nguyên hợp lệ.")
