chuoi_so = input("Nhập danh sách số nguyên, cách nhau bởi dấu phẩy: ")
so_nguyen = [int(phan_tu.strip()) for phan_tu in chuoi_so.split(",") if phan_tu.strip()]

for vi_tri in range(len(so_nguyen) - 1):
    vi_tri_nho_nhat = vi_tri

    for vi_tri_tiep_theo in range(vi_tri + 1, len(so_nguyen)):
        if so_nguyen[vi_tri_tiep_theo] < so_nguyen[vi_tri_nho_nhat]:
            vi_tri_nho_nhat = vi_tri_tiep_theo

    so_nguyen[vi_tri], so_nguyen[vi_tri_nho_nhat] = (
        so_nguyen[vi_tri_nho_nhat],
        so_nguyen[vi_tri],
    )

print(f"Danh sách sau khi sắp xếp tăng dần: {so_nguyen}")
