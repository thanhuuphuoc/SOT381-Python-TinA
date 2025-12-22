n = int(input("Nhap gioi han day fibonacci: "))
dsfib = [1, 1]
tongfib = 0
for i in range(1, n + 1):
    dsfib.append(dsfib[i-1] + dsfib[i])
for i in dsfib:
    tongfib += i
print(f"Day fibonacci la {dsfib}")
print(f"Tong day fibonacci la {tongfib}")

