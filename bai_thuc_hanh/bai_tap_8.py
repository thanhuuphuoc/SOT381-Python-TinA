n = int(input("Nhập số nguyên dương n: "))
while n == 0:
    n = int(input("Nhập lại số nguyên dương n: "))
tong_S1 = 0
tong_S2 = 10
for i in range(n):
    tong_S1 += 1/(i+1)
for k in range(1, n+1):
    tong_S2 += (k-1)/(k)
print (tong_S1)
print (tong_S2)