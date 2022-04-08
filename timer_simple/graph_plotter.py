import matplotlib.pyplot as plt


def plot_times(listSizes, times, functionName):
    plt.plot(listSizes, times)
    plt.title(f"{functionName}")
    plt.ylabel("Time taken to run")
    plt.xlabel("List size")

    plt.show()  # display the graph does not seem to work in vscode
    plt.savefig(f"./timer_simple/graphed_times/{functionName}.png")  # savefig, don't show
