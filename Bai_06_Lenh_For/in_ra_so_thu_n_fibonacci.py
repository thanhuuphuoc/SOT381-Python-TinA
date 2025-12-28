n = int(input("Nhap vi tri ban muon tra cuu trong day Fibonacci: "))
k = [1, 1]
while len(k) < n:
    k.append(k[-1] + k[-2])
print(k[n - 1])