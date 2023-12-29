def recursive_sum(nested_lists):
    res = []

    def rec(nested_lists):
        if type(nested_lists) == int:
            res.append(nested_lists)
        if type(nested_lists) == list:
            for i in nested_lists:
                rec(i)
    rec(nested_lists)
    return sum(res)
