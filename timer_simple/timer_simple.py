import time
import random


def generateTestDataLists():
    # create list of integers in increments of 5000 up to 100,000
    listSizes = list(range(0, 100000, 5000))
    # print(listSizes)
    testLists = []
    # create testLists in every size, with elements as integers between 1 and 20.
    for size in listSizes:
        testList = random.choices((range(1, 20)), k=size)
        testLists.append(testList)
    return [testLists, listSizes]


def calcRunTime(codeToRun, testList):
    i = 0
    total = 0
    while i < 10000:
        start_time = time.perf_counter()
        codeToRun(testList)
        finish_time = time.perf_counter()
        time_elapsed = finish_time - start_time
        total += time_elapsed
        i += 1
    averageTimeElapsed = total / 10000
    return averageTimeElapsed


def calcTimes(function, data):
    times = []
    for l in data:
        time = calcRunTime(codeToRun=function, testList=l)
        print(f"Average time taken to run with {len(l)} element list: {time}")
        times.append(time)
    return times
