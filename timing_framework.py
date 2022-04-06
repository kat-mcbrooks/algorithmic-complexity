import timeit


def calcRunTime(setupCode, codeToRun):
    # number = 1 so it only runs the code once, but repeats 5 times so I can take an average

    runTimes = timeit.repeat(setup=setupCode, stmt=codeToRun, repeat=5, number=1)
    sum = 0
    # add the 5 runtimes together and divide to get the average
    for i in runTimes:
        sum += i
    averageTime = sum / 5
    return averageTime * 100000  # multiply it by 100000 just to make it easier to read
