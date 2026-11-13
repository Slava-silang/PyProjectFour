import copy
import sys
from math import log2, ceil


class Sorting:
    def bubble_sort(self, arr: list) -> list:
        if not isinstance(arr, list):
            raise TypeError("Invalid input type")
        new_arr = copy.deepcopy(arr)
        try:
            for i in range(len(new_arr)):
                for j in range(len(new_arr) - i - 1):
                    if new_arr[j] > new_arr[j + 1]:
                        new_arr[j], new_arr[j + 1] = new_arr[j + 1], new_arr[j]
            return new_arr
        except TypeError as error:
            raise TypeError("Invalid input type") from error

    def _merge_sort_iteration(self, arr: list) -> list:
        new_arr = copy.deepcopy(arr)
        length = len(new_arr)
        size = 1
        while size < len(arr):
            for left in range(0, length, 2 * size):
                mid = min(left + size, length)
                right = min(left + 2 * size, length)

                merged = []
                i, j = left, mid
                while i < mid and j < right:
                    if new_arr[i] <= new_arr[j]:
                        merged.append(new_arr[i])
                    else:
                        merged.append(new_arr[j])

                merged.extend(new_arr[i:mid])
                merged.extend(new_arr[j:right])

                arr[left:right] = merged
            size *= 2
        return new_arr

    def _merge_sort_recursive(self, arr: list) -> list:
        length = len(arr)
        if length == 1:
            return arr
        left = self._merge_sort_recursive(arr[:length//2])
        right = self._merge_sort_recursive(arr[length//2:])
        result = []
        i, j = 0, 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result

    def merge_sort(self, arr: list) -> list:
        if not isinstance(arr, list):
            raise TypeError("Invalid input type")
        try:
            if ceil(log2(len(arr))) + 1 >= sys.getrecursionlimit():
                return self._merge_sort_iteration(arr)
            else:
                return self._merge_sort_recursive(arr)
        except TypeError as error:
            raise TypeError("Invalid input type") from error
