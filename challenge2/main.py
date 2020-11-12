
def fun(giorni):
    decrementi = 0
    incrementi = 0
    invariati = 0

    for g in giorni:
        if g == 0:
            invariati += 1
        elif g > 0:
            incrementi += 1
        else:
            decrementi += 1

    decrementi /= len(giorni)
    incrementi /= len(giorni)
    invariati /= len(giorni)

    incrementi = round(incrementi * 100, 1)
    if int(incrementi) == incrementi:
        incrementi = int(incrementi)

    decrementi = round(decrementi * 100, 1)
    if int(decrementi) == decrementi:
        decrementi = int(decrementi)

    invariati = round(invariati * 100, 1)
    if int(invariati) == invariati:
        invariati = int(invariati)

    print(incrementi)
    print(decrementi)
    print(invariati)


n = int(input())
giorni = [int(x) for x in input().split()]
fun(giorni)
