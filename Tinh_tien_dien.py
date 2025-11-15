print ("Phép tính tiền điện")
so_dien = float(input("Nhập số tiền điện: "))
tien_dien = float
if so_dien < 0:
    print("Số điện không hợp lệ.")
elif so_dien <= 50:
    tien_dien = so_dien * 1678
    print("Tiền điện phải trả là: ", tien_dien, "VND")
elif so_dien <= 100:
    tien_dien = (50*1678) + (so_dien - 50) * 1734
    print("Tiền điện phải trả là: ", tien_dien, "VND")
elif so_dien <= 200:
    tien_dien = (50*1678) + (50*1734) + (so_dien - 100) * 2014
    print("Tiền điện phải trả là: ", tien_dien, "VND")
elif so_dien <= 350:
    tien_dien = (50*1678) + (50*1734) + (100*2014) + (so_dien - 200) * 2536
    print("Tiền điện phải trả là: ", tien_dien, "VND")
else: 
    tien_dien = (50*1678) + (50*1734) + (100*2014) + (150*2536) + (so_dien - 350) * 2834
    print("Tiền điện phải trả là: ", tien_dien, "VND")