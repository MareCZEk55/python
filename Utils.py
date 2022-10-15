def kontrolaCisla(vstup):
    retVal = False
    try:
        vstup = float(vstup)
        retVal = True
    except ValueError:
        retVal = False
    return retVal