def date_to_jd(year: int, month: int, day: int, time=0) -> float:
    a = int((14 - month)/12)
    y = year + 4800 - a
    m = month + 12*a - 3
    JDN = day+int((153 * m+2)/5) + 365*y + int(y/4) - int(y/100)+ int(y/400)-32045
    hours = int(time)
    min = (time - hours)*60
    minutes = int(min)
    s = min - minutes
    sec = s*60
    JD = JDN + (hours-12)/24 + minutes/1440 + sec/86400
    return JD

#Григорианский календарь в Юлианскую