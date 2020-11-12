
def fun(costo, sconto, minimo, fondi):
    numPacchetti = 0
    while fondi > 0:
        # compro
        if costo > fondi:
            break
        numPacchetti += 1
        fondi -= costo
        costo -= sconto
        if costo < minimo:
            costo = minimo
    return numPacchetti


c, s, m, b = str(input()).split()
print(fun(int(c), int(s), int(m), int(b)))
