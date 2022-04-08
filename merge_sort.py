import matplotlib.pyplot as plt
from timer_timeit import calcRunTime


def merge_sort_data(list):
    if len(list) < 2:
        return list
    mid = len(list) // 2
    # recursively split the list in two, sorting each half and calling the merge method on the final result
    return merge(left_list_sorted=merge_sort_data(list[:mid]), right_list_sorted=merge_sort_data(list[mid:]))


def merge(left_list_sorted, right_list_sorted):
    left = left_list_sorted
    right = right_list_sorted
    if len(left) == 0:
        return right
    elif len(right) == 0:
        return left
    else:
        merged_result = []
        idx_left = idx_right = 0
        # until merged result contains all elements from both arrays,
        while len(merged_result) < len(left) + len(right):
            if left[idx_left] < right[idx_right]:
                merged_result.append(left[idx_left])
                idx_left += 1
            else:
                merged_result.append(right[idx_right])
                idx_right += 1
            # if we get to the end of either array, the remaining elements of the other array (which are of course, already sorted) can then just be added to the end of the merged_result
            if idx_left == len(left):
                merged_result += right[idx_right:]
                break
            if idx_right == len(right):
                merged_result += left[idx_left:]
                break
        return merged_result


# create array of integers in increments of 5000 up to 100,000
listSizes = list(range(0, 100000, 5000))
print(listSizes)
idx = 0
times = []
# in the setup code, we create testLists in every size, with elements as integers between 1 and 20. setupCode is separated from the algorithm being tested so that the timer is based solely on the algorithm itself rather than generating the test arrays
for size in listSizes:
    setupCode = f"""
from merge_sort import merge_sort_data
import random
testList = random.choices((range(1, 20)), k={size})
"""
    codeToRun = """
merge_sort_data(testList)
"""

    time = calcRunTime(setupCode, codeToRun)
    print(f"Average time taken to run {size} element list: {time}")
    idx += 1
    times.append(time)


print(times)

plt.plot(listSizes, times)
plt.title("merge sort times")
plt.ylabel("Time taken to run")
plt.xlabel("List size")

plt.show()  # display the graph
plt.savefig("./graphed_results/merge_sort.png")  # savefig, don't show
