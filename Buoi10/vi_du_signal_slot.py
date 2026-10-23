import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLineEdit, QVBoxLayout

class ViDuSignalSlot(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Vi du Signal - Slot")
        self.resize(300, 180)
        
        # 1. Tạo các widget
        self.o_nhap = QLineEdit()
        nut_hien_thi = QPushButton("Hien thi noi dung")
        self.nhan_ket_qua = QLabel("Chua co noi dung")
        
        # 2. Sắp xếp vào layout
        layout = QVBoxLayout()
        layout.addWidget(self.o_nhap)
        layout.addWidget(nut_hien_thi)
        layout.addWidget(self.nhan_ket_qua)
        self.setLayout(layout)
        
        # 3. KẾT NỐI SIGNAL - SLOT (Phần quan trọng nhất)
        #        # (Nằm trong hàm __init__)
        nut_hien_thi.clicked.connect(self.hien_thi_noi_dung) # Slot 1
        # Thêm dòng này để kết nối thêm 1 slot dùng lambda
        nut_hien_thi.clicked.connect(lambda: print("Nut vua duoc bam!")) # Slot 2
        
    # Hàm này chính là SLOT (nơi xử lý sự kiện)
    def hien_thi_noi_dung(self):
        noi_dung = self.o_nhap.text() # Lấy text từ QLineEdit
        self.nhan_ket_qua.setText(f"Ban vua nhap: {noi_dung}") # Gán vào QLabel

if __name__ == "__main__":
    app = QApplication(sys.argv)
    cua_so = ViDuSignalSlot()
    cua_so.show()
    sys.exit(app.exec_())