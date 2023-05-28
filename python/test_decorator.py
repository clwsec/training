
""" 1.普通装饰器的运用 """
# def my_decorator(func):
#     print("这个被执行的次数为代码中@装饰的个数，非函数调用的次数，可以将对应@的内如注释后运行查看，和后续部分一起处理")
#     def wrapper(*args):
#         print("Before the function is called.")
#         return func(*args)
#         print("After the function is called.")
#     return wrapper
# @my_decorator
# def say_hello():
#     print("Hello!")
# 调用被装饰的函数
#say_hello()

""" 2.装饰器 缓存函数结果 """
# def cache(func):
#     cached_results = {}
#     print("beg #######:", cached_results)
#     def wrapper(*args):
#         if args in cached_results:
#             return cached_results[args]
#         result = func(*args)
#         cached_results[args] = result
#         print("wrapper #######:", cached_results)
#         return result
#     x = wrapper
#     print(x)
#     print("end #######:", cached_results)
#     return x
# @my_decorator
# def fibonacci(n):
#     if n <= 1:
#         return n    
#     return fibonacci(n-1) + fibonacci(n-2)

# print(fibonacci(5))

""" 3.装饰器的执行顺序 """
def decorator_a(func):
    print('Get in decorator_a')
    def inner_a(*args, **kwargs):
        print('Get in inner_a')
        return func(*args, **kwargs)
    return inner_a

def decorator_b(func):
    print('Get in decorator_b')
    def inner_b(*args, **kwargs):
        print('Get in inner_b')
        return func(*args, **kwargs)
    return inner_b

@decorator_b
@decorator_a
def f(x):
    print('Get in f')
    return x * 2

f(1)
