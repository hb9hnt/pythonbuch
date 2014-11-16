def Celsius_Kelvin(t):
    if t >= ABSOLUTER_NP_C:
        return t - ABSOLUTER_NP_C
    else:
        raise TypeError(FEHLERMELDUNG_TEMP)