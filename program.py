def cache(func):
    cache_dic = {}
    def wrapper (*args):
        if args in cache_dic:
            return cache_dic[args]
        result = func(*args)
        cache_dic[args] = result
        return result
    return wrapper

@cache
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

print(fib(5))