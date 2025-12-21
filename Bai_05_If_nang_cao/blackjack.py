n = list(map(str,input("Nhap cac la bai: ").split()))
JQK = ["J", "Q", "K"]
A = ["A"]
diem_so = 0
for i in n:
    if "0" < i < "9":
        diem_so += int(i)
    if i in JQK:
        diem_so += 10
    if i in A:
        diem_so += 11
if diem_so > 21:
    for i in n:
        if i in A:
            diem_so -= 10
print("Diem cua ban la", diem_so)