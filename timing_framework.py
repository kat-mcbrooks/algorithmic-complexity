import timeit

import time
# from numpy import random, sort
# import numpy as np

# code snippet to be executed only once
smallest_array = '''
import numpy as np

a = np.random.randint(1000, size=10)

'''

codeToExecute = '''
def sort_data():
    a.sort()
'''

def timer(codeToRun, setupCode):
    times_50k_reps = timeit.repeat(
    setup=smallest_array, stmt=codeToExecute, repeat=50000
)
    sum = 0
    for i in times_50k_reps: 
        sum += i
    averageTime = sum / 50000
    return averageTime

print(f"Time taken to run smallest array: {averageTime}")


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
