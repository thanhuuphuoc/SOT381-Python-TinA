danhsach = list(map(int, input("Nhap danh sach so ban dau: ").split()))
so = int(input("Nhap so ma ban muon tra cuu: "))
if so in danhsach:
    vi_tri = danhsach.index(so)
    print(f"So do o vi tri {vi_tri}")
else:
    print("Khong ton tai so do")