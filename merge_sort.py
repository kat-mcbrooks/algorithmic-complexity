import matplotlib.pyplot as plt
from timing_framework import calcRunTime


def merge_sort_data(list):
    if len(list) < 2:
        return list
    mid = len(list) // 2
    return merge(left=merge_sort_data(list[:mid]), right=merge_sort_data(list[mid:]))


# create array of integers in increments of 5000 up to 100,000
listSizes = list(range(0, 100000, 5000))
# print(listSizes)
idx = 0
times = []
# create testLists in every size, with elements as integers between 1 and 20. Assign to setupCode.
for size in listSizes:
    setupCode = f"""
from merge_sort import merge_sort_data
import random
testList = random.choices((range(1, 20)), k={size})
"""
    codeToRun = """
merge_sort_data(testList)
"""
    # setupCode should be separated from the sort function so that the timer is based solely on the sort_function itself rather than generating the test arrays
    time = calcRunTime(setupCode, codeToRun)
    print(f"Average time taken to run {size} element list: {time}")
    idx += 1
    times.append(time)

print(times)

plt.plot(listSizes, times)

plt.ylabel("Time taken to run")
plt.xlabel("List size")

plt.show()  # display the graph
plt.savefig("./graphed_results/merge_sort.png")  # savefig, don't show
