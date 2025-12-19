n = int(input("Nhap so ban muon kiem tra: "))
uoc_so = 0
for i in range (2, n):
    if n % i == 0: 
        uoc_so += 1
if uoc_so == 0:
    print (f"{n} la so nguyen to")
else: 
    print (f"{n} khong la so nguyen to")