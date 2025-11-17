import threading
import time


THREAD_COUNT = 5


ranges = [
    [10, 20],
    [1, 5],
    [70, 80],
    [27, 92],
    [0, 16]
]

threads = []

thread_output = [0] * THREAD_COUNT 


def runner(name, count):
    """ Thread running function. """
    ##print(name)
    start = ranges[count][0]
    end =  ranges[count][1]

    thread_output[count] = sum(range(start, end + 1))


for i in range(THREAD_COUNT):

    # Give them a name
    name = f"Thread{i}"

    # Set up the thread object. We're going to run the function called
    # "runner" and pass it two arguments: the thread's name and count:
    t = threading.Thread(target=runner, args=(name, i), daemon=True) 

    # The thread won't start executing until we call `start()`:
    t.start()

    # Keep track of this thread so we can join() it later.
    threads.append(t)

# Join all the threads back up to this, the main thread. The main thread
# will block on the join() call until the thread is complete. If the
# thread is already complete, the join() returns immediately.

for t in threads:
    t.join()

for output in thread_output:
    print(output)

print(sum(thread_output))