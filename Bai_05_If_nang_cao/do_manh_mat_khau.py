mk = list(input("Nhap mat khau cua ban: "))
diem = 0
chu_hoa = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
dac_biet = "!@#$%^&*()"
so_dem = "1234567890"

if len(mk) >= 8 and len(mk) < 12:
    diem += 1
elif len(mk) >= 12:
    diem += 2
else:
    diem += 0
#--------------
for i in mk:
    if i in chu_hoa:
        diem += 1
        break
#---------------
for i in mk:
    if i in so_dem:
        diem += 1
        break 
#--------------
for i in mk:
    if i in dac_biet:
        diem += 1
        break

if diem == 5:
    print("Mat khau rat manh")
elif diem >= 3:
    print("Mat khau manh")
elif diem >= 2:
    print("Mat khau trung binh")
else:
    print("Mat khau yeu")
print (len(mk))