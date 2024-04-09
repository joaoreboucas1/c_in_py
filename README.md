# C in Python

A small example project on how to use C code in Python to speed up CPU-bound operations.

## The Problem

We want to implement the (prime-counting function)[https://en.wikipedia.org/wiki/Prime-counting_function]. A simple Python implementation is given in `prime_count.py`, which iterates over all numbers and checks if each of them is prime. The complexity of this specific implementation is `O(n*sqrt(n))`. For `n = 1000000`, the program already takes 2.5 seconds. Of course, we can optimize the implementation, but an alternative is to port the "math-heavy" part of the code to a low-level language such as C.

## Porting to C

`prime_count.c` is the C version of the same algorithm. Opening the codes side-by-side, they are very similar. We can compile and run the code normally with the command:

```console
gcc -o prime_count prime_count.c
./prime_count
```

For `n = 1000000`, the code takes 0.3 seconds, almost 10 times faster!

## Compiling C Code as Shared Library

Our main goal is to dynamically link the C code in Python, which can be done using the `ctypes.cdll.LoadLibrary()` function. To do that, we must compile the C code as a (shared library)[https://en.wikipedia.org/wiki/Shared_library]:

```console
gcc -c -fpic prime_count.c
```

This command should create an object file named `prime_count.o`. To make it a shared library, do the command:

```console
gcc -shared -o prime_count.so prime_count.o
```

The shared library `prime_count.so` can be dynamically linked to other programs, including Python programs!

## Using the Shared Library in Python

Finally, to import the shared library in Python, we use:

```python
import ctypes
library = ctypes.cdll.LoadLibrary("./prime_count.so")
```

Python reuses the library syntax with shared libraries as well, and it is able to read the names included from the shared library. In principle, we could simply do:

```python
count = library.prime_count(100)
print(count)
```

But C code must know the types in advance, and Python may pass data to the C code as a wrong type. Before using functionality from shared libraries, it's good to provide the argument types:

```python
library.prime_count.argtypes = [ctypes.float, ] # This makes Python cast the numbers to float before passing them to the function
count = library.prime_count(100)
print(count) # 25
```

## Benchmarking

In my machine, the Python version is 6.8x faster!