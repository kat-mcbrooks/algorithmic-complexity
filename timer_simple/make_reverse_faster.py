from timer_simple import generateTestDataLists, calcTimes
from graph_plotter import plot_times

def inefficient_reverse(test_list):
  newlist = []
  i = 0 
  for i < len(test_list):
      newlist.insert(0, test_list[i]) # insert at beginning has O(n). So because this is within a loop over the elements which also has O(n), then the whole function is O(n^2) i.e. quadractic!
      i += 1


testData = generateTestDataLists()[0]
listSizes = generateTestDataLists()[1]

# times = calcTimes(function=myHasDuplicates, data=testData, repetitions=1000)
times = calcTimes(function=inefficient_reverse, data=testData, repetitions=100000)
print(times)

plot_times(listSizes, times, "inefficient reverse")