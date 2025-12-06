print("Hoang Nguyen Tuan Tu")
print("245752021610129")
print("--------------------")
## Bài 19: Tạo ra tuple gồm các số nguyên tố
print("\n### Bài 19: Tạo tuple các số nguyên tố (giới hạn 100) ###")

def is_prime(num):
    """Kiểm tra một số có phải là số nguyên tố không."""
    if num <= 1:
        return False
    # Kiểm tra từ 2 đến căn bậc hai của num
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

gioi_han = 100 # Giới hạn 1 triệu quá lớn để chạy và in ra
prime_list = []

for num in range(2, gioi_han):
    if is_prime(num):
        prime_list.append(num)

prime_tuple = tuple(prime_list) # Chuyển list thành tuple

print(f"Tuple các số nguyên tố nhỏ hơn {gioi_han}:")
print(prime_tuple)
