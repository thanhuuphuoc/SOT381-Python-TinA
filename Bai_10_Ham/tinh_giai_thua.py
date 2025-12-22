
def giai_thua(so):
    tong = 1
    for i in range (1, so + 1):
        tong *= i
    return tong
so = int(input("Nhap so nguyen muon tinh giai thua: "))
print("Ket qua la:", giai_thua(so))