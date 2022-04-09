from timer_simple import generateTestDataLists, calcTimes
from graph_plotter import plot_times


def inefficient_reverse(test_list):
    newlist = []
    for i in test_list:
        newlist.insert(
            0, test_list[i]
        )  # insert at beginning has O(n). So because this is within a loop over the elements which also has O(n), then the whole function is O(n^2) i.e. quadractic (see graph)!
    return newlist


def improved_reverse(test_list):
    if len(test_list) == 0:
        return test_list
    newlist = []
    midpoint = len(test_list) // 2
    last_idx = len(test_list) - 1
    i = 0
    while i < len(test_list):
        # print(i)
        # print(last_idx)
        # print(last_idx - i)
        # print(test_list[last_idx - i])
        newlist.append(test_list[last_idx - i])
        i += 1
    return newlist


# improved_reverse([1, 2, 3, 4, 5, 6])
testData = generateTestDataLists()[0]
listSizes = generateTestDataLists()[1]

times = calcTimes(function=improved_reverse, data=testData, repetitions=50)
# times = calcTimes(function=inefficient_reverse, data=testData, repetitions=10)
print(times)

# plot_times(listSizes, times, "inefficient reverse")
plot_times(listSizes, times, "improved reverse")
