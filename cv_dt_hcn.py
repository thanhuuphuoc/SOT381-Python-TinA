
w = 0
h = 0
while w == 0:
    ngan = float(input("Nhap chieu rong hcn: "))
    if ngan >= 0:
        w += 1

while h == 0:
    dai = float(input("Nhap chieu dai hcn: "))
    if dai <= 100 and dai >= 0:
        h += 1

cv = 2 * (ngan + dai)
dt = ngan * dai
round(cv, 2)
round(dt, 2)
print(f"Chu vi hinh chu nhat la {cv}")
print(f"Dien tich hinh chu nhat la {dt}")


