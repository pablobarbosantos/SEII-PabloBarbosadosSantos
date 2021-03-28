import concurrent.futures
import threading
import time

start = time.perf_counter()

# def do_something():
#     print(f'Sleeping 1 second...')
#     time.sleep(1)
#     print(f'Done Sleeping...')

# t1 = threading.Thread(target=do_something)
# t2 = threading.Thread(target=do_something)

# t1.start()
# t2.start()

# t1.join()
# t2.join()


def do_something(seconds):
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(seconds)
    return f'Done Sleeping...{seconds}'


# threads = []

# for _ in range(10):
#     t = threading.Thread(target=do_something, args=[1.05])
#     t.start()
#     threads.append(t)

# for thread in threads:
#     thread.join()

with concurrent.futures.ThreadPoolExecutor() as executor:

    # f1 = executor.submit(do_something, 1.5)
    # f2 = executor.submit(do_something, 1.5)
    # print(f1.result())
    # print(f2.result())

    secs = [1.5, 1.4, 1.3, 1.2, 1]
    results = executor.map(do_something, secs)

    # resutls = [executor.submit(do_something,1) for _ in range(10)]

    for result in results:
        print(result)

finish = time.perf_counter()
print(f'Finished in {round(finish-start, 4)} second(s)')