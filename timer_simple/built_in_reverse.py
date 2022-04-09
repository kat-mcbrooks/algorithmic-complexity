from timer_simple import generateTestDataLists, calcTimes
from graph_plotter import plot_times


def reverseFunction(test_list):
    return test_list.reverse()


testData = generateTestDataLists()[0]
listSizes = generateTestDataLists()[1]
# for l in testData:
#     print(f"list with {len(l)} elements")


times = calcTimes(function=reverseFunction, data=testData, repetitions=10000)
print(times)

plot_times(listSizes, times, "built-in-reverse")
