def Gst_to_LST(GST, longitude: int) -> float:
    longitude = longitude / 15
    LST = GST + longitude
    if LST > 24:
        LST = LST - 24
    elif LST < 0:
        LST = LST + 24
    return LST

#Гринвичевское звёздное время в местное звёздное время