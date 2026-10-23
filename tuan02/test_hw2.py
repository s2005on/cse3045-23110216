"""Kiểm tra dữ liệu biên, FIFO, lệnh và sự chồng lấp hai tác vụ."""

import asyncio
import unittest
from collections import deque

from tuan02.data_structures import Student, build_index, describe_command, take_next


class DataStructureTests(unittest.TestCase):
    def test_lookup_and_missing_id(self) -> None:
        student = Student("23110216", "Lâm Hải Sơn")
        index = build_index([student])
        self.assertEqual(index.get("23110216"), student)
        self.assertIsNone(index.get("missing"))

    def test_empty_index(self) -> None:
        self.assertEqual(build_index([]), {})

    def test_duplicate_id_rejected(self) -> None:
        with self.assertRaises(ValueError):
            build_index([Student("1", "An"), Student("1", "Bình")])

    def test_fifo_and_empty_queue(self) -> None:
        queue: deque[str] = deque(["A", "B"])
        self.assertEqual(take_next(queue), "A")
        queue.append("C")
        self.assertEqual(take_next(queue), "B")
        self.assertEqual(take_next(queue), "C")
        self.assertIsNone(take_next(queue))

    def test_commands(self) -> None:
        cases = {
            "find 23110216": "Tra cứu sinh viên: 23110216",
            "next": "Xử lý yêu cầu đầu hàng đợi",
            "quit": "Kết thúc",
            "find": "Lệnh không hợp lệ",
            "find 1 2": "Lệnh không hợp lệ",
            "": "Lệnh không hợp lệ",
        }
        for command, expected in cases.items():
            with self.subTest(command=command):
                self.assertEqual(describe_command(command), expected)


class AsyncTests(unittest.IsolatedAsyncioTestCase):
    async def test_demo_starts_both_tasks_before_either_finishes(self) -> None:
        from unittest.mock import patch

        from tuan02 import async_demo

        started: list[str] = []
        both_started = asyncio.Event()

        async def fake_fetch(name: str, delay: float) -> str:
            started.append(name)
            if len(started) == 2:
                both_started.set()
            await asyncio.wait_for(both_started.wait(), timeout=2.0)
            return f"Dữ liệu {name}"

        with patch.object(async_demo, "fetch_data", side_effect=fake_fetch):
            with patch("builtins.print"):
                await async_demo.main()
        self.assertEqual(started, ["sinh viên", "môn học"])


if __name__ == "__main__":
    unittest.main()
