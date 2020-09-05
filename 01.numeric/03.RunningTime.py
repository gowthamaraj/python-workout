'''
Write a function (run_timing) that asks how long it took for you to run 10 km.
The function continues to ask how long (in minutes) it took for additional runs, until
the user presses Enter. At that point, the function exits—but only after calculating and
displaying the average time that the 10 km runs took.


 *** For example, here’s what the output would look like if the user entered three data
points:

->
Enter 10 km run time: 15
Enter 10 km run time: 20
Enter 10 km run time: 10
Enter 10 km run time: <enter>
Average of 15.0, over 3 runs
->
'''
from functools import reduce

def run_timing() -> None:
    '''function to calculate the average time taken for daily running regime'''

    record = []
    while True:
        time = input('Enter 10 km run time: ')
        if not time: break
        record.append(float(time))
    print(f'Average of {reduce(lambda x,y:(x+y), record)/len(record)}, over {len(record)} runs')


run_timing()

