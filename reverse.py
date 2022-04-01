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
def sort_data():
    a.sort()
'''

it = np.nditer(np.random.randint(1000, size=10), flags=['f_index'])
for x in it:
  print(x, it.index, end=' ')