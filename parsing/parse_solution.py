from requests_html import HTMLSession
from bs4 import BeautifulSoup

import collect_links_solution_by_month as fool

host = 'https://sudact.ru'
params = '/arbitral/doc/3fWgpz207oN3/?arbitral-txt=&arbitral-case_doc=&arbitral-lawchunkinfo=&arbitral-date_from=01.10.2022&arbitral-date_to=31.10.2022&arbitral-region=1027&arbitral-court=%D0%90%D0%A1+%D0%B3%D0%BE%D1%80%D0%BE%D0%B4%D0%B0+%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D1%8B&arbitral-judge=&_=1696531254209'
selector = 'h-col1-inner3'

session = HTMLSession()


def pull_solution():
    response = session.get(host + params, verify=False)
    response.html.render()
    html = response.text
    soup = BeautifulSoup(response.html.raw_html, "html.parser")
    c = soup.find(class_=selector)
    print(type(c))


pull_solution()
