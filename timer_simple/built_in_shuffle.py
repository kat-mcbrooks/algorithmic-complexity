from timer_simple import generateTestDataLists, calcTimes
from graph_plotter import plot_times
import random


def shuffleFunction(list):
    return random.shuffle(list)


testData = generateTestDataLists()[0]
listSizes = generateTestDataLists()[1]

# tried with 10,000 reps but it was really slow, so reduced.
times = calcTimes(function=shuffleFunction, data=testData, repetitions=1000)
print(times)

plot_times(listSizes, times, "built-in-shuffle")
