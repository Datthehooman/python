n = float(input("Nhập điểm từ 0 đến 10: "))

if(n < 0 or n > 10):
    print("Điểm không hợp lệ")
elif(n >= 9):
    print("Xuất sắc")
elif(n >= 8):
    print("Giỏi")
elif(n >= 6.5):
    print("Khá")
elif(n >= 5):
    print("Trung bình")
else:
    print("Yếu")