from timer_simple import generateTestDataLists, calcTimes
from graph_plotter import plot_times
from random import randint

# Time Complexity: O(n)
def sortFunction(test_list):
    size = len(test_list)
    # looks at each element starting from the first (i) and compares it with the element that follows (j)
    for i in range(size):
        for j in range(size - i - 1):
            if test_list[j] > test_list[j + 1]:
                test_list[j], test_list[j + 1] = test_list[j + 1], test_list[j]
    return test_list


testData = generateTestDataLists()[0]
listSizes = generateTestDataLists()[1]

# tried with 10,000 reps but it was really slow, so reduced.
times = calcTimes(function=sortFunction, data=testData, repetitions=10)
print(times)

plot_times(listSizes, times, "my-sort_bubble")
