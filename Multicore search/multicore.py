import concurrent.futures
import time


def heuristic_search(total_bits, distance):
    correct_strings = []
    strings = [string for string in range(pow(2, total_bits))]
    while len(strings) > 0:
        current_num = strings.pop(0)
        correct_strings.append(bin(current_num)[2:])
        with concurrent.futures.ProcessPoolExecutor() as executor:
            results = [executor.submit(check_distance, current_num, string, distance) for string in strings]

            strings = []
            for f in concurrent.futures.as_completed(results):
                if f.result() is None:
                    pass
                else:
                    strings.append(f.result())

    final_list = []
    for i in correct_strings:
        while len(i) < total_bits:
            i = '0' + i
        final_list.append(i)
    return sorted(final_list)


def check_distance(current_number, new_number, distance):
    if list(bin(current_number ^ new_number)).count('1') >= distance:
        return new_number


if __name__ == '__main__':
    start = time.perf_counter()
    print(heuristic_search(7, 3))
    finish = time.perf_counter()
    print(f'Total time: {finish - start} second(s)')
