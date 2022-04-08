import matplotlib.pyplot as plt
from timer_simple import generateTestDataLists, calcTimes
from graph_plotter import plot_times


def reverseFunction(list):
    i = 0
    size = len(list)
    n = int(size / 2)
    while i < n:  # while loop is more efficient in Python than for because for is dynamic
        first = list[i]
        last = list[size - 1 - i]
        list[i] = last
        list[size - 1 - i] = first
        i += 1
    return list


testData = generateTestDataLists()[0]
listSizes = generateTestDataLists()[1]


times = calcTimes(function=reverseFunction, data=testData, repetitions=1000)
print(times)

plot_times(listSizes, times, "my reverse")
