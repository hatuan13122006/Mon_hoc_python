diem_so = [8.5, 7.0, 9.2, 6.5, 5.5]

print(diem_so[0])    # Phần tử đầu tiên -> Output: 8.5
print(diem_so[-1])   # Phần tử cuối cùng -> Output: 5.5
print(diem_so[1:4])  # Cắt từ vị trí 1 đến trước 4 -> Output: [7.0, 9.2, 6.5]
print(diem_so[::2])  # Lấy cách 1 phần tử (step = 2) -> Output: [8.5, 9.2, 5.5]
print(diem_so[::-1]) # Đảo ngược danh sách -> Output: [5.5, 6.5, 9.2, 7.0, 8.5]


ten_sv = ["An", "Binh", "Chi"]
ten_sv.append("Dung")       # Thêm vào cuối -> ['An', 'Binh', 'Chi', 'Dung']
ten_sv.insert(1, "Em")      # Chèn vào vị trí 1 -> ['An', 'Em', 'Binh', 'Chi', 'Dung']
print(ten_sv)
ten_sv.remove("Chi")        # Xóa giá trị "Chi"
pop_ra = ten_sv.pop()       # Xóa và lấy ra phần tử cuối ("Dung")
print(ten_sv, "- da xoa:", pop_ra) # Output: ['An', 'Em', 'Binh'] - da xoa: Dung
ten_sv.sort()               # Sắp xếp tăng dần theo bảng chữ cái -> ['An', 'Binh', 'Em']
print(ten_sv)
ten_sv.reverse()            # Đảo ngược thứ tự hiện tại -> ['Em', 'Binh', 'An']
print(ten_sv)
ten_sv.extend(["Giang", "Hoa"]) # Nối thêm một list khác vào -> ['Em', 'Binh', 'An', 'Giang', 'Hoa']
print(ten_sv)


diem_so = [8.5, 7.0, 9.2, 6.5, 5.5]
tong = 0

for diem in diem_so:
    print(diem)
    tong = tong + diem

print("Tong diem:", tong)
print("Diem trung binh:", round(tong / len(diem_so), 2))


ma_tran = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# In ra theo từng hàng
for hang in ma_tran:
    print(hang)

# In ra từng phần tử, duyệt theo hàng rồi theo cột
for hang in ma_tran:
    for phan_tu in hang:
        print(phan_tu, end=" ")
    print()


    tong_ma_tran = 0

for hang in ma_tran:
    for phan_tu in hang:
        tong_ma_tran += phan_tu

print("Tong tat ca phan tu trong ma tran:", tong_ma_tran)


# Bài tập 3.1 - Lọc số chẵn/lẻ
day_so = list(range(1, 21))  # dãy số từ 1 đến 20

so_chan = [x for x in day_so if x % 2 == 0]
so_le = [x for x in day_so if x % 2 != 0]

print("So chan:", so_chan)
print("So le:", so_le)

# Bài tập 3.2 - Biến đổi phần tử
diem_so = [8.5, 7.0, 9.2, 6.5, 5.5]
diem_cong = [round(diem + 0.5, 2) for diem in diem_so]
print("Diem cong:", diem_cong)