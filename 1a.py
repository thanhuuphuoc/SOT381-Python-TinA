dsdiemthi = list(map(int, input("Nhap diem thi 3 mon Toan, Ly, Hoa: ").split()))
tongdiem = 0
thidau = True
hocdeu = True
for i in dsdiemthi:
    tongdiem += i
for i in dsdiemthi:
    if i < 4 or tongdiem < 15:
        thidau = False
for i in dsdiemthi:
    if i > 5:
        hocdeu = True
    else:
        hocdeu = False
        break
if thidau:
    if hocdeu:
        print("Hoc deu cac mon")
    else: 
        print("Khong hoc deu cac mon")
else:
    print("Thi hong")

