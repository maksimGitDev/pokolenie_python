def custom_isinstance(objects, typeinfo):
    res = []
    for i in objects:
        if isinstance(i, typeinfo):
            res.append(i)
    return len(res)
