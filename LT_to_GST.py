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

#Местное время в Гринвичевское звёздное время