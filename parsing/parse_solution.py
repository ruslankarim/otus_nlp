import re

from requests_html import HTMLSession
from bs4 import BeautifulSoup

host = 'https://sudact.ru'
params = '/arbitral/doc/3fWgpz207oN3/?arbitral-txt=&arbitral-case_doc=&arbitral-lawchunkinfo=&arbitral-date_from=01.10.2022&arbitral-date_to=31.10.2022&arbitral-region=1027&arbitral-court=%D0%90%D0%A1+%D0%B3%D0%BE%D1%80%D0%BE%D0%B4%D0%B0+%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D1%8B&arbitral-judge=&_=1696531254209'
selector = 'h-col1-inner3'

session = HTMLSession()


def pull_solution():
    with open('parsing/links_solutions.txt', 'r') as file:
        with open(f'parsing/dataset.txt', 'r') as dataset:
            lenn = len(dataset.readlines())
            dataset.close()
        content = file.readlines()[lenn + 1:3477]
        for line in content:
            response = session.get(host + line, verify=False)
            response.html.render(sleep = 2, timeout = 20)
            soup = BeautifulSoup(response.html.raw_html, "html.parser")
            c = soup.find(class_=selector)
            solution = ' '.join(c.get_text(strip=True, separator=' ').split(' Суд: АС города Москвы ')[0].split())
            avoid_dot = re.sub(' \. ', '. ', solution)
            avoid_comma = re.sub(' , ', ', ', avoid_dot)
            with open(f'data/dataset.txt', 'a') as wfile:
                wfile.write(avoid_comma + '\n')
                wfile.close()
        file.close()

pull_solution()
