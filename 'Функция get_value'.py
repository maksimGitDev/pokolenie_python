def get_value(nested_dicts, key):
    res = []

    def rec(nested_dicts):
        try:
            res.append(nested_dicts[key])
        except:
            for i in nested_dicts.values():
                if type(i) == dict:
                    rec(i)
    rec(nested_dicts)
    return res[0]
