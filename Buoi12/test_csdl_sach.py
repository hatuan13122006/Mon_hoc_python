import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import csdl_sach as db


class KiemThuCSDLThuSach(unittest.TestCase):
    def setUp(self):
        self.thu_muc = tempfile.TemporaryDirectory()
        self.patch_duong_dan = patch.object(
            db, "TEN_FILE_CSDL", Path(self.thu_muc.name) / "kiem_thu.db"
        )
        self.patch_duong_dan.start()
        db.tao_bang_neu_chua_co()

    def tearDown(self):
        self.patch_duong_dan.stop()
        self.thu_muc.cleanup()

    def test_them_va_lay_sach(self):
        db.them_sach("Nhà Giả Kim", "Paulo Coelho", "Tiểu thuyết")

        sach = db.lay_toan_bo_sach()

        self.assertEqual(len(sach), 1)
        self.assertEqual(sach[0][1:], ("Nhà Giả Kim", "Paulo Coelho", "Tiểu thuyết", 0))

    def test_danh_dau_da_doc(self):
        db.them_sach("Sapiens", "Yuval Noah Harari", "Lịch sử")
        id_sach = db.lay_toan_bo_sach()[0][0]

        db.danh_dau_da_doc(id_sach)

        self.assertEqual(db.lay_toan_bo_sach()[0][4], 1)

    def test_xoa_sach(self):
        db.them_sach("Sapiens", "Yuval Noah Harari", "Lịch sử")
        id_sach = db.lay_toan_bo_sach()[0][0]

        db.xoa_sach(id_sach)

        self.assertEqual(db.lay_toan_bo_sach(), [])

    def test_thong_ke_theo_the_loai(self):
        db.them_sach("Sách A", "Tác giả A", "Khoa học")
        db.them_sach("Sách B", "Tác giả B", "Khoa học")
        db.them_sach("Sách C", "Tác giả C", "Lịch sử")

        self.assertEqual(
            db.thong_ke_theo_the_loai(), [("Khoa học", 2), ("Lịch sử", 1)]
        )

    def test_tu_choi_thong_tin_bat_buoc_bi_trong(self):
        with self.assertRaises(ValueError):
            db.them_sach(" ", "Tác giả", "Tiểu thuyết")

        with self.assertRaises(ValueError):
            db.them_sach("Tên sách", " ", "Tiểu thuyết")

    def test_tu_choi_id_khong_ton_tai(self):
        with self.assertRaises(ValueError):
            db.xoa_sach(999)

        with self.assertRaises(ValueError):
            db.danh_dau_da_doc(999)


if __name__ == "__main__":
    unittest.main()
