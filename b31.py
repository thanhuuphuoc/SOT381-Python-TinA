n = int(input("Nhap gioi han muon tinh: "))
x = int(input("Nhap so muon tinh: "))
tong1 = 0
tong2 = 1
for i in range (1, n + 1):
    tong1 = (tong1 + x) ** 0.5
    tong2 = tong2 + ((x**i)/(i+1))
print(tong1)
print(tong2)

