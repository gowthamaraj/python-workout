"""
 In this exercise, write a generator function whose argument must be iterable. With
each iteration, the generator will return a two-element tuple. The first element in the
tuple will be an integer indicating how many seconds have passed since the previous
iteration. The tuple’s second element will be the next item from the passed argument.
"""
import time

def elapsed_since(data):
    last_time = None
    for item in data:
        current_time = time.perf_counter()
        delta = current_time - (last_time
        or current_time)
        last_time = time.perf_counter()
        yield (delta, item)
        
for t in elapsed_since('abcd'):
    print(t)
    time.sleep(2)