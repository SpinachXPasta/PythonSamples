def ft(ar):
    try:
        if len(ar) <= 1 and str(type(ar)) != "<class 'list'>":
            return [ar]
    except TypeError:
        return [ar]
    out = []
    for i in ar:
        out += ft(i)
    return out
