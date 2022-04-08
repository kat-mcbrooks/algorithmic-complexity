import matplotlib.pyplot as plt
from timer_timeit import calcRunTime
import numpy as np
import random


def reverse_data(a):
    i = 0
    size = len(a)
    n = int(size / 2)
    while i < n:
        first = a[i]
        last = a[size - 1 - i]
        a[i] = last
        a[size - 1 - i] = first
        i += 1
    return a


# create array of integers in increments of 5000 up to 100,000
listSizes = list(range(0, 100000, 5000))
# print(listSizes)
idx = 0
times = []
# create testLists in every size, with elements as integers between 1 and 20. Assign to setupCode.
for size in listSizes:
    setupCode = f"""
from reverse import reverse_data
import random
testList = random.choices((range(1, 20)), k={size})

"""
    codeToRun = """
reverse_data(testList)
"""
    # setupCode should be separated from the reverse function so that the timer is based solely on the reverse_function itself rather than generating the test arrays
    time = calcRunTime(setupCode, codeToRun)
    print(f"Average time taken to run array {size} element list: {time}")
    idx += 1
    times.append(time)

print(times)

plt.plot(listSizes, times)

plt.ylabel("Time taken to run")
plt.xlabel("List size")

plt.show()  # display the graph
plt.savefig("./graphed_results/reverse.png")  # savefig, don't show
