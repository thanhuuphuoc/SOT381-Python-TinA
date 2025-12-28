dsso = list(input("Nhap danh sach so muon so sanh: ").split())
so_lon_nhat = float(dsso[1])
so_nho_nhat = float(dsso[1])
for i in dsso:
    if so_lon_nhat < float(i):
        so_lon_nhat = float(i)
    else:
        so_nho_nhat = float (i)

print(f"So lon nhat la {so_lon_nhat}")
print(f"So nho nhat la {so_nho_nhat}")