# Algorithmic Complexity

Workshop and exercises to develop an understanding of algorithmic complexity and data structures, as well as get to grips with writing simple functions in **Python**.

#### Complexity

The amount of time, storage and/or other resources necessary to execute an algorithm. Our aim is to reduce complexity in our algorithms, i.e. make them more efficient. Efficiency is one of the dimensions of a good piece of code.

### Results

My reverse function is much slower than built-in reverse but both seem to be linear in complexity.

### My approach

I created a framework to time different algorithms and compare their efficiency. It plots results using matplotlib. First I tested out python in-built functions e.g. sort. Then I wrote my own, trying to be as efficient as possible. Each function is contained in its own file, so run each function file to test its time.

To run the code on varying sizes of python lists, I created a listSizes list, which is looped over within the setup code to create a testList with 0 elements, then with 5000 elements, then with 10000 elements etc:

```
listSizes =
[0, 5000, 10000, 15000, 20000, 25000, 30000, 35000, 40000, 45000, 50000, 55000, 60000, 65000, 70000, 75000, 80000, 85000, 90000, 95000]
```

So the codeToRun will run on 20 different lists increasing in size by increments of 5000.

??? Not sure why but all my self-written algorithm files seems to be running twice and so I get two lines on the graphs. The built-in files only run once.
??? Maybe try going back to using perf counter?!

#### To time a function:

Each function to be timed is contained in a separate file. So to time it, run the file e.g.

```
$ python3 built_in_sort.py
```

#### Notes: Numpy array vs list efficiency

Generally numpy arrays are more efficient and scalable than python lists. Most processing in numpy is vectorized, meaning the operations can run simultaneously on multiple elements rathen than iterating through each element individually like with a list. Numpy arrays also take up less space than lists (we can check this with getsizeof(list))
HOWEVER, on SMALL lists: List comprehensions are faster than doing the same with numpy as the performance gain from using numpy is not enough to offset the overhead of creating an array.
