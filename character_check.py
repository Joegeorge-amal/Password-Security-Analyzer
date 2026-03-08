import string
def analyzecharacters(password):
    haslower = any(c.islower() for c in password)
    hasupper = any(c.isupper() for c in password)
    hasdigit = any(c.isdigit() for c in password)
    hassymbol = any(c in string.punctuation for c in password)

    return{"lowercase": haslower,"uppercase": hasupper,"digits": hasdigit,"symbols": hassymbol}