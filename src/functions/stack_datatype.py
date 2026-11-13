from typing import Any


class Stack:
    def __init__(self) -> None:
        self._stack = []
        self.size = 0

    def push(self, value: Any) -> None:
        self._stack.append(value)
        self.size += 1

    def pop(self) -> Any:
        if self.size == 0:
            raise IndexError("Stack is empty")
        self.size -= 1
        return self._stack.pop()

    def peek(self) -> Any:
        if self.size == 0:
            raise IndexError("Stack is empty")
        return self._stack[-1]

    def is_empty(self) -> bool:
        return self.size == 0

    def clear(self) -> None:
        self._stack = []
        self.size = 0

    def swap(self) -> None:
        if self.size < 2:
            raise IndexError("Stack has less than 2 elements")
        self._stack[-2], self._stack[-1] = self._stack[-1], self._stack[-2]

    def duplicate(self) -> None:
        if self.size == 0:
            raise IndexError("Stack is empty")
        self.size += 1
        self._stack.append(self._stack[-1])

    def __bool__(self) -> bool:
        return bool(self.size)

    def __contains__(self, item: Any) -> bool:
        return item in self._stack

    def __len__(self) -> int:
        return self.size
