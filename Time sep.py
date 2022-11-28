def time_sep(str_sep: float) -> str:
    a = int(str_sep)
    d = str_sep - a
    e = d * 60
    r = int(e)
    s = e - r
    g = (s * 60)
    str_time = str(a) + ":" + str(r) + ":" + str(g)
    return str_time

#Время из десятичной в часах в обычную
