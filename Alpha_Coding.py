"""swap two variables in python with and without using temporary variable"""


def swapp(a, b):
    a, b = b, a
    print(a)
    print(b)


a = "first_var"
b = "second_var"

swapp(a, b)

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

'''
One-method-that-accepts the "url" variable-below, parses the query string-parameters (everything-after-the-?), and returns 
the following dictionary/hashmap/hash-with-the-query-string-key-values-as -key-values-in-the-data-structure. 
If-there-are-identical-keys, add-the
#Input:
gid-10"
values to a list. -url "https://api.komodohealth.com/vi/organizations?oid=5&pid=4&pid=7&qid=10"
#Returns (Python-dictionary, not-JSON):
{
"oid": 5,
"pid":[4,7], 
"qid": 10
}
'''

from collections import defaultdict


def urlhandle(str):
    vardict = defaultdict(list)
    abc = (str.split("?")[1]).split("&")
    for i in abc:
        k = i.split("=")[0]
        v = int(i.split("=")[1])
        vardict[k].append(v)
    finaldict = {}
    for i in vardict:
        if len(vardict[i]) == 1:
            finaldict[i] = vardict[i][0]
        else:
            finaldict[i] = vardict[i]
    print(finaldict)


urlhandle("https://api.komodohealth.com/vi/organizations?oid=5&pid=4&pid=7&qid=10")
