moneyMade = int(input("Nhập doanh thu thực tế: "))
baseSalary = 15000000

if(moneyMade > 100000000):
    print(f"Tăng 10% lương: {int(baseSalary * 1.1)}")
elif(moneyMade >= 80000000 and moneyMade <= 100000000):
    print(f"Giữ nguyên lương: {baseSalary}")
elif(moneyMade >= 10000000 and moneyMade < 80000000):
    print(f"Giảm 10% lương: {int(baseSalary * 0.9)}")
else:
    print("Cần xử lý theo quy định doanh nghiệp")