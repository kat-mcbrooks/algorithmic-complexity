import matplotlib.pyplot as plt
from timing_framework import calcRunTime
import numpy as np
import random

# create list of integers in increments of 5000 up to 100,000
listSizes = list(range(0, 100000, 5000))
# print(listSizes)
idx = 0
times = []
# create testLists in every size, with elements as integers between 1 and 20. Assign to setupCode.
for size in listSizes:
    testList = random.choices((range(1, 20)), k=size)
    setupCode = f"""
{testList}

"""
    reverse_function = f"""
{testList}.reverse()
"""
    # setupCode should be separated from the reverse function so that the timer is based solely on the reverse_function itself rather than generating the test arrays
    time = calcRunTime(setupCode, reverse_function)
    print(f"Average time taken to run array {size} element list: {time}")
    idx += 1
    times.append(time)

print(times)

plt.plot(listSizes, times)
plt.title("Built-in reverse")
plt.ylabel("Time taken to run")
plt.xlabel("List size")

plt.show()  # display the graph
plt.savefig("./graphed_results/built_in_reverse.png")  # savefig, don't show

#
