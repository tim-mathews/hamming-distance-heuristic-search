import time


def heuristic_search(total_bits, distance):
    # Searches for a hamming distance using a heuristic search
    correct_strings = []
    strings = [string for string in range(pow(2, total_bits))]
    while len(strings) > 0:
        current_num = strings.pop(0)
        correct_strings.append(bin(current_num)[2:])
        strings = [i for i in strings if list(bin(current_num ^ i)).count('1') >= distance]

    # formatting for the list
    final_list = []
    for i in correct_strings:
        while len(i) < total_bits:
            i = '0' + i
        final_list.append(i)
    return final_list


start = time.perf_counter()
length = int(input("Enter length of strings: "))
search_distance = int(input("Enter desired hamming distance: "))
print(heuristic_search(length, search_distance))
finish = time.perf_counter()
print(f'Total time: {finish-start} second(s)')
