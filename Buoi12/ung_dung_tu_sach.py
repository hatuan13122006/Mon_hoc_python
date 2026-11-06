import sqlite3
import tkinter as tk
from tkinter import messagebox, ttk

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

import csdl_sach as db


class UngDungTuSach(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Quản lý Tủ sách cá nhân")
        self.geometry("900x600")
        self.minsize(760, 500)

        try:
            db.tao_bang_neu_chua_co()
        except sqlite3.Error as loi:
            messagebox.showerror(
                "Lỗi cơ sở dữ liệu",
                f"Không thể khởi tạo cơ sở dữ liệu:\n{loi}",
                parent=self,
            )
            self.destroy()
            raise

        self._tao_giao_dien()
        self.tai_lai_danh_sach_sach()

    def _tao_giao_dien(self):
        khung_nhap = ttk.LabelFrame(self, text="Thêm sách mới", padding=12)
        khung_nhap.pack(fill="x", padx=16, pady=(16, 10))
        khung_nhap.columnconfigure(1, weight=1)
        khung_nhap.columnconfigure(3, weight=1)

        ttk.Label(khung_nhap, text="Tên sách:").grid(
            row=0, column=0, padx=(0, 8), pady=6, sticky="w"
        )
        self.o_nhap_ten_sach = ttk.Entry(khung_nhap)
        self.o_nhap_ten_sach.grid(
            row=0, column=1, padx=(0, 18), pady=6, sticky="ew"
        )

        ttk.Label(khung_nhap, text="Tác giả:").grid(
            row=0, column=2, padx=(0, 8), pady=6, sticky="w"
        )
        self.o_nhap_tac_gia = ttk.Entry(khung_nhap)
        self.o_nhap_tac_gia.grid(
            row=0, column=3, padx=(0, 18), pady=6, sticky="ew"
        )

        ttk.Label(khung_nhap, text="Thể loại:").grid(
            row=1, column=0, padx=(0, 8), pady=6, sticky="w"
        )
        self.chon_the_loai = ttk.Combobox(
            khung_nhap,
            values=db.DANH_SACH_THE_LOAI,
            state="readonly",
        )
        self.chon_the_loai.grid(
            row=1, column=1, padx=(0, 18), pady=6, sticky="ew"
        )
        self.chon_the_loai.current(0)

        ttk.Button(
            khung_nhap, text="Thêm sách", command=self.xu_ly_them_sach
        ).grid(row=1, column=3, padx=(0, 18), pady=6, sticky="e")

        khung_danh_sach = ttk.LabelFrame(
            self, text="Danh sách sách trong tủ", padding=10
        )
        khung_danh_sach.pack(fill="both", expand=True, padx=16, pady=10)
        khung_danh_sach.columnconfigure(0, weight=1)
        khung_danh_sach.rowconfigure(0, weight=1)

        cot = ("id", "ten_sach", "tac_gia", "the_loai", "trang_thai")
        self.bang_sach = ttk.Treeview(
            khung_danh_sach, columns=cot, show="headings", selectmode="browse"
        )
        self.bang_sach.heading("id", text="ID")
        self.bang_sach.heading("ten_sach", text="Tên sách")
        self.bang_sach.heading("tac_gia", text="Tác giả")
        self.bang_sach.heading("the_loai", text="Thể loại")
        self.bang_sach.heading("trang_thai", text="Trạng thái")
        self.bang_sach.column("id", width=55, anchor="center", stretch=False)
        self.bang_sach.column("ten_sach", width=260)
        self.bang_sach.column("tac_gia", width=190)
        self.bang_sach.column("the_loai", width=140)
        self.bang_sach.column("trang_thai", width=110, anchor="center")

        thanh_cuon = ttk.Scrollbar(
            khung_danh_sach, orient="vertical", command=self.bang_sach.yview
        )
        self.bang_sach.configure(yscrollcommand=thanh_cuon.set)
        self.bang_sach.grid(row=0, column=0, sticky="nsew")
        thanh_cuon.grid(row=0, column=1, sticky="ns")

        khung_nut = ttk.Frame(self, padding=(16, 0, 16, 16))
        khung_nut.pack(fill="x")
        ttk.Button(
            khung_nut,
            text="Đánh dấu đã đọc",
            command=self.xu_ly_danh_dau_da_doc,
        ).pack(side="left", padx=(0, 8))
        ttk.Button(
            khung_nut, text="Xóa sách", command=self.xu_ly_xoa_sach
        ).pack(side="left", padx=8)
        ttk.Button(
            khung_nut,
            text="Thống kê theo thể loại",
            command=self.xu_ly_thong_ke,
        ).pack(side="left", padx=8)

    def tai_lai_danh_sach_sach(self):
        for dong in self.bang_sach.get_children():
            self.bang_sach.delete(dong)

        for id_sach, ten_sach, tac_gia, the_loai, da_doc in db.lay_toan_bo_sach():
            trang_thai = "Đã đọc" if da_doc else "Chưa đọc"
            self.bang_sach.insert(
                "",
                "end",
                values=(id_sach, ten_sach, tac_gia, the_loai, trang_thai),
            )

    def xu_ly_them_sach(self):
        try:
            db.them_sach(
                self.o_nhap_ten_sach.get(),
                self.o_nhap_tac_gia.get(),
                self.chon_the_loai.get(),
            )
        except ValueError as loi:
            messagebox.showerror("Thông tin chưa hợp lệ", str(loi), parent=self)
            return
        except sqlite3.Error as loi:
            messagebox.showerror(
                "Lỗi cơ sở dữ liệu", f"Không thể thêm sách:\n{loi}", parent=self
            )
            return

        ten_sach = self.o_nhap_ten_sach.get().strip()
        self.o_nhap_ten_sach.delete(0, tk.END)
        self.o_nhap_tac_gia.delete(0, tk.END)
        self.tai_lai_danh_sach_sach()
        messagebox.showinfo(
            "Thành công", f"Đã thêm sách: {ten_sach}", parent=self
        )

    def _lay_id_sach_dang_chon(self):
        lua_chon = self.bang_sach.selection()
        if not lua_chon:
            messagebox.showerror(
                "Chưa chọn sách",
                "Vui lòng chọn một cuốn sách trong danh sách.",
                parent=self,
            )
            return None
        return int(self.bang_sach.item(lua_chon[0], "values")[0])

    def xu_ly_danh_dau_da_doc(self):
        id_sach = self._lay_id_sach_dang_chon()
        if id_sach is None:
            return

        try:
            db.danh_dau_da_doc(id_sach)
            self.tai_lai_danh_sach_sach()
        except (ValueError, sqlite3.Error) as loi:
            messagebox.showerror(
                "Không thể cập nhật sách", str(loi), parent=self
            )

    def xu_ly_xoa_sach(self):
        id_sach = self._lay_id_sach_dang_chon()
        if id_sach is None:
            return
        if not messagebox.askyesno(
            "Xác nhận xóa", "Bạn có chắc muốn xóa cuốn sách này?", parent=self
        ):
            return

        try:
            db.xoa_sach(id_sach)
            self.tai_lai_danh_sach_sach()
        except (ValueError, sqlite3.Error) as loi:
            messagebox.showerror("Không thể xóa sách", str(loi), parent=self)

    def xu_ly_thong_ke(self):
        try:
            du_lieu = db.thong_ke_theo_the_loai()
        except sqlite3.Error as loi:
            messagebox.showerror(
                "Lỗi cơ sở dữ liệu", f"Không thể lấy thống kê:\n{loi}", parent=self
            )
            return

        if not du_lieu:
            messagebox.showinfo(
                "Chưa có dữ liệu", "Hãy thêm sách trước khi xem thống kê.", parent=self
            )
            return

        cua_so_bieu_do = tk.Toplevel(self)
        cua_so_bieu_do.title("Thống kê sách theo thể loại")
        cua_so_bieu_do.geometry("720x480")

        the_loai = [dong[0] for dong in du_lieu]
        so_luong = [dong[1] for dong in du_lieu]
        hinh = Figure(figsize=(7, 4.5), dpi=100)
        truc = hinh.add_subplot(111)
        cot = truc.bar(the_loai, so_luong, color="cornflowerblue")
        truc.set_title("Số lượng sách theo thể loại")
        truc.set_xlabel("Thể loại")
        truc.set_ylabel("Số lượng sách")
        truc.bar_label(cot, padding=3)
        truc.grid(axis="y", alpha=0.25)
        hinh.tight_layout()

        canvas = FigureCanvasTkAgg(hinh, master=cua_so_bieu_do)
        canvas.draw()
        canvas.get_tk_widget().pack(fill="both", expand=True)


if __name__ == "__main__":
    ung_dung = UngDungTuSach()
    ung_dung.mainloop()
