from datetime import datetime, date


def date_formatter(counry_code):
    my_dict = {'ru': '%d.%m.%Y',
               'us': '%m-%d-%Y',
               'ca': '%Y-%m-%d',
               'br': '%d/%m/%Y',
               'fr': '%d.%m.%Y',
               'pt': '%d-%m-%Y'}

    def inner(today, d=my_dict[counry_code]):
        return today.strftime(d)

    return inner


date_ru = date_formatter('us')
today = date(2022, 1, 25)
print(date_ru(today))
