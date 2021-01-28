import sys


### The recursive solution is elegant, but very inefficient -
### numbers are recalculated
### shows how to use a list comprehension.

def fibonacci(n):
    return [fib(i) for i in range(1, n + 1)]

def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


### we can make things faster by cacheing previous results

def fibonacci2(n):
    return [fib2(i) for i in range(1, n + 1)]

## shows how to use a dictionary

def fib2(n, cache=None):
    ### set up the cache initially
    if cache == None:
        cache = {}
    ### base case
    if n == 1 or n == 2:
        cache[n] = 1
        return 1
    else:
        if n in cache:
            return cache[n]
        else:
            cache[n] = fib2(n - 1, cache) + fib2(n - 2, cache)
            return cache[n]


### here's an iterative version
## note the multiple assignment.
## shows a for loop

def iterative_fib(n):
    results = [0] * n
    results[0], results[1] = 1, 1
    for i in range(2, n):
        results[i] = results[i - 1] + results[i - 2]
    return results


if __name__ == '__main__':
    if len(sys.argv) < 1 :
        print("Usage: fibonacci {number}")
        sys.exit(-1)
    else :
        n = int(sys.argv[1])
        print("Version 1: %s" % fibonacci(n)) ## note the use of '%' as as format operator
        print("Version 2: %s" % fibonacci2(n))
        print("Version 3: %s" % iterative_fib(n))