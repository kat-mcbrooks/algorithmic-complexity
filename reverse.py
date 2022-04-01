import matplotlib.pyplot as plt
from timing_framework import calcRunTime
import numpy as np
# code snippet to be executed only once
smallest_array = '''
import numpy as np

a = np.random.randint(1000, size=10)

'''
smaller_array = '''
import numpy as np

a = np.random.randint(1000, size=1000)

'''
middle_array = '''
import numpy as np

a = np.random.randint(1000, size=50000)

'''
bigger_array = '''
import numpy as np

a = np.random.randint(1000, size=75000)

'''
biggest_array = '''
import numpy as np

a = np.random.randint(1000, size=100000)

'''
reverse_function = '''
def reverse_data():
    i=0
    size = len(a)
    n=int(length/2)
    while i < n:
        first = a[i]
        last = a[size-1-i]
        a[i] = last
        a[size-1-i] = first 
        i += 1
    return a
'''

a = calcRunTime(smallest_array, reverse_function)
print(f"Average time taken to run smallest array: {a}")
b = calcRunTime(smaller_array, reverse_function)
print(f"Average time taken to run smaller array: {b}")
e = calcRunTime(middle_array, reverse_function)
print(f"Average time taken to run middle array: {e}")
f = calcRunTime(bigger_array, reverse_function)
print(f"Average time taken to run bigger array: {f}")
g = calcRunTime(biggest_array, reverse_function)
print(f"Average time taken to run biggest array: {g}")

plt.plot([10, 1000, 50000, 75000, 100000], [a, b, e, f, g])

plt.ylabel('Time taken to run')
plt.xlabel('Array size')

plt.show() #display the graph
plt.savefig("./graphed_results/reverse.png")  #savefig, don't show

# def reverse_data():
#     a = np.random.randint(1000, size=11)
#     i=0
#     size = len(a)
#     n=int(length/2)
#     print(a)
#     while i < n:
#         first = a[i]
#         last = a[size-1-i]
#         a[i] = last
#         a[size-1-i] = first 
#         i += 1
#     print(a)
# reverse_data()
# it = np.nditer(np.random.randint(1000, size=10), flags=['f_index'])
# for x in it:
#   print(x, it.index, end=' ')
