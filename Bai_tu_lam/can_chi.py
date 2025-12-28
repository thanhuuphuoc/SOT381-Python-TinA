nam = int(input("Nhap nam ma ban muon tim: "))
Can = ["Canh", "Tan", "Nham", "Quy", "Giap", "At", "Binh", "Dinh", "Mau", "Ky"]
Chi = ["Ty", "Suu", "Dan", "Mao", "Thin", "Ty", "Ngo", "Mui", "Than", "Dau", "Tuat", "Hoi"]
nam_can = nam % 10
nam_chi = nam % 12
print(f"Nam do la {Can[nam_can]} {Chi[nam_chi]}")