# Functions package
## Recurrent functions
### Fast power algorithm
Has two realizations:
* by recursion
* by iterations
## Sorting
Has two algorithm of sorting
### Bubble sort
An algorithm of basic sorting. Very simple, but has high complexity: n*n
### Merge sort
An algorithm of quick sorts, has lower complexity then bubble sort, but uses recursion and memory.
## Stack datatype
Realization of stack. Has methods:
* push - pushes one element on the top of stack
* pop - return top element and remove it from stack
* peek - return top element without deleting it
* is_empty - returns 1 if length of stack is 0 and 1 else
* clear - clears stack
* swap - swap two elements in the top
* duplicate - push a copy of top element in the stack
## Generator
Makes lists of integers. Can take seed by creating object and size, start, end by using methods.
Methods:
* random_list - returns list of random numbers
* random_sorted_list - returns sorted list of random numbers
* random_reversed_list - returns reversed list of random numbers
* random_almost_sorted_list - returns sorted list of random elements but makes any replaces
* random_duplicated_list - returns list of random numbers with high count of duplicates
## Benchmark
Makes benchmark, analysis of sorting complexity and writes it to file. Also has an opportunity to print benchmark to console
## Installation 
```commandline
git clone https://github.com/Slava-silang/PyProjectFour.git
uv sync
```

If you want to make benchmark and analysis:

```commandline
uv run python -m functions benchmark
```
PS: also write data to benchmark.md