import sys
from math import log2, ceil
def fast_power_iteration(value: float | int, power: int) -> float | int:
    if not isinstance(value, (float, int)) or not isinstance(power, int):
        raise ValueError('Invalid data')
    if power < 0:
        return 1 / fast_power_iteration(value, -power)
    result = 1
    base = value
    while power > 0:
        if power % 2 == 1:
            result *= base

        base *= base
        power //= 2

    return result

def fast_power_recursive(value: float | int, power: int, *, _check: bool = True) -> float | int:
    if not isinstance(value, (float, int)) or not isinstance(power, int):
        raise ValueError('Invalid data')
    if power < 0:
        return 1 / fast_power_recursive(value, -power)
    if _check:
        if power == 0:
            return 1
        if ceil(log2(power)) > sys.getrecursionlimit():
            raise ValueError('Recursion limit exceeded')

    half = fast_power_recursive(value, power // 2, _check=False)

    if power % 2 == 1:
        return half * half
    else:
        return half * half * value
