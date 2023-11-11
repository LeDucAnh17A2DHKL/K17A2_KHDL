# Nhập số tiền muốn đổi
so_tien = int(input("Số tiền muốn đổi: "))

# Định nghĩa các mệnh giá tiền
menh_gia = [500000, 200000, 100000, 50000]

# Tính số tờ tiền cho mỗi mệnh giá
for mg in menh_gia:
    so_to = so_tien // mg
    so_tien %= mg
    print("Số tờ", mg, ":", so_to)
