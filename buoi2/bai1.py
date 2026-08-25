age = int(input("Nhập tuổi của bạn: "))

if(age < 0):
    print("Dữ liệu không hợp lệ")
elif(age >= 18):
    print("Đủ tuổi")
else:
    print("Chưa đủ tuổi")