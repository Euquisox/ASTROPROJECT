

def JD_to_date(JD)->float:
    tem = JD + 0.5
    F = int(tem)
    I = tem - F
    if F > 2299160:
        A = int((F-1867216.25)/36524.25)
        B = F + 1 + A - int(A/4)
    else:
        A = 1
    C = B + 1524
    D = int((C-122.1)/365.25)
    E = int(365.25 * D)
    G = int((C-E)/30.6001)
    d = C-E+I-int(30.6001*G)
    if G < 13.5:
        mint = G - 1
    else:
        mint = G - 13
    if mint > 2.5:
        y = D - 4716
    else:
        y = D - 4715
    hours = int((d - int(d)) * 24)
    minutes = int(((d - int(d)) * 24) - hours)
    seconds = (((d - int(d)) * 24) - hours) - minutes
    e = list[y, mint, int(d), hours, minutes, seconds]
    return e

#Юлианский календарь в Григорианскую