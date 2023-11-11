def gcd(a, b):
    while(b):
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

num1 = int(input("Nhập số thứ nhất: "))
num2 = int(input("Nhập số thứ hai: "))

print("Bội chung nhỏ nhất của", num1, "và", num2, "là:", lcm(num1, num2))