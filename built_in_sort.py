import matplotlib.pyplot as plt
from timing_framework import calcRunTime
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
sort_function = '''
def sort_data():
    a.sort()
'''

a = calcRunTime(smallest_array, sort_function)
print(f"Average time taken to run smallest array: {a}")
b = calcRunTime(smaller_array, sort_function)
print(f"Average time taken to run smaller array: {b}")
e = calcRunTime(middle_array, sort_function)
print(f"Average time taken to run middle array: {e}")
f = calcRunTime(bigger_array, sort_function)
print(f"Average time taken to run bigger array: {f}")
g = calcRunTime( biggest_array, sort_function)
print(f"Average time taken to run biggest array: {g}")

plt.plot([10, 1000, 50000, 75000, 100000], [a, b, e, f, g])

plt.ylabel('Time taken to run')
plt.xlabel('Array size')

plt.show() #display the graph
plt.savefig("built_in_sort.png")  #savefig, don't show