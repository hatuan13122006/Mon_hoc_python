import tkinter as tk
from tkinter import messagebox

def bam_nut(ky_tu):
    """Hàm xử lý khi bấm các nút số hoặc phép toán"""
    hien_tai = entry_hien_thi.get()
    entry_hien_thi.delete(0, tk.END)
    entry_hien_thi.insert(0, hien_tai + str(ky_tu))

def xoa_het():
    """Xóa toàn bộ nội dung trên màn hình"""
    entry_hien_thi.delete(0, tk.END)

def tinh_ket_qua():
    """Tính toán khi bấm nút ="""
    try:
        bieu_thuc = entry_hien_thi.get()
        # Thay thế các ký hiệu cho đúng với Python nếu cần (ở đây dùng trực tiếp + - * /)
        ket_qua = eval(bieu_thuc)
        entry_hien_thi.delete(0, tk.END)
        entry_hien_thi.insert(0, str(ket_qua))
    except ZeroDivisionError:
        messagebox.showerror("Loi", "Khong the chia cho 0")
        entry_hien_thi.delete(0, tk.END)
    except Exception:
        messagebox.showerror("Loi", "Bieu thuc khong hop le")
        entry_hien_thi.delete(0, tk.END)

# --- Tạo cửa sổ chính ---
cua_so = tk.Tk()
cua_so.title("May tinh bo tui")

# ĐÃ XÓA DÒNG GEOMETRY. Cửa sổ sẽ tự động co giãn vừa vặn với các nút.
# cua_so.geometry("420x580") 
cua_so.resizable(False, False)

# --- Ô hiển thị biểu thức/kết quả ---
entry_hien_thi = tk.Entry(cua_so, width=18, font=("Arial", 24), borderwidth=5, relief="ridge", justify="right")
entry_hien_thi.grid(row=0, column=0, columnspan=4, padx=10, pady=15, ipady=15)

# --- Các nút bấm ---
cac_nut = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
]

for (text, row, col) in cac_nut:
    if text == '=':
        # Nút bằng: Màu xanh, chữ đậm
        btn = tk.Button(cua_so, text=text, width=6, height=3, font=("Arial", 18, "bold"),
                        command=tinh_ket_qua, bg="lightblue")
    else:
        # Các nút số và phép tính
        btn = tk.Button(cua_so, text=text, width=6, height=3, font=("Arial", 18),
                        command=lambda t=text: bam_nut(t))
    btn.grid(row=row, column=col, padx=5, pady=5)

# Nút xóa (C) - Đã được đảm bảo hiển thị đầy đủ
btn_xoa = tk.Button(cua_so, text="C", width=27, height=3, font=("Arial", 18, "bold"),
                    command=xoa_het, bg="lightcoral")
btn_xoa.grid(row=5, column=0, columnspan=4, padx=5, pady=10)

cua_so.mainloop()