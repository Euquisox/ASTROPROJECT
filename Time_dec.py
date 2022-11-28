def time_dec(t: str) -> float:
    t = t.split(":")
    a = float(t[0])
    b = float(t[1])
    c = float(t[2])
    d = (b / 60)
    e = (c / 3600)
    k = a + d + e
    return k

#Время из обычной в десятичную в часах