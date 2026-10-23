# HW2 - Cấu trúc dữ liệu ứng dụng và Python nâng cao

- Sinh viên: Lâm Hải Sơn
- MSSV: 23110216
- Python: 3.10 trở lên; đã chạy kiểm tra bằng Python 3.12.14.

## Phạm vi và điều cần xác nhận

PDF yêu cầu chọn cấu trúc dữ liệu cho **hai bài toán cho sẵn**, nhưng không
ghi nội dung hai bài toán. Bản này dùng hai bài toán minh họa tự chọn dưới đây.
Cần đối chiếu đề chi tiết của giảng viên trước khi nộp chính thức.

## 1. Tra cứu sinh viên theo MSSV

Cho danh sách sinh viên có MSSV duy nhất. Cần tra cứu nhiều lần bằng MSSV,
trả về sinh viên tương ứng hoặc `None` nếu không có.

Chọn `dict[str, Student]`: khóa là MSSV, giá trị là đối tượng sinh viên.

| Thao tác | Độ phức tạp |
| --- | --- |
| Tạo chỉ mục từ n sinh viên | O(n) trung bình |
| Tra cứu một MSSV | O(1) trung bình; O(n) trong trường hợp xấu nhất |
| Bộ nhớ chỉ mục | O(n) |

Nếu giữ `list` rồi duyệt từng sinh viên, mỗi lần tìm có thể tốn O(n).
Dictionary phù hợp khi cần tìm nhiều lần theo khóa. Mã trùng gây `ValueError`
để không âm thầm ghi đè sinh viên trước đó. Các phân tích trên coi độ dài mã
là giới hạn; chúng bỏ qua chi phí xử lý chuỗi theo độ dài mã.

## 2. Xử lý yêu cầu theo thứ tự đến

Yêu cầu đến trước được xử lý trước (FIFO). Thêm yêu cầu ở cuối, lấy ở đầu.
Chọn `collections.deque`, dùng `append()` và `popleft()`.

| Thao tác | Độ phức tạp |
| --- | --- |
| Thêm ở cuối bằng append | O(1) |
| Lấy ở đầu bằng popleft | O(1) |
| Bộ nhớ cho n yêu cầu | O(n) |

`list.pop(0)` tốn O(n) vì phải dịch các phần tử còn lại. Khi hàng đợi rỗng,
`take_next()` trả `None`. Dữ liệu yêu cầu là chuỗi nên không nhầm với `None`.

## 3. Dataclass và match/case

`Student` có hai trường `student_id` và `name`. `@dataclass` tự sinh hàm
khởi tạo, biểu diễn và so sánh. `frozen=True` ngăn gán lại các trường thông
thường sau khi tạo; kiểu dữ liệu được khai báo không tự kiểm tra lúc chạy.

`describe_command()` tách chuỗi thành danh sách và dùng `match/case`:

- `find 23110216`: nhận đúng hai thành phần và lấy MSSV.
- `next`: xử lý yêu cầu tiếp theo.
- `quit`: kết thúc.
- Các trường hợp khác: lệnh không hợp lệ.

Hàm này chỉ **mô tả** lệnh; việc tra cứu và lấy yêu cầu được minh họa riêng
trong `main()`, không phải một ứng dụng dòng lệnh tương tác hoàn chỉnh.

## 4. Async/await

`async_demo.py` dùng `asyncio.gather()` để chạy đồng thời hai coroutine,
mỗi coroutine mô phỏng chờ I/O bằng `await asyncio.sleep(1.0)`.
Trong lúc một tác vụ chờ, event loop có thể chạy tác vụ còn lại.
Tổng thời gian thường khoảng 1 giây thay vì khoảng 2 giây nếu chờ tuần tự.
Đây là tính đồng thời khi chờ I/O, không phải chạy tính toán trên hai CPU.
Ví dụ không gọi API thật và không cần mạng. Thời gian thực tế có thể dao động.
Kết quả của `gather` giữ thứ tự đầu vào, dù thứ tự hoàn thành có thể khác nhau.

## 5. Chạy trên Windows

Mở PowerShell **tại thư mục gốc `cse3045-23110216`**, nơi chứa `tuan02`:

```powershell
py -3 tuan02/data_structures.py
py -3 tuan02/async_demo.py
py -3 -m unittest discover -s tuan02 -p "test_*.py" -v
```

Nếu dùng môi trường uv đã tạo ở HW1, thay `py -3` bằng
`.\.venv\Scripts\python.exe`. Trên Linux/macOS có thể dùng `python3`.
Chương trình chỉ dùng thư viện chuẩn, không cần cài thêm gói.

Kết quả `data_structures.py`:

```text
Tìm thấy: Lâm Hải Sơn
Mã không tồn tại: None
Tra cứu sinh viên: 23110216
Lượt 1: Yêu cầu A
Lượt 2: Yêu cầu B
Hàng đợi rỗng: None
```

Kết quả async: hai dòng `Bắt đầu` xuất hiện trước hai dòng `Hoàn thành`,
sau đó có danh sách dữ liệu và thời gian khoảng 1 giây.

## 6. Kiểm tra đã thực hiện

Trợ lý đã chạy hai chương trình và bộ kiểm thử trên Python 3.12.14:
**6 test đạt**. Các test kiểm tra tìm thấy/không tìm thấy, danh sách rỗng,
MSSV trùng, FIFO và hàng đợi rỗng, các mẫu lệnh, và khả năng khởi động cả
hai tác vụ trước khi một tác vụ hoàn thành. Test async dùng sự kiện đồng bộ,
không khẳng định một ngưỡng thời gian chạy tuyệt đối.

Chưa chạy ruff/mypy trong môi trường chuẩn bị. Chưa xác nhận người học
đã chạy trên máy cá nhân, chưa xác nhận PR hoặc nộp LMS.

## 7. Tự giải thích trước khi nộp

1. Vì sao dùng dictionary thay vì duyệt list để tra cứu nhiều lần?
2. Vì sao deque tốt hơn list.pop(0) cho hàng đợi?
3. `case ["find", student_id]` nhận những lệnh nào?
4. `await` nhường quyền thực thi khi nào? Vì sao hai lần chờ mất khoảng 1 giây?
5. Chương trình xử lý MSSV trùng và hàng đợi rỗng ra sao?

Xem `PROMPTS.md` để biết phần AI hỗ trợ và phần người học cần hoàn thành.
