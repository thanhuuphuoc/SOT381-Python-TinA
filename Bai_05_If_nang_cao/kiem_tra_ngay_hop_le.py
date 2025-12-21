ngay = int(input("Nhap so ngay:" ))
thang = int(input("Nhap so thang: "))
nam = int(input("Nhap so nam: "))
thang_31 = [1, 3, 5, 7, 8, 10, 12]
thang_30 = [2, 4, 6, 9, 11]
if thang in thang_31:
    if ngay > 0 and ngay <= 31:
        print("Day la ngay hop le")
    else:
        print("Day khong la ngay hop le")
elif thang in thang_30:
    if thang != 2:
        if ngay > 0 and ngay <= 30:
            print ("Day la ngay hop le")
        else:
            print ("Day khong la hop le")
    else:
        if nam % 4 == 0 or nam % 400 == 0:
            if nam % 100 == 0:
                if ngay > 0 and ngay <= 29:
                    print("Day la ngay hop le")
                else:
                    print("Day khong la ngay hop le")
            else:
                if ngay > 0 and ngay <= 28:
                    print("Day la ngay hop le")
                else:
                    print("Day khong la ngay hop le")
        else:
            if ngay > 0 and ngay <= 29:
                print("Day la ngay hop le")
            else:
                print("Day khong la ngay hop le")
else:
    print("Day khong la ngay hop le")



