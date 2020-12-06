def decorator_func(func):
    def wrapper_func():
        print('X' * 20)
        func()
        print('Y' * 20)

    return wrapper_func

@decorator_func
def say_hello():
    print("laba labas")


#hello = decorator_func(say_hello)
#hello()
say_hello()
