# Hoạt động 4: Phạm vi biến – local, global, từ khóa global

so_luot_truy_cap = 0  # bien global


def tang_luot_truy_cap():
    global so_luot_truy_cap
    so_luot_truy_cap += 1


def vi_du_bien_local():
    so_luot_truy_cap = 100  # bien LOCAL, khac voi bien global cung ten
    print("Ben trong ham, bien local =", so_luot_truy_cap)


# Goi thu
tang_luot_truy_cap()
tang_luot_truy_cap()
print("So luot truy cap (global):", so_luot_truy_cap)

vi_du_bien_local()
print("Sau khi goi ham, bien global van la:", so_luot_truy_cap)


# Hoạt động 5: Hàm lambda kết hợp map(), filter(), sorted()

danh_sach_so = [1, 2, 3, 4, 5]

# Bài tập 5.1: Binh phuong cac so
binh_phuong = list(map(lambda x: x**2, danh_sach_so))
print("Binh phuong:", binh_phuong)

# Bài tập 5.2: Loc cac so chan
so_chan = list(filter(lambda x: x % 2 == 0, danh_sach_so))
print("So chan:", so_chan)

# Bài tập 5.3: Sap xep danh sach sinh vien theo diem
danh_sach_sv = [
    {"ten": "An", "diem": 8.5},
    {"ten": "Binh", "diem": 7.0},
    {"ten": "Chi", "diem": 9.2},
]

# Sap xep tang dan theo diem
sap_xep_theo_diem = sorted(danh_sach_sv, key=lambda sv: sv["diem"])

# Sap xep giam dan theo diem
sap_xep_giam_dan = sorted(danh_sach_sv, key=lambda sv: sv["diem"], reverse=True)

print("--- Tang dan theo diem ---")
for sv in sap_xep_theo_diem:
    print(sv["ten"], "-", sv["diem"])

print("--- Giam dan ---")
for sv in sap_xep_giam_dan:
    print(sv["ten"], "-", sv["diem"])

