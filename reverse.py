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
    n=int(len(arr)/2)
    print(n)
  while i < n:
    print(i)
'''
def reverse_data():
    a = np.random.randint(1000, size=11)
    i=0
    length = len(a)
    n=int(length/2)
    print(a)
    while i < n:
        first = a[i]
        last = a[length-1-i]
        a[i] = last
        a[length-1-i] = first 
        i += 1
    print(a)
reverse_data()
# it = np.nditer(np.random.randint(1000, size=10), flags=['f_index'])
# for x in it:
#   print(x, it.index, end=' ')
