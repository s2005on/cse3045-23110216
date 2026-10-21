# HW3 — Kiểm thử hàm tính tổng tiền

- Sinh viên: Lâm Hải Sơn
- MSSV: 23110216
- Python: 3.12

## Chức năng
calculate_total(items) tính tổng tiền từ danh sách (giá, số lượng).
- Giá: số nguyên không âm, đơn vị VND.
- Số lượng: số nguyên dương.
- Không chấp nhận chuỗi, số thập phân hoặc boolean.
- Giỏ hàng rỗng trả về 0.

Ví dụ: [(25000, 2), (10000, 3)] trả về 80000.

## Cài đặt và chạy trên Windows
Chạy từ thư mục gốc của repo:

```powershell
uv venv --python 3.12
uv pip install -r tuan03/requirements-dev.txt
.\.venv\Scripts\python.exe -m pytest tuan03 -q --cov=tuan03.cart --cov-report=term-missing --cov-fail-under=80
```

## Kết quả trên máy
- 13 trường hợp kiểm thử thành công.
- Độ bao phủ dòng lệnh của tuan03/cart.py: 100%.
- Ngưỡng yêu cầu: 80%.
- Coverage 100% không có nghĩa là chương trình không còn lỗi.

## Quá trình thực hiện
1. Tạo bộ kiểm thử trước.
2. Chạy thử và nhận ModuleNotFoundError vì chưa có cart.py.
3. Viết hàm calculate_total.
4. Chạy lại: 13 passed, coverage 100%.
5. Do thiếu cấu hình danh tính Git, các commit ban đầu bị lỗi.
   Sau khi sửa cấu hình, lưu riêng commit test và commit hàm.

## GitHub Actions
Workflow: .github/workflows/hw3-tests.yml.
Tự chạy khi push nhánh tuan03/main hoặc mở PR vào main.
Kiểm tra thất bại nếu test lỗi hoặc coverage dưới 80%.
Kết quả CI thực tế xem trong tab Actions và phần Checks của PR.

## Tài liệu dự án B3
Charter, yêu cầu, thiết kế, WBS và Gantt thuộc repo đồ án:
https://github.com/s2005on/vnu-food-hola/pull/3
