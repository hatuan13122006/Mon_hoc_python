# main.py - Chương trình chính import và sử dụng utils module

import utils

if __name__ == "__main__":
    print("=== HOẠT ĐỘNG 7: MINI PROJECT ===")
    print("Dao nguoc chuoi:", utils.dao_nguoc_chuoi("Python"))
    print("Kiem tra palindrome:", utils.kiem_tra_palindrome("madam"))
    print("Chuan hoa ho ten:", utils.chuan_hoa_ho_ten("   nguyen   van   an  "))
    print("USCLN(24, 36):", utils.uscln(24, 36))
    print("Kiem tra nguyen to (29):", utils.kiem_tra_nguyen_to(29))

