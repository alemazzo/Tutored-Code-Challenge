"""
Nel tempo libero, i membri del team tech si divertono ad inventare possibili nuove convenzioni per gli ID delle tabelle del database.
L'ultima è la seguente:
Un id è valido solo se

1. ogni lettera appare lo stesso numero di volte.
2. oppure rimuovendo un solo carattere, si ottiene una stringa che soddisfa la condizione 1

Dato un possibile `id`, verifica se questo rispetta le specifiche citate.

Input Format

La prima riga contiene una stringa, l' `id` di cui bisogna verificare la validità

Constraints

*   1 <= |id| <= 10^5

*   Ogni carattere appartiene all'insieme [a-z]

Output Format

Fornire

*   "valido" se l `id` soddisfa le condizioni
*   "non valido" altrimenti

"""


def fun(id):
    letters = dict()
    for char in id:
        if char in letters:
            letters[char] += 1
        else:
            letters[char] = 0

    values = sorted(letters.values())
    prev = values[0]
    diffs = 0
    for val in values:
        diffs += val - prev

    if diffs < 2:
        return "valido"
    else:
        return "non valido"


id = str(input())
print(fun(id))
