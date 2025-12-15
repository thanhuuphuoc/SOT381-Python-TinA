n = int(input("Nhập giới hạn dãy số: "))
for x in range(n+1):
    if x % 2 == 0 and x % 3 == 0:
        tong_cac_so += x
print("Tổng các số chia hết cho 2 và 3 trong dãy số là: ", tong_cac_so)