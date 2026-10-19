chuoi_so = input("Nhập danh sách số nguyên, cách nhau bởi dấu phẩy: ")
so_nguyen = [int(phan_tu.strip()) for phan_tu in chuoi_so.split(",") if phan_tu.strip()]

so_khac_nhau = []
for so in so_nguyen:
    if so not in so_khac_nhau:
        so_khac_nhau.append(so)

if len(so_khac_nhau) < 2:
    print("Danh sách phải có ít nhất hai số khác nhau.")
else:
    so_lon_nhat = so_khac_nhau[0]
    so_lon_thu_hai = so_khac_nhau[1]

    for so in so_khac_nhau[1:]:
        if so > so_lon_nhat:
            so_lon_thu_hai = so_lon_nhat
            so_lon_nhat = so
        elif so > so_lon_thu_hai:
            so_lon_thu_hai = so

    print(f"Số lớn thứ hai là: {so_lon_thu_hai}")
