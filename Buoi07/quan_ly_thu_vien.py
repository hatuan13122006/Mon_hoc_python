danh_sach_sach = [
    {"ma_sach": "S001", "ten_sach": "Lap trinh Python co ban", "tac_gia": "Nguyen Van A", "trang_thai": "Co san", "nguoi_muon": ""},
    {"ma_sach": "S002", "ten_sach": "Cau truc du lieu va gia thuat", "tac_gia": "Tran Van B", "trang_thai": "Co san", "nguoi_muon": ""},
    {"ma_sach": "S003", "ten_sach": "Co so du lieu SQL", "tac_gia": "Le Thi C", "trang_thai": "Co san", "nguoi_muon": ""},
]

def hien_thi_sach():
    print("\n" + "="*70)
    print(f"{'Ma sach':<10}{'Ten sach':<30}{'Tac gia':<18}{'Trang thai':<12}")
    print("-"*70)
    for s in danh_sach_sach:
        print(f"{s['ma_sach']:<10}{s['ten_sach']:<30}{s['tac_gia']:<18}{s['trang_thai']:<12}")
    print("-"*70)

def tim_sach(ma_sach):
    for s in danh_sach_sach:
        if s["ma_sach"] == ma_sach:
            return s
    return None

def muon_sach():
    ma_sach = input("Nhap ma sach muon muon: ").strip().upper()
    sach = tim_sach(ma_sach)
    if not sach:
        print("-> Khong tim thay ma sach nay!")
        return
    if sach["trang_thai"] == "Da muon":
        print(f"-> Sach {ma_sach} da duoc mượn roi!")
        return
    
    ten_nguoi = input("Nhap ten nguoi muon: ").strip().title()
    sach["trang_thai"] = "Da muon"
    sach["nguoi_muon"] = ten_nguoi
    print(f"-> Cho mượn sach '{sach['ten_sach']}' thanh cong cho {ten_nguoi}.")

def tra_sach():
    ma_sach = input("Nhap ma sach can tra: ").strip().upper()
    sach = tim_sach(ma_sach)
    if not sach:
        print("-> Khong tim thay ma sach!")
        return
    if sach["trang_thai"] == "Co san":
        print("-> Sach nay dang o thu vien, khong can tra!")
        return
    
    print(f"-> Tra sach '{sach['ten_sach']}' tu nguoi muon {sach['nguoi_muon']} thanh cong.")
    sach["trang_thai"] = "Co san"
    sach["nguoi_muon"] = ""

def main():
    while True:
        print("\n=== QUAN LY THU VIEN ===")
        print("1. Hien thi danh sach sach")
        print("2. Muon sach")
        print("3. Tra sach")
        print("0. Thoat")
        chon = input("Chon chuc nang: ").strip()
        if chon == "1":
            hien_thi_sach()
        elif chon == "2":
            muon_sach()
        elif chon == "3":
            tra_sach()
        elif chon == "0":
            print("Thoat chuong trinh!")
            break
        else:
            print("Chon sai, vui long chon lai!")

if __name__ == "__main__":
    main()
