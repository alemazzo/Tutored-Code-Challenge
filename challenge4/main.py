def fun(massimo, punteggi):
    ERROR = None
    if len(punteggi) == 0:
        if massimo == 0:
            return 0
        else:
            return ERROR
    if massimo == 0:
        return 0
    elif punteggi[0] > massimo:
        return ERROR

    counter = 0
    for i in range(0, int(massimo/punteggi[0]) + 1):
        # Ci sarà almeno un ciclo
        # Per ogni possibile presa dell elemento
        # Ne ho presi i
        counter += 1
        newMassimo = massimo - (i * punteggi[0])

        # Quante combinazioni ci sono senza questo elemento ?
        comb = fun(newMassimo, punteggi[1:len(punteggi)])

        # Se senza questo elemento e con i restanti valori ci sono combinazioni
        if comb is ERROR:
            counter -= 1

    if counter == 0:
        return ERROR
    return counter


n, m = [int(x) for x in input().split()]
punteggi = [int(x) for x in input().split()]
print(fun(n, sorted(punteggi)))
