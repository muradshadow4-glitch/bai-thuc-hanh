print("Hoang Nguyen Tuan Tu")
print("245752021610129")
print("--------------------")
## Bài 18: Tạo list gồm các số fibonacci
print("\n### Bài 18: Tạo list Fibonacci và in ra phần tử ###")

try:
    n = int(input("18. Nhập n (số lượng phần tử Fibonacci): "))
    m = int(input("18. Nhập m (vị trí phần tử muốn in ra): "))
    
    fib_list = []
    a, b = 0, 1
    
    # Tạo list Fibonacci có n phần tử
    while len(fib_list) < n:
        fib_list.append(a)
        a, b = b, a + b
    
    print(f"List Fibonacci có {n} phần tử: {fib_list}")
    
    # In ra số thứ m (lưu ý index bắt đầu từ 0)
    if 1 <= m <= n:
        print(f"Số Fibonacci thứ {m} (index {m-1}) là: {fib_list[m-1]}")
    else:
        print(f"Vị trí m={m} nằm ngoài phạm vi list.")
        
except ValueError:
    print("Giá trị nhập vào không phải là số nguyên hợp lệ.")
