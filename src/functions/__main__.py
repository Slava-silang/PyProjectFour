import argparse

from .behchmark import make_benchmark, print_benchmark, write_benchmark


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "command",
        choices=["benchmark"],
        type=str,
        default="benchmark",
        help="Command to print benchmark results in console",
    )
    parser.add_argument("--output", type=str, default="benchmark.md")
    args = parser.parse_args()
    if args.command == "benchmark":
        benchmark = make_benchmark()
        print_benchmark(benchmark)
        write_benchmark(path=args.output, benchmark=benchmark)
        print(f"results of benchmark in {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
