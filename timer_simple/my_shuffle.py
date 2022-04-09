from timer_simple import generateTestDataLists, calcTimes
from graph_plotter import plot_times
from random import randint

# Time Complexity: O(n), vs using a nested loop which would be O(n2)
def shuffleFunction(test_list):
    i = len(test_list) - 1  # start at last element of list
    # shuffle one element at a time, working backwards from last element of list until we get to first element at i=0
    while i >= 0:
        random_idx = randint(0, i)  # get random integer between 0 and the index of the current element to be shuffled
        test_list[i], test_list[random_idx] = (
            test_list[random_idx],
            test_list[i],
        )  # swap the randomly chosen element with the current element
        i -= 1
    return test_list


testData = generateTestDataLists()[0]
listSizes = generateTestDataLists()[1]

# tried with 10,000 reps but it was really slow, so reduced.
times = calcTimes(function=shuffleFunction, data=testData, repetitions=20)
print(times)

plot_times(listSizes, times, "my-shuffle")
