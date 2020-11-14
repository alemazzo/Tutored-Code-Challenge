"""
Ad ogni attività da svolgere viene assegnato un punteggio `p`, scelto in base alla quantità di risorse necessarie per portarla a termine.
Il punteggio assegnato è un intero presente nel vettore `punteggi`.
C'è sempre qualcosa da fare, quindi per ogni punteggio, ci sono infiniti task che corrispondono a quel carico di lavoro.
Dato l'obiettivo settimanale `n`, trovare il numero di combinazioni possibili tra punteggi che sommati diano esattamente `n` punti.

Input Format

La prima riga contiene due interi,

* `n` = l'obiettivo settimanale

* `m` =  la lunghezza del vettore `punteggi`

La seconda riga contiene `m` interi, il contenuto del vettore `punteggi`

Constraints

* 1 <= punteggi[i] <= 50

* 1 <= n <= 250

* 1 <= m <= 50


Tutti i punteggi sono diversi tra di loro.

Output Format

Stampa un intero a 64 bit, rappresentante il numero di combinazioni tra punteggi che è possibile effettuare per ottenere esattamente l'obiettivo settimanale.

"""


def fun(maximum, scores):
    # Return in case of a non-possible sequence
    Error = None

    if maximum == 0:
        return 1

    if len(scores) == 0:
        # If we have no more scores but we haven't
        # reached the maximum the sequence we are testing isn't possible.
        return Error if maximum != 0 else 0

    actualValue = scores[0]

    # if actualValue > maximum:
    #    return Error

    counter = 0
    for length in range(0, int(maximum / actualValue) + 1):
        newMaximum = maximum - (length * actualValue)

        res = fun(newMaximum, scores[1: len(scores)])
        if res is Error:
            pass
        else:
            counter += res

    if counter == 0:
        return Error

    return counter


n, m = [int(x) for x in input().split()]
scores = [int(x) for x in input().split()]

res = fun(n, sorted(scores, reverse=True))
print(0 if res is None else res)


"""
ERROR = None
    if len(scores) == 0:
        if maximum == 0:
            return 0
        else:
            return ERROR
    if maximum == 0:
        return 0
    elif scores[0] > maximum:
        return ERROR

    counter = 0
    for i in range(0, int(maximum/scores[0]) + 1):
        # Ci sarà almeno un ciclo
        # Per ogni possibile presa dell elemento
        # Ne ho presi i
        counter += 1
        newMassimo = maximum - (i * scores[0])

        # Quante combinazioni ci sono senza questo elemento ?
        comb = fun(newMassimo, scores[1:len(scores)])

        # Se senza questo elemento e con i restanti valori ci sono combinazioni
        if comb is ERROR:
            counter -= 1

    if counter == 0:
        return ERROR
    return counter



    ***********************


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    scores = list(map(int, input().rstrip().split()))

    res = fun(n, sorted(scores))

    fptr.write(str(0 if res is None else res) + '\n')

    fptr.close()

"""
