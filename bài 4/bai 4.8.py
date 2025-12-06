print("Hoang Nguyen Tuan Tu")
print("245752021610129")
print("--------------------")
print("--- Bài 8: Tìm từ dài nhất trong dãy ---")
ds_tu_bai8 = input("# Nhập dãy các từ (cách nhau bởi khoảng trắng): ").split()

if not ds_tu_bai8:
    print("Không có từ nào được nhập.")
else:
    # Python có hàm max() với tham số key để tìm phần tử dựa trên một tiêu chí
    # key=len sẽ tìm phần tử (từ) có độ dài (len) lớn nhất.
    tu_dai_nhat = max(ds_tu_bai8, key=len)
    do_dai_max = len(tu_dai_nhat)
            
    print(f"Từ dài nhất: **{tu_dai_nhat}**")
    print(f"Độ dài: **{do_dai_max}**")
