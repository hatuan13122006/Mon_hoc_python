import sqlite3
from contextlib import closing
from pathlib import Path


TEN_FILE_CSDL = Path(__file__).with_name("tu_sach.db")
DANH_SACH_THE_LOAI = (
    "Kỹ năng sống",
    "Tiểu thuyết",
    "Lịch sử",
    "Khoa học",
    "Kinh tế",
    "Khác",
)


def ket_noi_csdl():
    return sqlite3.connect(TEN_FILE_CSDL)


def tao_bang_neu_chua_co():
    with closing(ket_noi_csdl()) as ket_noi:
        with ket_noi:
            ket_noi.execute(
                """
                CREATE TABLE IF NOT EXISTS sach (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    ten_sach TEXT NOT NULL,
                    tac_gia TEXT NOT NULL,
                    the_loai TEXT NOT NULL,
                    da_doc INTEGER NOT NULL DEFAULT 0
                        CHECK (da_doc IN (0, 1))
                )
                """
            )


def them_sach(ten_sach, tac_gia, the_loai):
    ten_sach = ten_sach.strip()
    tac_gia = tac_gia.strip()
    if not ten_sach or not tac_gia:
        raise ValueError("Tên sách và tác giả không được để trống.")
    if the_loai not in DANH_SACH_THE_LOAI:
        raise ValueError("Vui lòng chọn thể loại trong danh sách.")

    with closing(ket_noi_csdl()) as ket_noi:
        with ket_noi:
            ket_noi.execute(
                """
                INSERT INTO sach (ten_sach, tac_gia, the_loai)
                VALUES (?, ?, ?)
                """,
                (ten_sach, tac_gia, the_loai),
            )


def lay_toan_bo_sach():
    with closing(ket_noi_csdl()) as ket_noi:
        return ket_noi.execute(
            """
            SELECT id, ten_sach, tac_gia, the_loai, da_doc
            FROM sach
            ORDER BY id
            """
        ).fetchall()


def xoa_sach(id_sach):
    with closing(ket_noi_csdl()) as ket_noi:
        with ket_noi:
            ket_qua = ket_noi.execute(
                "DELETE FROM sach WHERE id = ?", (id_sach,)
            )
            if ket_qua.rowcount == 0:
                raise ValueError("Không tìm thấy sách cần xóa.")


def danh_dau_da_doc(id_sach):
    with closing(ket_noi_csdl()) as ket_noi:
        with ket_noi:
            ket_qua = ket_noi.execute(
                "UPDATE sach SET da_doc = 1 WHERE id = ?", (id_sach,)
            )
            if ket_qua.rowcount == 0:
                raise ValueError("Không tìm thấy sách cần đánh dấu.")


def thong_ke_theo_the_loai():
    with closing(ket_noi_csdl()) as ket_noi:
        return ket_noi.execute(
            """
            SELECT the_loai, COUNT(*)
            FROM sach
            GROUP BY the_loai
            ORDER BY the_loai
            """
        ).fetchall()
