"""swap two variables in python with and without using temporary variable"""
a = "first_var"
b = "second_var"

a, b = b, a

"""Calculate the time taken by function using decorator in python
and 
Calculate number of times function called using decorator in python"""


import time


def time_func(original):
    def wrapper():
        wrapper.calls += 1
        print(wrapper.calls)
        st = time.time()
        result = original()
        final = time.time() - st
        print(f"took {final} seconds for executing {original.__name__}")
        return result
    wrapper.calls = 0

    return wrapper


@time_func
def printfunc():
    time.sleep(1)
    print("Hello Rio")


printfunc()
printfunc()
