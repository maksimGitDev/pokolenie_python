def get_all_values(nested_dicts, key):
    res = []

    def rec(nested_dicts):
        try:
            res.append(nested_dicts[key])
        except:
            for i in nested_dicts.values():
                if type(i) == dict:
                    rec(i)
    rec(nested_dicts)
    return set(res)


my_dict = {
    'Arthur': {'hobby': 'videogames', 'drink': 'cacao'},
    'Timur': {'hobby': 'math'},
    'Dima': {
        'hobby': 'CS',
        'sister':
        {
            'name': 'Anna',
            'hobby': 'TV',
            'age': 14
        }
    }
}

result = get_all_values(my_dict, 'hobby')
print(*sorted(result))
