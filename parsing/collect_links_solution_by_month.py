import calendar
from datetime import date
from dateutil import relativedelta
from requests_html import HTMLSession

host = 'https://sudact.ru/arbitral/doc/'
arbitral_region_moscow = '1027'
arbitral_region_spb = '1029'
arbitral_court = '%D0%90%D0%A1+%D0%B3%D0%BE%D1%80%D0%BE%D0%B4%D0%B0+%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D1%8B'
selector = '#docListContainer > .results > li > h4 > b > a'
params_map = {
    'txt': '?arbitral-txt=',
    'case_doc': '&arbitral-case_doc=',
    'lawchunkinfo': '&arbitral-lawchunkinfo=',
    'date_from': '&arbitral-date_from=',
    'date_to': '&arbitral-date_to=',
    'region': '&arbitral-region=',
    'court': '&arbitral-court=',
    'judge': '&arbitral-judge='
}

session = HTMLSession()


def collect_links_solution_by_month(start_day, num_months_frward, params_arg):
    for i in range(num_months_frward):
        arbitral_date_from = start_day.strftime("%d.%m.%Y")
        month = calendar.monthrange(start_day.year, start_day.month)
        arbitral_date_to = date(start_day.year, start_day.month, month[1]).strftime("%d.%m.%Y")
        params = params_arg['txt'] + \
                 params_arg['case_doc'] + \
                 params_arg['lawchunkinfo'] + \
                 params_arg['date_from'] + arbitral_date_from \
                 + params_arg['date_to'] + arbitral_date_to \
                 + params_arg['region'] + arbitral_region_spb \
                 + params_arg['court'] + arbitral_court \
                 + params_arg['judge']
        while True:
            response = get_rendered(host + params)
            list_html_elements = get_html_solutions(response, selector)
            list_link_str = get_link_solutions(list_html_elements)
            with open('data/links_solutions_spb.txt', 'r') as rfile:
                set_links = set(rfile.readlines())
            rfile.close()
            for link in list_link_str:
                link = link.split('/?')[0] + '\n'
                if link not in set_links:
                    with open('data/links_solutions_spb.txt', 'a') as file:
                        file.write(link)
                    file.close()
            next_page = response.html.find('.page-next > a', first=True)
            if next_page is None:
                break
            else:
                params = next_page.attrs['href']

        start_day = start_day + relativedelta.relativedelta(months=1)


def get_rendered(req):
    response = session.get(req, verify=False)
    response.html.render(sleep=2, timeout=20)
    return response


def get_html_solutions(response, path):
    return response.html.find(path)


def get_link_solutions(list_link_element):
    if type(list_link_element) == list:
        res = []
        for el in list_link_element:
            if 'резолютивная часть решения' not in el.full_text.lower():
                res.append(el.attrs['href'])
        return res


collect_links_solution_by_month(date(2022, 10, 1), 1, params_map)
