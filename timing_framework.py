import timeit


def calcRunTime(setupCode, codeToRun):
    # number = 1 so it only runs the code once, but repeats 10 times so I can take an average
    runTimes = timeit.repeat(setup=setupCode, stmt=codeToRun, repeat=10, number=1)
    print(sum(runTimes) / 10)
    return sum(runTimes) / 10
