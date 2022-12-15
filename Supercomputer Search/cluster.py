from mpi4py import MPI
import concurrent.futures
from mpi4py.futures import MPIPoolExecutor
import time
comm = MPI.COMM_WORLD
my_rank = comm.Get_rank()
p = comm.Get_size()


def heuristic_search(total_bits, distance):
    # Searches for a hamming distance using a heuristic search
    correct_strings = []
    strings = [string for string in range(pow(2, total_bits))]
    while len(strings) > 0:
        current_num = strings.pop(0)
        correct_strings.append(bin(current_num)[2:])
        executor = MPIPoolExecutor(max_workers=p)
        results = [executor.submit(check_distance, current_num, string, distance) for string in strings]

        # Filters results
        strings = []
        for f in concurrent.futures.as_completed(results):
            if f.result() is None:
                pass
            else:
                strings.append(f.result())

    # formatting for the list
    final_list = []
    for i in correct_strings:
        while len(i) < total_bits:
            i = '0' + i
        final_list.append(i)
    return sorted(final_list)


def check_distance(current_number, new_number, distance):
    # returns strings with desired hamming distance
    if list(bin(current_number ^ new_number)).count('1') >= distance:
        return new_number


if __name__ == '__main__':
    start = time.perf_counter()
    print(heuristic_search(7, 3))
    finish = time.perf_counter()
    print(f'Total time: {finish - start} second(s)')
