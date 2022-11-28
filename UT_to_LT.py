def UT_to_LT(u_time:float, Time_zone:float)->float:
    u_time = u_time + Time_zone
    if u_time > 24:
        u_time = u_time - 24
    return u_time
#Всемирное время в местное время