def time_dec(t: str) -> float:
    t = t.split(":")
    a = float(t[0])
    b = float(t[1])
    c = float(t[2])
    d = (b / 60)
    e = (c / 3600)
    k = a + d + e
    return k



def time_sep(str_sep:float)-> str:
    a = int(str_sep)
    d = str_sep - a
    e = d * 60
    r = int(e)
    s = e - r
    g = (s * 60)
    str_time = str(a) + ":" + str(r) + ":" + str(g)
    return str_time



def date_to_jd(year:int,month:int, day:int,time=0)->float:
    a = int ((14 - month)/12)
    y = year + 4800 - a
    m = month + 12*a -3
    JDN = day+int((153 * m+2)/5) + 365*y + int(y/4) - int(y/100)+ int(y/400)-32045
    hours = int(time)
    min = (time - hours)*60
    minutes = int(min)
    s = min - minutes
    sec = s*60
    JD = JDN + (hours-12)/24 + minutes/1440 + sec/86400
    return JD



def JD_to_date(JD)->float:
    tem = JD + 0.5
    F = int(tem)
    I = tem - F
    if F > 2299160:
        A = int((F-1867216.25)/36524.25)
        B = F + 1 + A- int(A/4)
    else:
        A = 1
    C = B +1524
    D = int((C-122.1)/365.25)
    E = int(365.25 * D)
    G = int((C-E)/30.6001)
    d = C-E+I-int(30.6001*G)
    if G < 13.5:
        mint = G - 1
    else:
        mint = G - 13
    if mint > 2.5:
        y = D -4716
    else:
        y = D -4715
    hours = int  ((d - int(d)) * 24)
    minutes = int (((d - int(d)) * 24) - hours)
    seconds = (((d - int(d)) * 24) - hours) - minutes
    e = list[y , mint , int(d), hours , minutes , seconds ]
    return e



def ut_to_gst (year:int, month:int, day:int, ut_time:float)->float:
    JD = date_to_jd(year,month, day)
    S = JD -2451545.0
    T = S/36525
    T0 = 6.697374558 + (2400.051336*T)+(0.000025862*(T**2))
    T0 = T0 % 24
    if T0 < 0:
        T0 = T0 + 24
    Star_time = ut_time * 1.002737909
    GST = T0 + Star_time
    if GST > 24:
        GST = GST-24
    return GST



def Gst_to_LST(GST, longitude:int)->float:
        longitude = longitude / 15
        LST = GST + longitude
        if LST > 24:
            LST = LST-24
        elif LST < 0:
            LST = LST + 24
        return LST



def UT_to_LT(u_time:float, Time_zone:float)->float:
    u_time = u_time + Time_zone
    if u_time > 24:
        u_time = u_time - 24
    return u_time




def LT_to_UT(l_time:float, Time_zone:float)->float:
    l_time = l_time - Time_zone
    if l_time > 24:
        l_time = l_time -24
    return l_time



def LT_to_GST(year:int,month:int, day:int, time:float, time_zone:float)->float:
    Ut = time - time_zone
    if Ut > 24:
        Ut = Ut - 24
        day = day - 1
    elif Ut < 0:
        Ut = Ut + 24
        day = day + 1
    GST = ut_to_gst(year,month,day,Ut)
    return GST



def LT_to_Lst(year:int,month:int, day:int, time:float, time_zone:float,longtitude:float)->float:
    Ut = time - time_zone
    if Ut > 24:
        Ut = Ut - 24
        day = day + 1
    elif Ut < 0:
        Ut = Ut + 24
        day = day - 1
    Gst = ut_to_gst(year,month,day,Ut)
    Lst  = Gst + longtitude/15
    if Lst > 24:
        Lst = Lst -24
    elif Lst < 0:
        Lst = Lst + 24
    return  Lst
