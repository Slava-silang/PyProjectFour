import random
from typing import Any


class Generator:
    def __init__(self, seed: Any = "Stanislav") -> None:
        self._seed = str(seed) # save seed when object is created

    def random_list(self, size: int, *, start: int = 0, end: int = 1000) -> list[int]:
        """Returns a list of random integers between start and end"""
        if type(size) is not int:
            raise TypeError("Size must be an integer")
        if type(start) is not int or type(end) is not int:
            raise TypeError("Start or end must be an integer")
        if size < 0:
            raise ValueError("Size must be positive")
        generator = random.Random(self._seed)
        return [generator.randint(start, end) for _ in range(size)]

    def random_sorted_list(
        self, size: int, *, start: int = 0, end: int = 1000
    ) -> list[int]:
        """Returns a sorted list of random integers between start and end"""
        if type(size) is not int:
            raise TypeError("Size must be an integer")
        if type(start) is not int or type(end) is not int:
            raise TypeError("Start or end must be an integer")
        if size < 0:
            raise ValueError("Size must be positive")
        generator = random.Random(self._seed)
        arr = [generator.randint(start, end) for _ in range(size)]
        arr.sort()
        return arr

    def random_reversed_list(
        self, size: int, *, start: int = 0, end: int = 1000
    ) -> list[int]:
        """Returns a reversed list of random integers between start and end"""
        if type(size) is not int:
            raise TypeError("Size must be an integer")
        if type(start) is not int or type(end) is not int:
            raise TypeError("Start or end must be an integer")
        if size < 0:
            raise ValueError("Size must be positive")
        generator = random.Random(self._seed)
        arr = [generator.randint(start, end) for _ in range(size)]
        arr.sort(reverse=True)
        return arr

    def random_almost_sorted_list(
        self, size: int, *, start: int = 0, end: int = 1000
    ) -> list[int]:
        """Makes a random sorted list of integers between start and end
        and replace some items.
        WARNING: does not guarantee replacing if count of items is too small"""
        if type(size) is not int:
            raise TypeError("Size must be an integer")
        if type(start) is not int or type(end) is not int:
            raise TypeError("Start or end must be an integer")
        if size < 0:
            raise ValueError("Size must be positive")
        generator = random.Random(self._seed)
        arr = [generator.randint(start, end) for _ in range(size)]
        arr.sort()
        for i in range(generator.randint(size // 16, size // 8)):
            i = generator.randint(0, size - 1)
            j = generator.randint(0, size - 1)
            arr[i], arr[j] = arr[j], arr[i]

        return arr

    def random_duplicated_list(
        self, size: int, *, start: int = 0, end: int = 1000
    ) -> list[int]:
        """Makes a random list of integers between start and end
        and makes some duplicates
        WARNING: does not guarantee duplicates if count of items is too small"""
        if type(size) is not int:
            raise TypeError("Size must be an integer")
        if type(start) is not int or type(end) is not int:
            raise TypeError("Start or end must be an integer")
        if size < 0:
            raise ValueError("Size must be positive")
        generator = random.Random(self._seed)
        arr = [generator.randint(start, end) for _ in range(size)]
        for i in range(generator.randint(size // 2, size * 3 // 4)):
            i = generator.randint(0, size - 1)
            key = generator.randint(0, size - 1)
            arr[(key + i) % size] = arr[i]
        return arr
