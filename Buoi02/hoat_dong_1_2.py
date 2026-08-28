ho_ten = input("Nhap ho ten: ")
nam_sinh = int(input("Nhap nam sinh: "))
diem_tb = float(input("Nhap diem trung binh: "))


print("Python", "la", "ngon", "ngu", "lap trinh", sep="-")
print("Dong 1", end=" | ")
print("Dong 2")


print("Python", "la", "ngon", "ngu", "lap trinh", sep=",")
print("Dong 1", end=" | ")
print("Dong 2")


print("Python", "la", "ngon", "ngu", "lap trinh", sep="'")
print("Dong 1", end=" | ")
print("Dong 2")


print("Python", "la", "ngon", "ngu", "lap trinh", sep="\n")
print("Dong 1", end=" | ")
print("Dong 2")


ho_ten = "tuan"
nam_sinh = 2006
diem_tb = 8.5

# Cách 1: f-string
print(f"Ho ten: {ho_ten} - Nam sinh: {nam_sinh} - DTB: {diem_tb:.2f}")

# Cách 2: str.format()
print(
    "Ho ten: {} - Nam sinh: {} - DTB: {:.2f}".format(
        ho_ten, nam_sinh, diem_tb
    )
)

# Cách 3: Toán tử %
print("Ho ten: %s - Nam sinh: %d - DTB: %.2f" % (ho_ten, nam_sinh, diem_tb))


# Chu thich mot dong: khai bao thong tin sinh vien
"""
Chu thich/docstring nhieu dong:
Chuong trinh quan ly diem sinh vien - Buoi 2
"""
ho_ten = "Tran Thi B" # bien luu ho ten


s1 = 'Xin chao'
s2 = "Ban co khoe khong?"
s3 = '''Day la
mot chuoi
nhieu dong'''
s4 = "Duong dan: C:\\Python\\data"
s5 = r"Duong dan raw: C:\Python\data"
s6 = "Toi ten la \"Nam\", con ban ten gi?"
print(s1); print(s2); print(s3); print(s4); print(s5); print(s6)


so_nguyen = 15
so_thuc = 4.2
so_phuc = 3 + 4j
print(type(so_nguyen), type(so_thuc), type(so_phuc))
print(float(so_nguyen)) # ep int -> float
print(int(so_thuc)) # ep float -> int (cat phan thap phan)


a = -7
b = 2.6789
c, d = 17, 5
print(abs(a)) # gia tri tuyet doi
print(round(b)) # lam tron
print(round(b, 2)) # lam tron 2 chu so thap phan
print(pow(c, 2)) # c mu 2
print(divmod(c, d)) # tra ve (thuong, du) dang tuple


import math
a, b, c = 1, -3, 2
delta = b ** 2 - 4 * a * c
x1 = (-b + math.sqrt(delta)) / (2 * a)
x2 = (-b - math.sqrt(delta)) / (2 * a)
print(f"Delta = {delta}")
print(f"Nghiem x1 = {round(x1, 2)}, x2 = {round(x2, 2)}")
