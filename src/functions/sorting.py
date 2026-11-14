import sys
from _collections_abc import Callable
from math import ceil, log2
from typing import Any


class Sorting:
    def bubble_sort(
        self, arr: list, *, key: Callable[[Any], Any] | None = None
    ) -> list:
        if not isinstance(arr, list):
            raise TypeError("Invalid input type")
        new_arr = arr.copy()
        keys = [key(item) if key is not None else item for item in new_arr]
        try:
            for i in range(len(new_arr)):
                for j in range(len(new_arr) - i - 1):
                    if keys[j] > keys[j + 1]:
                        new_arr[j], new_arr[j + 1] = (
                            new_arr[j + 1],
                            new_arr[j],
                        )
                        keys[j], keys[j + 1] = keys[j + 1], keys[j]
            return new_arr
        except TypeError as error:
            raise TypeError("Invalid input type") from error

    def _merge_sort_iteration(self, arr: list) -> list:
        length = len(arr)
        size = 1
        while size < len(arr):
            for left in range(0, length, 2 * size):
                mid = min(left + size, length)
                right = min(left + 2 * size, length)

                merged = []
                i, j = left, mid
                while i < mid and j < right:
                    if arr[i][1] <= arr[j][1]:
                        merged.append(arr[i])
                        i += 1
                    else:
                        merged.append(arr[j])
                        j += 1

                merged.extend(arr[i:mid])
                merged.extend(arr[j:right])

                arr[left:right] = merged
            size *= 2
        return arr

    def _merge_sort_recursive(self, arr: list) -> list:
        length = len(arr)
        if length <= 1:
            return arr
        left = self._merge_sort_recursive(arr[: length // 2])
        right = self._merge_sort_recursive(arr[length // 2 :])
        result = []
        i, j = 0, 0
        while i < len(left) and j < len(right):
            if right[j][1] < left[i][1]:
                result.append(right[j])
                j += 1
            else:
                result.append(left[i])
                i += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result

    def merge_sort(self, arr: list, *, key: Callable[[Any], Any] | None = None) -> list:
        if not isinstance(arr, list):
            raise TypeError("Invalid input type")
        if len(arr) <= 1:
            return arr
        try:
            new_arr = arr.copy()
            items = [(item, key(item) if key is not None else item) for item in new_arr]
            if ceil(log2(len(arr))) + 1 >= sys.getrecursionlimit():
                sorted_items = self._merge_sort_iteration(items)
                return [item for item, _ in sorted_items]
            else:
                sorted_items = self._merge_sort_recursive(items)
                return [item for item, _ in sorted_items]
        except TypeError as error:
            raise TypeError("Invalid input type") from error
