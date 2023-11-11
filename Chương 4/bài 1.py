number = input("nhập một số nguyên:")
if number.isdigit():
    number = int(number)
    square = number** 2
    print("bình phương của",number,"là",square)
else:
    print("số bạn nhập không hợp lệ!")