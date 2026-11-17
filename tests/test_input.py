import pytest

from functions.generator import Generator
from functions.sorting import Sorting


def test_empty_input():
    sort = Sorting()
    generator = Generator(seed="test")

    assert sort.bubble_sort([]) == []
    assert sort.merge_sort([]) == []

    assert generator.random_list(size=0) == []
    assert generator.random_sorted_list(size=0) == []
    assert generator.random_almost_sorted_list(size=0) == []
    assert generator.random_duplicated_list(size=0) == []
    assert generator.random_reversed_list(size=0) == []


def test_invalid_input():
    sort = Sorting()
    generator = Generator(seed="test")

    with pytest.raises(TypeError):
        sort.bubble_sort([1, 2, "Name"])
    with pytest.raises(TypeError):
        sort.merge_sort([1, 2, "Name"])

    with pytest.raises(ValueError):
        generator.random_list(-1)
    with pytest.raises(ValueError):
        generator.random_sorted_list(-1)
    with pytest.raises(ValueError):
        generator.random_duplicated_list(-1)
    with pytest.raises(ValueError):
        generator.random_reversed_list(-1)
    with pytest.raises(ValueError):
        generator.random_almost_sorted_list(-1)


def test_one_element():
    sort = Sorting()

    assert sort.bubble_sort([1]) == [1]
    assert sort.merge_sort([1]) == [1]


def test_sorted_list():
    sort = Sorting()
    generator = Generator(seed="test")

    arr = generator.random_sorted_list(size=10)

    assert sort.bubble_sort(arr) == arr
    assert sort.merge_sort(arr) == arr


def test_reversed_list():
    sort = Sorting()
    generator = Generator(seed="test")

    arr = generator.random_reversed_list(size=10)

    assert sort.bubble_sort(arr) == list(reversed(arr))
    assert sort.merge_sort(arr) == list(reversed(arr))


def test_duplicated_list():
    sort = Sorting()
    generator = Generator(seed="test")

    arr = generator.random_duplicated_list(size=100)
    assert sort.bubble_sort(arr) == sorted(arr)
    assert sort.merge_sort(arr) == sorted(arr)


def test_negative_numbers():
    sort = Sorting()
    generator = Generator(seed="test")

    arr = generator.random_list(size=100, start=-1000, end=-1)

    assert sort.bubble_sort(arr) == sorted(arr)
    assert sort.merge_sort(arr) == sorted(arr)


def test_reproducibility():
    first = Generator(seed="TESTING")
    second = Generator(seed="TESTING")

    assert first.random_list(100) == second.random_list(100)
    assert first.random_sorted_list(100) == second.random_sorted_list(100)
    assert first.random_duplicated_list(100) == second.random_duplicated_list(100)
    assert first.random_reversed_list(100) == second.random_reversed_list(100)
    assert first.random_almost_sorted_list(100) == second.random_almost_sorted_list(100)


def test_empty_structure():
    generator = Generator(seed="TESTING")
    sort = Sorting()
    with pytest.raises(TypeError):
        sort.bubble_sort(generator)
    with pytest.raises(TypeError):
        sort.merge_sort(generator)


def test_key_sorting():
    sort = Sorting()
    arr = ["A", "AAA", "AA", "AAAAAAA", "BBG", "ZHHI"]
    expected = ["A", "AA", "AAA", "BBG", "ZHHI", "AAAAAAA"]

    assert sort.bubble_sort(arr, key=len) == expected
    assert sort.merge_sort(arr, key=len) == expected


def test_stability():
    sort = Sorting()
    arr = [
        {"name": "Anna", "age": 14},
        {"name": "Bob", "age": 18},
        {"name": "Anna", "age": 12},
    ]
    expected = [
        {"name": "Anna", "age": 14},
        {"name": "Anna", "age": 12},
        {"name": "Bob", "age": 18},
    ]

    assert sort.merge_sort(arr, key=lambda x: x["name"]) == expected
