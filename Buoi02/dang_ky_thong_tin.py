# 1. Nhập thông tin đầu vào
ho_ten = input("Nhap ho ten: ")
sdt = input("Nhap so dien thoai: ")
email = input("Nhap email: ")

# 2. Xử lý & kiểm tra dữ liệu
ho_ten_chuan = " ".join(ho_ten.split()).title()  # Loại bỏ khoảng trắng thừa & viết hoa chữ cái đầu
sdt_hop_le = len(sdt) == 10                       # Kiểm tra độ dài có đúng 10 ký tự không
email_hop_le = "@" in email                       # Kiểm tra sự tồn tại của ký tự '@'

# 3. Xuất kết quả ra màn hình
print(f"Ho ten (da chuan hoa): {ho_ten_chuan}")
print(f"So dien thoai hop le (du 10 ky tu)? {sdt_hop_le}")
print(f"Email hop le (co ky tu @)? {email_hop_le}")