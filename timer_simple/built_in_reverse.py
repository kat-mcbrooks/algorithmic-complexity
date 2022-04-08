import matplotlib.pyplot as plt
from timer_simple import generateLists, calcTimes


def reverseFunction(list):
    return list.reverse()


testData = generateLists()
# for l in testData:
#     print(f"list with {len(l)} elements")


times = calcTimes(function=reverseFunction, data=testData)
print(times)
