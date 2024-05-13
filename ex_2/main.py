import time
from multiprocessing import Pool, cpu_count


def factorize_single_number(number):
    res = set()
    for i in range(1, number % 2 + int(number / 2)):
        if not (number % i):
            res.add(i)
            res.add(int(number / i))
    return sorted(list(res))


def factorize(*number):
    res = []
    for i in number:
        res.append(factorize_single_number(i))
    return res


def factorize_use_processes(*number):
    res = []
    with Pool(processes=cpu_count()) as pool:
        res = pool.map(factorize_single_number, number)
    return res


if __name__ == '__main__':
    start = time.perf_counter()
    factorize(128, 255, 99999, 10651060, 10651060, 10651060, 10651060, 10651060, 10651060, 10651060, 10651060, 10651060, 10651060)
    stop = time.perf_counter()
    print(stop - start)

    start = time.perf_counter()
    factorize_use_processes(128, 255, 99999, 10651060, 10651060, 10651060, 10651060, 10651060, 10651060, 10651060, 10651060, 10651060, 10651060)
    stop = time.perf_counter()
    print(stop - start)

    # assert a == [1, 2, 4, 8, 16, 32, 64, 128]
    # assert b == [1, 3, 5, 15, 17, 51, 85, 255]
    # assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
    # assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106,
    #              1521580, 2130212, 2662765, 5325530, 10651060]
