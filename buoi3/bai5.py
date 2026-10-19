chuoi_so = input("Nhập danh sách số nguyên, cách nhau bởi dấu phẩy: ")
so_can_tim = int(input("Nhập số nguyên cần tìm: "))
so_nguyen = [int(phan_tu.strip()) for phan_tu in chuoi_so.split(",") if phan_tu.strip()]

vi_tri_xuat_hien = []
for vi_tri in range(len(so_nguyen)):
    if so_nguyen[vi_tri] == so_can_tim:
        vi_tri_xuat_hien.append(vi_tri + 1)

if vi_tri_xuat_hien:
    print(f"Số {so_can_tim} xuất hiện tại các vị trí: {vi_tri_xuat_hien}")
else:
    print(f"Không tìm thấy số {so_can_tim} trong danh sách.")
