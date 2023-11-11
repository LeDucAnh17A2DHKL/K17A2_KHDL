def sum_of_digits(n):
    n = abs(n)  # Trường hợp n là số nguyên âm
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total

N = int(input("Nhập một số nguyên N: "))
print("Tổng các chữ số của", N, "là:", sum_of_digits)
#chuye tu c sang f
def celsius_to_fahrenheit(celsius):
    return celsius * 9/5 + 32

celsius = float(input("Nhập nhiệt độ ở độ Celsius: "))
fahrenheit = celsius_to_fahrenheit(celsius)
print(celsius, "độ Celsius tương ứng với", fahrenheit, "độ Fahrenheit.")
# tiền lãi 
def calculate_interest(principal, rate, time):
    # Tính lãi suất theo công thức lãi suất kép
    amount = principal * (1 + rate / 100)**time
    interest = amount - principal
    return interest, amount

principal = float(input("Nhập số tiền gốc: "))
rate = float(input("Nhập lãi suất hàng năm (dưới dạng phần trăm): "))
time = float(input("Nhập thời gian gửi tiền (dưới dạng năm): "))

interest, total_amount = calculate_interest(principal, rate, time)

print("Số tiền lãi sau", time, "năm là:", interest)
print("Tổng số tiền nhận được sau", time, "năm là:", total_amount)
# tinh vaf in 
x = float(input("Nhập giá trị của x: "))

S = 1 + x + (x**3)/3 + (x**5)/5

print("Tổng của biểu thức S=1 + x + x^3/3 + x^5/5 là:", S)