import argparse

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'command',
        choices=['benchmark'],
        type=str,
        default='benchmark',
        help='Command to run'
    )
    return 0

if __name__ == '__main__':
    raise SystemExit(main())