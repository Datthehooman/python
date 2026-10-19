chuoi_so = input("Nhập danh sách số nguyên, cách nhau bởi dấu phẩy: ")
nguong = int(input("Nhập ngưỡng: "))
so_nguyen = [int(phan_tu.strip()) for phan_tu in chuoi_so.split(",") if phan_tu.strip()]

so_dat_nguong = []
for so in so_nguyen:
    if so >= nguong:
        so_dat_nguong.append(so)

print(f"Các số lớn hơn hoặc bằng {nguong}: {so_dat_nguong}")
