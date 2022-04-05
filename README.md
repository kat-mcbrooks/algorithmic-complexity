# Algorithmic Complexity

Workshop and exercises to develop an understanding of algorithmic complexity and data structures, as well as get to grips with writing simple functions in **Python**.

#### Complexity

The amount of time, storage and/or other resources necessary to execute an algorithm. Our aim is to reduce complexity in our algorithms, i.e. make them more efficient. Efficiency is one of the dimensions of a good piece of code.

#### My task

I created a framework to time different algorithms and compare their efficiency. It plots results using matplotlib. First I tested out python in-built functions e.g. sort. Then I wrote my own, trying to be as efficient as possible. I ran the code on varying sizes of arrays.

Not sure why but my calcRunTime seems to be running twice

#### Numpy array vs list efficiency

Generally numpy arrays are more efficient and scalable than python lists. Most processing in numpy is vectorized, meaning the operations can run simultaneously on multiple elements rathen than iterating through each element individually like with a list. Numpy arrays also take up less space than lists (we can check this with getsizeof(list))
HOWEVER, on SMALL lists: List comprehensions are faster than doing the same with numpy as the performance gain from using numpy is not enough to offset the overhead of creating an array.