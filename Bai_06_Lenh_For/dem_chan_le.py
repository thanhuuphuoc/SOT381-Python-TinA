n = int(input("Nhap gioi han so muon tinh: "))
tong_chan = 0
tong_le = 0
#đặt biến-----------------
for i in range(n+1):
    if i % 2 == 0:
        tong_chan += 1
    else:
        tong_le += 1
print ("Tong so chan la", tong_chan)
print ("Tong so le la", tong_le)