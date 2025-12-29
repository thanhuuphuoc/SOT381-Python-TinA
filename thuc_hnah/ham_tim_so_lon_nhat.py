def so_lon_nhat(a):
    gtln = int(a[0])
    for i in a:
        if gtln < int(i):
            gtln = int(i)
    return gtln
a = list(input("Nhap cac so muon tinh: ").split())
print("So lon nhat la: ", so_lon_nhat(a))