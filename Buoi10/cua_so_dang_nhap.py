import sys
import os
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox

class CuaSoDangNhap(QWidget):
    def __init__(self):
        super().__init__()
        
        # Lấy đường dẫn tuyệt đối
        current_dir = os.path.dirname(os.path.abspath(__file__))
        ui_path = os.path.join(current_dir, "form_dang_nhap.ui")
        
        # Nạp giao diện
        uic.loadUi(ui_path, self) 
        
        # Kết nối signal - slot
        self.nut_dang_nhap.clicked.connect(self.xu_ly_dang_nhap)
        
    # --- PHẦN BẠN CẦN VIẾT THÊM VÀO ---
    def xu_ly_dang_nhap(self):
        tai_khoan = self.o_nhap_tai_khoan.text()
        mat_khau = self.o_nhap_mat_khau.text()
        
        if tai_khoan == "" or mat_khau == "":
            QMessageBox.critical(self, "Loi", "Vui long nhap day du tai khoan va mat khau.")
            return
            
        QMessageBox.information(self, "Thanh cong", f"Xin chao {tai_khoan}, dang nhap thanh cong!")

# --- PHẦN CHẠY CHƯƠNG TRÌNH ---
if __name__ == "__main__":
    app = QApplication(sys.argv)
    cua_so = CuaSoDangNhap()
    cua_so.show()
    sys.exit(app.exec_())