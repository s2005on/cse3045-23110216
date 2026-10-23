"""Mô phỏng hai tác vụ I/O đồng thời, không cần mạng."""

import asyncio
from time import perf_counter


async def fetch_data(name: str, delay: float) -> str:
    print(f"Bắt đầu: {name}")
    await asyncio.sleep(delay)
    print(f"Hoàn thành: {name}")
    return f"Dữ liệu {name}"


async def main() -> None:
    start = perf_counter()
    results = await asyncio.gather(
        fetch_data("sinh viên", 1.0),
        fetch_data("môn học", 1.0),
    )
    print(f"Kết quả: {results}")
    print(f"Thời gian: {perf_counter() - start:.2f} giây")


if __name__ == "__main__":
    asyncio.run(main())
