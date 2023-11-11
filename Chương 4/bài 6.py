import numbers as np

# Hệ số của hệ phương trình
a = np.array([[3, 2], [1, 2]])
b = np.array([18, 14])

# Giải hệ phương trình
x = np.linalg.solve(a, b)

print("Nghiệm của hệ phương trình là: ", x)
# tính số ngày của tháng của năm nào đó 
import calendar

year = 2023
month = 2

# Tính số ngày trong tháng
num_days = calendar.monthrange(year, month)[1]

print("Số ngày trong tháng là: ", num_days)
#thuật toán tìm ước số chung lớn nhất
import math

num1 = 60
num2 = 48

# Tìm ước chung lớn nhất
gcd = math.gcd(num1, num2)

print("Ước chung lớn nhất của", num1, "và", num2, "là:", gcd)