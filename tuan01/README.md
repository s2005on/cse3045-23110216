\# HW1 - Modern Python Refactoring



\## Thông tin



\- Họ tên: Lâm Hải Sơn

\- MSSV: 23110216

\- Học phần: CSE3045



\## Mô tả



Bài tập refactor chương trình quản lý điểm sinh viên từ phong cách

Python cũ sang phong cách Python hiện đại.



Chương trình đọc thông tin sinh viên từ file CSV, tính điểm trung bình

và phân loại sinh viên.



\## Cấu trúc



\- `old\_student\_report.py`: phiên bản code trước khi refactor.

\- `student\_report.py`: phiên bản sau khi refactor.

\- `students.csv`: dữ liệu sinh viên mẫu.

\- `PROMPTS.md`: ghi nhận việc sử dụng AI.



\## Nội dung refactor



Phiên bản mới sử dụng:



\- Type hints để khai báo kiểu dữ liệu.

\- `@dataclass` để biểu diễn thông tin sinh viên.

\- `pathlib.Path` để xử lý đường dẫn file.

\- f-string để định dạng chuỗi.

\- Context manager (`with`) để quản lý file.



\## Cách chạy



Từ thư mục gốc của repository:



```bash

uv run python tuan01/student\_report.py

