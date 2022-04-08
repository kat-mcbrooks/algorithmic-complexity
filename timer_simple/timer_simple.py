import time
import random


def generateLists():
    # create list of integers in increments of 5000 up to 100,000
    listSizes = list(range(0, 100000, 5000))
    # print(listSizes)
    testLists = []
    # create testLists in every size, with elements as integers between 1 and 20.
    for size in listSizes:
        testList = random.choices((range(1, 20)), k=size)
        testLists.append(testList)
    return testLists


def calcRunTime(codeToRun, testList):
    start_time = time.perf_counter()
    codeToRun(testList)
    finish_time = time.perf_counter()
    time_elapsed = finish_time - start_time
    return time_elapsed


def calcTimes(function, data):
    times = []
    for l in data:
        print(f"list with {len(l)} elements")  # this is the right order
    data.sort(key=len)
    for i in range(len(data)):
        print(f"list with {len(data[i])} elements")  # but this is wrong..
        time = calcRunTime(codeToRun=function, testList=l)
        print(f"Average time taken to run {len(data[i])} element list: {time}")
        times.append(time)
    return times
