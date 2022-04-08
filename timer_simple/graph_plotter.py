import matplotlib.pyplot as plt
from timer_simple import calcRunTime

plt.plot(listSizes, times)
plt.title("Built-in sort")
plt.ylabel("Time taken to run")
plt.xlabel("List size")

plt.show()  # display the graph
plt.savefig("./graphed_results/built_in_sort.png")  # savefig, don't show
