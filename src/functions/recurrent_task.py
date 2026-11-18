import sys
from math import ceil, log2


def fast_power_iteration(value: float, power: int) -> float | int:
    """Raises a value to power by using fast power algorithm
    Input: value, power
    Output: value^power"""
    if not isinstance(value, (float, int)) or not isinstance(power, int):
        raise TypeError("Invalid data")
    if power < 0:
        return 1 / fast_power_iteration(value, -power) # process expression
    result = 1
    base = value
    while power > 0: # the algorithm
        if power % 2 == 1:
            result *= base

        base *= base
        power //= 2

    return result


def fast_power_recursive(
    value: float, power: int, *, _check: bool = True
) -> float | int:
    """Raises a value to power by using fast power algorithm
        Input: value, power
        Output: value^power"""
    if not isinstance(value, (float, int)) or not isinstance(power, int):
        raise TypeError("Invalid data")
    if power < 0:
        return 1 / fast_power_recursive(value, -power) # process expression
    if power == 0:
        return 1
    if _check:
        if power == 0:
            return 1
        if ceil(log2(power)) > sys.getrecursionlimit(): # check max recursion depth
            raise ValueError("Recursion limit exceeded")

    half = fast_power_recursive(value, power // 2, _check=False) # the same algorithm but by recursion

    if power % 2 == 1:
        return half * half * value
    else:
        return half * half
