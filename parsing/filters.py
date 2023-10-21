import re
from collections import OrderedDict



def frequency():
    map_unique = {}
    with open('data/final_moscow_oct22_march23.txt', 'r') as file:
        flag = True
        while flag:
            line = file.readline()
            if line != '' and line != '\n':
                for w in line.split(' '):
                    cleaned = re.sub(r'^\W|\W$|\(|\)', '', w).lower()
                    map_unique[cleaned] = map_unique.get(w, 0) + 1
            else:
                flag = False
    map_unique_by_value = {k: v for k, v in sorted(map_unique.items(), key=lambda item: item[1], reverse=True)}
    list_unique_by_value = map_unique_by_value.items()
    with open('data/frequency_final_moscow_oct22_march23.txt', 'a') as file:
        for k, v in list_unique_by_value:
            file.write(k + ',' + str(v) + '\n')
    file.close()
    map_unique_by_key = OrderedDict(sorted(map_unique.items()))
    list_unique_by_key = map_unique_by_key.items()
    with open('data/by_alphabet_frequency_final_moscow_oct22_march23.txt', 'a') as file:
        for k, v in list_unique_by_key:
            file.write(k + ',' + str(v) + '\n')
    file.close()

def filter_resolution_part(solution):
    try_remove_resolution = re.split(r'установил\W?|установил \W?|у с т а н о в и л \W?|у с т а н о в и л\W?', solution, maxsplit=1, flags=re.IGNORECASE)
    if len(try_remove_resolution) == 1:
        return solution.strip()
    return try_remove_resolution[1].strip()


def run():
    with open('data/dataset_mos_removed_resolution_part.txt', 'r') as file:
        flag = True
        with open('data/final_moscow_oct22_march23.txt', 'w') as wfile:
            while flag:
                line = file.readline()
                if line != '' and line != '\n':
                    wfile.write(filter_resolution_part(line) + '\n')
                else:
                    flag = False
    wfile.close()
    file.close()


# run()
frequency()