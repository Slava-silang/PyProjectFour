from math import log2
from pathlib import Path
from statistics import mean
from time import perf_counter
from typing import Any

from .generator import Generator
from .sorting import Sorting


def make_benchmark(*, seed: Any = "Stanislav", repeats: int = 5) -> list[dict]:
    benchmark = []
    generator = Generator(seed=seed)
    sorting = Sorting()
    algorithms = {
        "bubble": sorting.bubble_sort,
        "merge": sorting.merge_sort,
    }

    datasets = {
        "random": generator.random_list,
        "sorted": generator.random_sorted_list,
        "reversed": generator.random_reversed_list,
        "almost_sorted": generator.random_almost_sorted_list,
        "duplicates": generator.random_duplicated_list,
    }

    for size in [100, 1_000, 10_000]:
        for dataset_name, generate in datasets.items():
            original = generate(size)
            expected = sorted(original)
            for algorithm, sort in algorithms.items():
                durations = []
                status = "OK"
                for _ in range(repeats):
                    data = original.copy()
                    start = perf_counter()
                    result = sort(data)
                    elapsed = perf_counter() - start

                    if result != expected:
                        status = AssertionError(
                            f"Algorithm {algorithm} failed",
                            f"{dataset_name}: size {size}",
                        )
                        durations = [0]
                        break
                    durations.append(elapsed)

                benchmark.append(
                    {
                        "algorithm": algorithm,
                        "dataset": dataset_name,
                        "size": size,
                        "status": status,
                        "time": mean(durations),
                    }
                )
    return benchmark


def print_benchmark(
    benchmark: list[dict] | None = None, *, seed: Any = "Stanislav", repeats: int = 5
) -> None:
    if benchmark is None:
        benchmark = make_benchmark(seed=seed, repeats=repeats)
    print("Algorithm name | Dataset       | Size       | Time in second | Status")
    for item in benchmark:
        print(
            f"{item['algorithm']:14} | {item['dataset']:13} | {item['size']:10} | {item['time']:.10e} | {item['status']}"
        )


def write_benchmark(
    path: str | Path = "benchmark.md",
    benchmark: list[dict] | None = None,
    *,
    seed: Any = "Stanislav",
    repeats: int = 5,
):
    if benchmark is None:
        benchmark = make_benchmark(seed=seed, repeats=repeats)
    try:
        path = Path(path)
        with path.open(mode="w", encoding="utf-8") as file:
            file.write(
                "|Algorithm name | Dataset | Size | Time in second | Status|" + "\n"
            )
            file.write("|---|---|---|---|---|" + "\n")
            for item in benchmark:
                file.write(
                    f"|{item['algorithm']} | {item['dataset']} | {item['size']} | {item['time']} | {item['status']}|"
                    + "\n"
                )
    except OSError:
        raise OSError("Cannot write to file")


def analyze_complexity(benchmark: list[dict]) -> list[dict]:
    complexities = {
        "bubble": lambda n: n**2,
        "merge": lambda n: n * log2(n),
    }

    groups = {}
    for row in benchmark:
        if row["status"] != "OK":
            continue

        group = (row["algorithm"], row["dataset"])
        groups.setdefault(group, []).append(row)

    analysis = []

    for (algorithm, dataset), rows in groups.items():
        rows = sorted(rows, key=lambda row: row["size"])
        complexity = complexities[algorithm]

        for previous, current in zip(rows, rows[1:]):
            if previous["time"] <= 0 or current["time"] <= 0:
                continue

            analysis.append(
                {
                    "algorithm": algorithm,
                    "dataset": dataset,
                    "sizes": f"{previous['size']} -> {current['size']}",
                    "actual_ratio": current["time"] / previous["time"],
                    "expected_ratio": (
                        complexity(current["size"]) / complexity(previous["size"])
                    ),
                }
            )

    return analysis


def write_analysis(analysis: list[dict], path: Path | str) -> None:
    try:
        path = Path(path)
        with path.open(mode="a", encoding="utf-8") as file:
            file.write("\n")
            file.write("|Algorithm|Dataset|Sizes|Actual ratio|Expected ratio|\n")
            file.write("|---|---|---|---|---|\n")
            for row in analysis:
                file.write(
                    f"|{row['algorithm']}|{row['dataset']}|{row['sizes']}|{row['actual_ratio']}|{row['expected_ratio']}|\n"
                )
    except OSError:
        raise OSError("Cannot write to file")
