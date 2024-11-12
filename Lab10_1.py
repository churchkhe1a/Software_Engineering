from functools import lru_cache

@lru_cache(None)
def fiboonacci(n):
    if n ==0:
        return 0
    elif n == 1:
        return 1
    return fiboonacci(n-1) + fiboonacci(n-2)

if __name__ == '__main__':
    print(fiboonacci(100))
