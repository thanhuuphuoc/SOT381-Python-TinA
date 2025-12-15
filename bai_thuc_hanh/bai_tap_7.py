n = int(input("Nhập số nguyên dương n: "))
# nhập giá trị n----------------------------------------------
giai_thua = 1
while n <= 0 or n >= 10:
    n = int(input("Nhập lại số nguyên dương n: "))
#yêu cầu người dùng nhập chính xác n------------------------------
for x in range (n):
    giai_thua *= (x + 1)
#tính kết quả----------------------------------------------- 
print(giai_thua)