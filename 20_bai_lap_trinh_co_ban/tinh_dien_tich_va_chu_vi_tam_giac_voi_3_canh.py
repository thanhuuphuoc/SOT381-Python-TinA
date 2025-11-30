a = float(input("Nhập độ dài cạnh 1 tam giác: "))
b = float(input("Nhập độ dài cạnh 2 tam giác: "))
c = float(input("Nhập độ dài cạnh 3 tam giác: "))
p = float
p = (a + b + c)/2
print("Chu vi của tam giác là:", p * 2)
print("Diện tích của tam giác là:", (p*(p + a)*(p + b) * (p + c)) ** 0.5)