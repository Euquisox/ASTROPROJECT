def LT_to_UT(l_time:float, Time_zone:float)->float:
    l_time = l_time - Time_zone
    if l_time > 24:
        l_time = l_time -24
    return l_time

#Местное время в Всмирное время