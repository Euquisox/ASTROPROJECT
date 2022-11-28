from Astro import date_to_jd

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

#Всемирное время в Гринвичевское звёздное время