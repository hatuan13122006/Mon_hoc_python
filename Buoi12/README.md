# Đồ án quản lý Tủ sách cá nhân

Ứng dụng Tkinter lưu tủ sách bằng SQLite, cho phép thêm sách, xem danh sách,
đánh dấu đã đọc, xóa sách và xem biểu đồ số lượng theo thể loại.

## Các tệp

- `csdl_sach.py`: tạo bảng và cung cấp các thao tác SQLite.
- `ung_dung_tu_sach.py`: giao diện Tkinter và biểu đồ Matplotlib.
- `tu_sach.db`: cơ sở dữ liệu mẫu để mở ứng dụng với dữ liệu có sẵn.
- `test_csdl_sach.py`: kiểm thử các thao tác và kiểm tra dữ liệu.

## Chạy ứng dụng

Mở terminal tại thư mục `Buoi12`, sau đó chạy:

```text
python ung_dung_tu_sach.py
```

SQLite được tích hợp trong Python. Ứng dụng cần Matplotlib để hiển thị biểu đồ.
Dữ liệu được lưu cạnh các tệp chương trình trong `tu_sach.db`.

## Kiểm thử

```text
python -m unittest test_csdl_sach.py
```
