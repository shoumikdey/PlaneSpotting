

def identifier1(df, tc): #Aircraft identification
    if 17 <= df <= 18 and 1 <= tc <= 4:
        return True

def identifier2(df, tc):
    if 17 <= df <= 18 and 5 <= tc <= 8:
        return True

def identifier3(df, tc): #airborne position with baro altitude
    if 17 <= df <= 18 and 9 <= tc <= 18:
        return True

def identifier4(df, tc): #Airborne velocity
    if 17 <= df <= 18 and tc == 19:
        return True

def identifier5(df, tc): #Airborne Position with GNSS altitude
    if 17 <= df <= 18 and 20 <= tc <= 22:
        return True

def identifier6(df, tc): #Operation status
    if 17 <= df <= 18 and tc == 31:
        return True

def identifier7(df, tc): #Enhanced Mode-S
    if 20 <= df <= 21:
        return True