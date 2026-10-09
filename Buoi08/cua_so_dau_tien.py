import tkinter as tk

# Bài 1.1: Cửa sổ cơ bản
cua_so = tk.Tk()
cua_so.title("Cua so Tkinter dau tien")
cua_so.geometry("480x300") # rộng x cao

# Bài 1.2: Tùy chỉnh không cho resize và thêm nội dung
cua_so.resizable(True, False) # Không cho kéo rộng/cao
nhan = tk.Label(cua_so, text="Xin chao Tkinter!", font=("Arial", 16))
nhan.pack(pady=20)

cua_so.mainloop()


import tkinter as tk

cua_so = tk.Tk()
cua_so.title("Vi du Frame")
cua_so.geometry("480x300")

khung_tren = tk.Frame(cua_so, bg="lightblue", height=100)
khung_tren.pack(fill="x")

khung_duoi = tk.Frame(cua_so, bg="lightyellow")
khung_duoi.pack(fill="both", expand=True)

tk.Label(khung_tren, text="Khu vuc tieu de", bg="lightblue").pack(pady=10)
tk.Label(khung_duoi, text="Khu vuc noi dung", bg="lightyellow").pack(pady=10)

cua_so.mainloop()