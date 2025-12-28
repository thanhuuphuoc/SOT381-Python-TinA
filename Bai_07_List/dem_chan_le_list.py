dschanle = list(input("Nhap danh sach phan loai: ").split())
so_chan = 0
so_le = 0
for i in dschanle:
    if int(i) % 2 == 0:
        so_chan += 1
    else: 
        so_le += 1
print(f"Co {so_le} so le")
print(f"Co {so_chan} so chan")
