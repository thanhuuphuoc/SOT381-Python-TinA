def tinh_tong(*cac_so):
    """Tính tổng nhiều số"""
    tong = 0
    for so in cac_so:
        tong += so
    return tong

print(tinh_tong(1, 2, 3))        # 6
print(tinh_tong(1, 2, 3, 4, 5))  # 15