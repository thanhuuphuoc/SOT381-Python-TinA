n = int(input("Nhập giới hạn dãy số: "))
tong = int
for x in range(n+1):
    if x % 2 == 0 and x % 3 == 0:
        tong += x
print("Tổng các số chia hết cho 2 và 3 trong dãy số là: ", tong)