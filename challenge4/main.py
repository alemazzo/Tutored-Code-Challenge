
def test(massimo, punteggi):
    if len(punteggi) == 0 or massimo == 0:
        return 0
    elif punteggi[0] > massimo:
        raise Exception()
    elif len(punteggi) == 1:
        if punteggi[0] % massimo != 0:
            raise Exception()
        else:
            return int(massimo / punteggi[0])
    else:
        index = 0
        while(massimo > 0):
            massimo -= punteggi[0]
            if massimo < 0:
                raise Exception()
            if massimo >= punteggi[1]:
                try:
                    res = test(
                        massimo - (punteggi[0]),
                        punteggi[1: len(punteggi)]
                    )
                    index += res + 1
                except:
                    pass
        """
        while(punteggi[0] <= massimo):
            if punteggi[0] <= massimo:
                index += 1
            else:
                raise Exception()
            massimo -= punteggi[0]

            try:
                res = test(massimo, punteggi[1: len(punteggi)])
                index += res
            except:
                index -= 1
                pass
        """
        #print(f"P = {punteggi[0]} - Index = {index}")
    return index


def fun(number, punteggi):
    try:
        return test(number, sorted(punteggi))
    except:
        return 0


n, m = [int(x) for x in input().split()]
punteggi = [int(x) for x in input().split()]
print(fun(n, punteggi))
