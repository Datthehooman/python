ho_ten = input("Nhập họ tên: ")
tuoi = int(input("Nhập tuổi: "))
lop = input("Nhập lớp: ")
dia_chi = input("Nhập địa chỉ: ")

hoc_sinh = {
	"Họ tên": ho_ten,
	"Tuổi": tuoi,
	"Lớp": lop,
	"Địa chỉ": dia_chi,
}

print("\nThông tin cá nhân của học sinh:")
for thong_tin, gia_tri in hoc_sinh.items():
	print(f"{thong_tin}: {gia_tri}")
