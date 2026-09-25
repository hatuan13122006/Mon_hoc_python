def uscln(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def bscnn(a, b):
    return a * b // uscln(a, b)

def kiem_tra_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def kiem_tra_so_hoan_thien(n):
    tong_uoc = 0
    for i in range(1, n):
        if n % i == 0:
            tong_uoc += i
    return tong_uoc == n

# --- Kiểm thử với ít nhất 3 bộ dữ liệu khác nhau ---
# 1. Hàm USCLN
print("--- USCLN ---")
print(uscln(24, 36))  # Kết quả: 12
print(uscln(17, 13))  # Kết quả: 1
print(uscln(100, 75)) # Kết quả: 25

# 2. Hàm BSCNN
print("\n--- BSCNN ---")
print(bscnn(4, 6))    # Kết quả: 12
print(bscnn(15, 20))  # Kết quả: 60
print(bscnn(7, 5))    # Kết quả: 35

# 3. Hàm kiểm tra số nguyên tố
print("\n--- Kiểm tra số nguyên tố ---")
print(kiem_tra_nguyen_to(29)) # Kết quả: True
print(kiem_tra_nguyen_to(1))  # Kết quả: False
print(kiem_tra_nguyen_to(10)) # Kết quả: False

# 4. Hàm kiểm tra số hoàn thiện
print("\n--- Kiểm tra số hoàn thiện ---")
print(kiem_tra_so_hoan_thien(28)) # Kết quả: True (28 = 1 + 2 + 4 + 7 + 14)
print(kiem_tra_so_hoan_thien(6))  # Kết quả: True
print(kiem_tra_so_hoan_thien(12)) # Kết quả: False


def in_loi_chao(ten):
    print(f"Xin chao, {ten}!")
    return  # Hàm không trả về giá trị (trả về None)

def chia_lay_thuong_du(a, b):
    return a // b, a % b  # Trả về nhiều giá trị qua tuple

# Gọi thử nghiệm
in_loi_chao("An")

thuong, du = chia_lay_thuong_du(17, 5)
print(f"Thuong: {thuong}, du: {du}")


def gioi_thieu(ten, tuoi=18, lop="Chua ro"):
    print(f"Ten: {ten} - Tuoi: {tuoi} - Lop: {lop}")

# Chạy thử
gioi_thieu("An")                                   # Dùng hết giá trị mặc định
gioi_thieu("Binh", 20)                             # Ghi đè tuổi
gioi_thieu("Chi", lop="CNTT01")                    # Dùng tham số từ khóa, bỏ qua tuổi
gioi_thieu(ten="Dung", lop="CNTT02", tuoi=19)      # Thứ tự tham số từ khóa có thể đảo lộn


def tinh_tong(*args):
    tong = 0
    for so in args:
        tong += so
    return tong

print(tinh_tong(1, 2, 3))             # Kết quả: 6
print(tinh_tong(5, 10, 15, 20, 25))   # Kết quả: 75
print(tinh_tong())                    # Không truyền số nào -> Trả về 0


def in_thong_tin(ho_ten, tuoi, **kwargs):
    print(f"Ho ten: {ho_ten} - Tuoi: {tuoi}")
    for khoa, gia_tri in kwargs.items():
        print(f"  {khoa}: {gia_tri}")

# Gọi thử nghiệm
in_thong_tin("Nguyen Van A", 20, lop="CNTT01", que_quan="Ha Noi")
in_thong_tin("Tran Thi B", 21, email="b@example.com")