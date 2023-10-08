import re


def frequency():
    map_raw_unique = {}
    for w in drop_resolution.split(' '):
        cleaned = re.sub(r'^\W|\W$|\(|\)', '', w)
        map_raw_unique[cleaned] = map_raw_unique.get(w, 0) + 1
    print(map_raw_unique)


def filter_resolution_part(solution):
    try_remove_resolution = re.split(r'установил\W?|установил \W?|у с т а н о в и л \W?|у с т а н о в и л\W?', solution, maxsplit=1, flags=re.IGNORECASE)
    if len(try_remove_resolution) == 1:
        return solution.strip()
    return try_remove_resolution[1].strip()


def run():
    with open('data/dataset_mos_removed_resolution_part.txt', 'r') as file:
        flag = True
        with open('data/test2.txt', 'w') as wfile:
            while flag:
                line = file.readline()
                if line != '' and line != '\n':
                    wfile.write(filter_resolution_part(line) + '\n')
                else:
                    flag = False
    wfile.close()
    file.close()


run()
