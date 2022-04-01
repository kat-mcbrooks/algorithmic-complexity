import timeit

import time
# from numpy import random, sort
# import numpy as np

# code snippet to be executed only once
smallest_array = '''
import numpy as np

a = np.random.randint(1000, size=10)

'''
biggest_array = '''
import numpy as np

a = np.random.randint(1000, size=10000)

'''
sort_function = '''
def sort_data():
    a.sort()
'''

def calcRunTime(setupCode, codeToRun):
    times = timeit.repeat(setup=setupCode, stmt=codeToRun,  repeat=5000, number = 1)
    sum = 0
    for i in times: 
        sum += i
    averageTime = sum / 5000
    return averageTime * 100
   

a = calcRunTime(sort_function, smallest_array)
print(f"Average time taken to run smallest array: {a}")
b = calcRunTime(sort_function, biggest_array)
print(f"Average time taken to run biggest array: {b}")

# # test lists/arrays of random numbers
# a = random.randint(1000, size=(10))
# # b = random.randint(1000, size=(100))
# # c = random.randint(1000, size=(1000))
# # d = random.randint(1000, size=(5000))
# # e = random.randint(1000, size=(10000))
# # f = random.randint(1000, size=(15000))
# g = random.randint(1000, size=(20000))


# def timer(func, test_data):
#     print("starting timer...")
#     start_time = time.perf_counter()
#     print(test_data)
#     func(test_data)
#     print(test_data)
#     end_time = time.perf_counter()
#     time_elapsed = end_time - start_time  # in fractional seconds
#     print(f"Time taken to run: {time_elapsed}")


# def reverse_data(test_data):
#     np.flip(test_data)


# timer(sort_data, a)
# timer(sort_data, g)
# timer(reverse_data, a)
# timer(reverse_data, g)
# # timer(b)
# timer(c)
# timer(d)
# timer(e)
# timer(f)
# timer(g)
