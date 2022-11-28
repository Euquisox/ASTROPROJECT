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

#Местное время в Местное звёздное время