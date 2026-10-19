chuoi_so = input("Nhập danh sách số nguyên, cách nhau bởi dấu phẩy: ")
so_nguyen = [int(phan_tu.strip()) for phan_tu in chuoi_so.split(",") if phan_tu.strip()]

so_chan = []
so_le = []

for so in so_nguyen:
    if so % 2 == 0:
        so_chan.append(so)
    else:
        so_le.append(so)

print(f"Số chẵn: {so_chan}")
print(f"Số lẻ: {so_le}")
