def sourcetemplate(url):
    def inner(**kwargs):
        if not kwargs:
            return url
        else:
            lst = []
            for k, v in kwargs.items():
                lst.append(f'{k}={v}')
            lst.sort()
            return f'{url}?{"&".join(lst)}'
    return inner


url = 'https://all_for_comfort_life.com'
load = sourcetemplate(url)
print(load(smartphone='iPhone', notebook='huawei', sale=True))
