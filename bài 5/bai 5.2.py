print("Hoang Nguyen Tuan Tu")
print("245752021610129")
print("--------------------")
import datetime as dt

print("Hoang Nguyen Tuan Tu")
print("246752021610129")
print("----------------")

# 1. Phân tích cú pháp chuỗi ngày/giờ
# CHUỖI: '2008-10-12T14:45:52', Định dạng: '%Y-%m-%dT%H:%M:%S'
# SỬA LỖI: Bỏ format=
t1 = dt.datetime.strptime('2008-10-12T14:45:52', '%Y-%m-%dT%H:%M:%S')

# 2. Xuất các phần của đối tượng datetime (t1) và in ra
print('Day ' + str(t1.day))
print('Month ' + str(t1.month))
print('Minute ' + str(t1.minute))
print('Second ' + str(t1.second))

# 3. Tính toán sự khác biệt giữa hai ngày
# Định nghĩa ngày/giờ hôm nay (thời điểm chạy code)
t2 = dt.datetime.now()

# Tính toán sự khác biệt (sẽ là một đối tượng timedelta)
diff = t2 - t1

# In ra số ngày khác biệt. .days là thuộc tính của đối tượng timedelta
print('How many days difference? ' + str(diff.days))
