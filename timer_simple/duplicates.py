from numpy import true_divide
from timer_simple import generateTestDataLists, calcTimes
from graph_plotter import plot_times


def hasDuplicates(test_list):
    i = 0
    while i < len(test_list):
        j = i + 1
        while j < len(test_list):
            if test_list[i] == test_list[j]:
                return True
            j += 1
        i += 1
    return False


def myHasDuplicates(
    test_list,
):  # written with aim of reducing time complexity compared to the above. Graph suggests O(n) linear
    i = 0
    while i < len(test_list):
        new_list = [
            num for num in test_list if num != test_list[i]
        ]  # returns a list excluding any elements that match the current element. If no duplicates, it will be a list with one less element than the original list

        if len(test_list) - len(new_list) > 1:
            return True  # this breaks the while loop. Once any duplicate is found, we do not need to carry out any more checks
        test_list = new_list
    return False


testData = generateTestDataLists()[0]
listSizes = generateTestDataLists()[1]

# times = calcTimes(function=myHasDuplicates, data=testData, repetitions=1000)
times = calcTimes(function=hasDuplicates, data=testData, repetitions=100000)
print(times)

plot_times(listSizes, times, "hasDuplicates")


# check to make sure my algorithm actually does what it is supposed to!
# myHasDuplicates([10, 10, 1, 0, 1, 3, 4])  # should return True (yes, i tested it with print)
# myHasDuplicates([10, 9, 1, 0, 2, 3, 4])  # should return False
