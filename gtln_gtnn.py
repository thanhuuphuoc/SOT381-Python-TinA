dsso = list(input("Nhap danh sach so muon tinh: ").split())
gtln = int(dsso[0])
gtnn = int(dsso[0])
#-----------
for i in dsso:
    if gtln > int(i):
        gtln = int(i)
    else:
        gtnn = int(i)
print(f"Gia tri lon nhat la {gtln}")
print(f"Gia tri nho nhat la {gtnn}")