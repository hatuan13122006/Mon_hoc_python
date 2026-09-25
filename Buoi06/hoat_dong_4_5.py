# Hoạt động 4: Phạm vi biến – local, global, từ khóa global[cite: 8]

so_luot_truy_cap = 0  # bien global[cite: 8]

def tang_luot_truy_cap():
    global so_luot_truy_cap  # Khai báo sử dụng biến global[cite: 8]
    so_luot_truy_cap += 1[cite: 8]

def vi_du_bien_local():
    so_luot_truy_cap = 100  # Biến local trùng tên[cite: 8]
    print("Ben trong ham, bien local =", so_luot_truy_cap)[cite: 8]


# --- CHẠY THỬ CHƯƠNG TRÌNH ---
if __name__ == "__main__":
    print("=== HOẠT ĐỘNG 4 ===")
    tang_luot_truy_cap()[cite: 8]
    tang_luot_truy_cap()[cite: 8]
    print("So luot truy cap (global):", so_luot_truy_cap)[cite: 8]

    vi_du_bien_local()[cite: 8]
    print("Sau khi goi ham, bien global van la:", so_luot_truy_cap)[cite: 8]


# Hoạt động 5: Hàm lambda kết hợp map(), filter(), sorted()

danh_sach_so = [1, 2, 3, 4, 5]

# Bài tập 5.1: map()
binh_phuong = list(map(lambda x: x ** 2, danh_sach_so))

# Bài tập 5.2: filter()
so_chan = list(filter(lambda x: x % 2 == 0, danh_sach_so))

# Bài tập 5.3: sorted() với danh sách sinh viên
danh_sach_sv = [
    {"ten": "An", "diem": 8.5},
    {"ten": "Binh", "diem": 7.0},
    {"ten": "Chi", "diem": 9.2},
]

sap_xep_theo_diem = sorted(danh_sach_sv, key=lambda sv: sv["diem"])
sap_xep_giam_dan = sorted(danh_sach_sv, key=lambda sv: sv["diem"], reverse=True)


# --- CHẠY THỬ CHƯƠNG TRÌNH ---
if __name__ == "__main__":
    print("=== HOẠT ĐỘNG 5 ===")
    print("Binh phuong:", binh_phuong)
    print("So chan:", so_chan)
    
    print("\n--- Sap xep tang dan theo diem ---")
    for sv in sap_xep_theo_diem:
        print(sv["ten"], "-", sv["diem"])

    print("\n--- Giam dan ---")
    for sv in sap_xep_giam_dan:
        print(sv["ten"], "-", sv["diem"])

