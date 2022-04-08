import matplotlib.pyplot as plt
from timer_timeit import calcRunTime


def bubble_sort_data(list):
    # sorted = True # this will tell the function to stop
    size = len(list)
    for i in range(size):
        for j in range(size - i - 1):
            if list[j] > list[j + 1]:
                # reassigning simultaneously (swapping their order in the array)
                list[j], list[j + 1] = list[j + 1], list[j]

    return list


# create array of integers in increments of 5000 up to 100,000
listSizes = list(range(0, 100000, 5000))
# print(listSizes)
idx = 0
times = []
# create testLists in every size, with elements as integers between 1 and 20. Assign to setupCode.
for size in listSizes:
    setupCode = f"""
from bubble_sort import bubble_sort_data
import random
testList = random.choices((range(1, 20)), k={size})
"""
    codeToRun = """
bubble_sort_data(testList)
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
plt.savefig("./graphed_results/bubble_sort.png")  # savefig, don't show
