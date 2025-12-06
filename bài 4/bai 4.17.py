print("Hoang Nguyen Tuan Tu")
print("245752021610129")
print("--------------------")
## Bài 17: Nhập n, in ra các số nguyên nhỏ hơn n (diễn giải đơn giản)
print("\n### Bài 17: Nhập n, in ra các số nguyên dương nhỏ hơn n ###")

try:
    n = int(input("17. Nhập số nguyên n: "))
    
    print(f"Các số nguyên dương nhỏ hơn {n}:")
    # Lặp từ 1 đến n-1
    for i in range(1, n):
        print(i, end=' ')
    print()
        
except ValueError:
    print("Giá trị nhập vào không phải là số nguyên hợp lệ.")
