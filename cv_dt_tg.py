while True:
    a = float(input("Nhap canh dau tien: "))
    if a > 0:
        break
#-------------

while True:
    b = float(input("Nhap canh thu hai: "))
    if b > 0:
        break
#--------------

while True:
    c = float(input("Nhap can thu ba: "))
    if c > 0:
        break
#---------------

cv = a + b + c
ncv = cv * 0.5
dt = (ncv * (ncv - a) * (ncv - b) * (ncv - c)) ** 0.5

print(f"Chu vi tam giac la {cv}")
print(f"Dien tich tam giac la {dt}")