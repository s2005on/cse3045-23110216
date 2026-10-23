"""HW2: tra cứu theo mã và xử lý yêu cầu theo FIFO."""

from collections import deque
from dataclasses import dataclass


@dataclass(frozen=True)
class Student:
    student_id: str
    name: str


def build_index(students: list[Student]) -> dict[str, Student]:
    """Lập chỉ mục; từ chối mã trùng để không ghi đè dữ liệu."""
    index: dict[str, Student] = {}
    for student in students:
        if student.student_id in index:
            raise ValueError(f"MSSV bị trùng: {student.student_id}")
        index[student.student_id] = student
    return index


def describe_command(command: str) -> str:
    """Phân loại lệnh bằng structural pattern matching."""
    match command.split():
        case ["find", student_id]:
            return f"Tra cứu sinh viên: {student_id}"
        case ["next"]:
            return "Xử lý yêu cầu đầu hàng đợi"
        case ["quit"]:
            return "Kết thúc"
        case _:
            return "Lệnh không hợp lệ"


def take_next(queue: deque[str]) -> str | None:
    """Lấy yêu cầu đến trước; trả None khi hàng đợi rỗng."""
    return queue.popleft() if queue else None


def main() -> None:
    students = [Student("23110216", "Lâm Hải Sơn"), Student("23110001", "An")]
    index = build_index(students)
    student = index.get("23110216")
    print(f"Tìm thấy: {student.name if student else 'Không có'}")
    print(f"Mã không tồn tại: {index.get('00000000')}")
    print(describe_command("find 23110216"))
    queue: deque[str] = deque()
    queue.append("Yêu cầu A")
    queue.append("Yêu cầu B")
    print(f"Lượt 1: {take_next(queue)}")
    print(f"Lượt 2: {take_next(queue)}")
    print(f"Hàng đợi rỗng: {take_next(queue)}")


if __name__ == "__main__":
    main()
