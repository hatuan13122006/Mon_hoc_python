import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLineEdit, QPushButton, QGridLayout, QVBoxLayout, QMessageBox
)
from PyQt5.QtCore import Qt

class MayTinhBoTui(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("May tinh ")
        # Cửa sổ cố định kích thước cho giống Tkinter
        self.setFixedSize(350, 450) 
        
        self.khoi_tao_giao_dien()
        
    def khoi_tao_giao_dien(self):
        layout_chinh = QVBoxLayout()
        
        # 1. Ô hiển thị (QLineEdit)
        self.o_hien_thi = QLineEdit()
        self.o_hien_thi.setReadOnly(True) # Chỉ cho phép xem, không cho gõ phím trực tiếp
        self.o_hien_thi.setAlignment(Qt.AlignRight) # Căn lề phải
        self.o_hien_thi.setFixedHeight(60)
        # Dùng CSS (StyleSheet) để làm chữ to và đậm giống Tkinter
        self.o_hien_thi.setStyleSheet("font-size: 24px; font-weight: bold; padding: 5px; background-color: #f0f0f0;")
        
        layout_chinh.addWidget(self.o_hien_thi)
        
        # 2. Lưới các nút bấm (QGridLayout)
        layout_nut = QGridLayout()
        
        # Định nghĩa danh sách các nút: (Text, Row, Col)
        cac_nut = [
            ('7', 0, 0), ('8', 0, 1), ('9', 0, 2), ('/', 0, 3),
            ('4', 1, 0), ('5', 1, 1), ('6', 1, 2), ('*', 1, 3),
            ('1', 2, 0), ('2', 2, 1), ('3', 2, 2), ('-', 2, 3),
            ('0', 3, 0), ('.', 3, 1), ('=', 3, 2), ('+', 3, 3),
        ]
        
        for text, row, col in cac_nut:
            nut = QPushButton(text)
            nut.setFixedSize(70, 60) # Kích thước nút
            nut.setStyleSheet("font-size: 18px;")
            
            # Xử lý màu sắc và sự kiện riêng cho từng nút
            if text == '=':
                nut.setStyleSheet("font-size: 18px; font-weight: bold; background-color: lightblue;")
                nut.clicked.connect(self.tinh_ket_qua)
            else:
                # Dùng lambda để truyền tham số 'text' vào hàm
                nut.clicked.connect(lambda checked, t=text: self.bam_nut(t))
                
            layout_nut.addWidget(nut, row, col)
            
        # 3. Nút Xóa (C) trải dài cả hàng
        nut_xoa = QPushButton("C")
        nut_xoa.setFixedHeight(60)
        nut_xoa.setStyleSheet("font-size: 18px; font-weight: bold; background-color: lightcoral;")
        nut_xoa.clicked.connect(self.xoa_het)
        
        # Thêm lưới nút và nút xóa vào layout chính
        layout_chinh.addLayout(layout_nut)
        layout_chinh.addWidget(nut_xoa)
        
        self.setLayout(layout_chinh)

    # --- CÁC HÀM XỬ LÝ (SLOT) ---
    
    def bam_nut(self, ky_tu):
        """Thêm ký tự vào ô hiển thị"""
        hien_tai = self.o_hien_thi.text()
        self.o_hien_thi.setText(hien_tai + str(ky_tu))
        
    def xoa_het(self):
        """Xóa toàn bộ nội dung"""
        self.o_hien_thi.clear()
        
    def tinh_ket_qua(self):
        """Tính toán biểu thức"""
        bieu_thuc = self.o_hien_thi.text()
        if not bieu_thuc:
            return
            
        try:
            # Dùng eval() để tính toán giống hệt Tkinter
            ket_qua = eval(bieu_thuc)
            # Xử lý trường hợp kết quả là số thực dài (VD: 0.333333333333)
            if isinstance(ket_qua, float):
                ket_qua = round(ket_qua, 8) # Làm tròn 8 chữ số thập phân
            self.o_hien_thi.setText(str(ket_qua))
            
        except ZeroDivisionError:
            QMessageBox.critical(self, "Loi", "Khong the chia cho 0")
            self.xoa_het()
        except Exception:
            QMessageBox.critical(self, "Loi", "Bieu thuc khong hop le")
            self.xoa_het()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    cua_so = MayTinhBoTui()
    cua_so.show()
    sys.exit(app.exec_())