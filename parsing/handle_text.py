import re

with open('sol.txt', 'r') as file:
    s = 'РФ , '
    h = re.sub(' ,', ', ', s)
    print(h)
file.close()