x = int(input("Nhap toa do x cua diem: "))
y = int(input("Nhap toa do y cua diem: "))
if x == 0 and y == 0:
    print("Diem nam tren goc toa do O(0,0)")
elif x == 0 or y == 0:
    if x == 0:
        print("Diem nam tren truc Ox")
    else:
        print("Diem nam tren truc Oy")
else:
    if x > 0 and y > 0:
        print("Diem nam tren goc phan tu I")
    elif x < 0 and y > 0:
        print("Diem nam tren goc phan tu II")
    elif x < 0 and y < 0:
        print("Diem nam tren goc phan tu III")
    else: 
        print("Diem nam tren goc phan tu IV")  

