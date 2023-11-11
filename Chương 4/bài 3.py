m = int(input("Nhập một số tự nhiên m: "))
n = int(input("Nhập một số tự nhiên n (n > m): "))
for i in range(1, n+1):
    if i % m == 0:
        print(i)