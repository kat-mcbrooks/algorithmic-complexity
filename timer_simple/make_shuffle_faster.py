from timer_simple import generateTestDataLists, calcTimes
from graph_plotter import plot_times
from random import randint


def inefficientShuffle(test_list):
    """
    Quadratic, O(n^2) because .pop has O(n) because it has to move all the elements after it deletes one at an arbitrary index. (nb that pop on the last element is actually O(1)). And this pop is nested within a while loop which is also O(n), making the algorithm as a whole O(n^2)
    """
    newlist = []
    while len(test_list) > 0:
        random_idx = randint(0, len(test_list) - 1)
        newlist.append(test_list[random_idx])
        test_list.pop(random_idx)
    # print(newlist)
    return newlist


# Time Complexity: O(n), vs using a nested loop which would be O(n2)
def improvedShuffle(test_list):
    """
    start at last element of list, working backwards from last element of list until we get to first element at i=0. Swap the current element with anothe element at a randomly selected index.
    """
    i = len(test_list) - 1
    while i >= 0:
        random_idx = randint(0, i)  # get random integer between 0 and the index of the current element to be shuffled
        current_el = test_list[i]
        random_el = test_list[random_idx]
        test_list[random_idx], test_list[i] = current_el, random_el  # swap them
        i -= 1
    # print(test_list)
    return test_list


# improvedShuffle([1, 2, 3, 4, 5, 6, 7])  # testing that it works

testData = generateTestDataLists()[0]
listSizes = generateTestDataLists()[1]

# tried with 10,000 reps but it was really slow, so reduced.
times = calcTimes(function=improvedShuffle, data=testData, repetitions=20)
plot_times(listSizes, times, "improvedShuffle")
# times = calcTimes(function=inefficientShuffle, data=testData, repetitions=20)
# plot_times(listSizes, times, "inefficient shuffle")
print(times)
