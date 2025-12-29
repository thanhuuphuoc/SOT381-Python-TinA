n = int(input("Nhap so luong bai hat: "))
dsbaihat = []
for i in range(1, n+1):
    baihat = input(f"Nhap bai hat yeu thich thu {i}: ")
    dsbaihat.append(baihat)
print(dsbaihat)