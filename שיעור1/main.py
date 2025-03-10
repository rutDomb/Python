import time



def RunningTime(func):
    def wrapper(*args,**kwargs):
        start=time.time()
        func(*args,**kwargs)
        end = time.time()
        length = end - start
        print(length)
    return wrapper


dictionary={}
def cache(func):
    def wrapper(*args, **kwargs):
        key = (args, frozenset(kwargs.items()))
        if key in dictionary:
            print(f"Result from cache: {dictionary[key]}")
            return dictionary[key]
        else:
            result = func(*args, **kwargs)
            dictionary[key] = result
            print(f"Calculated result: {result}")
            return result
    return wrapper

@RunningTime
def say_hello():
    print("hi ruti")
    x=50+60
    while(x>0):
       print(100)
       x=x-10

@cache
def Fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return Fibonacci(n - 1) + Fibonacci(n - 2)



say_hello()
Fibonacci(30)