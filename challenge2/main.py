"""
Il team di marketing di Tutored ha finito di testare diverse campagne social. È arrivato il momento di analizzarne i risultati.
Data una campagna, durata `n` giorni, sono stati registrate le variazioni di utenti in quei giorni.
Sviluppa un algoritmo che date queste variazioni, restituisca la percentuale di giorni in cui c'è stato un incremento, un decremento e nessuna variazione.
Se necessario la percentuale deve essere arrotondata alla prima cifra decimale.

Input Format

    La prima riga contiene un intero `n`, la durata in giorni della campagna
    La seconda riga contiene il vettore `giorni`, contenente gli incremeneti di utenti durante la campagna

Constraints

* 1 < n < 100
* -100 <= giorni[i] <= 100

Output Format

Stampa tre righe:

    Nella prima la percentuale di giorni con incremento di utenti
    Nella seconda la percentuale di giorni con decremento di utenti
    Nella terza la percentuale di giorni con utenti invariati

Se necessario, la percentuale deve essere arrotondata alla prima cifra decimale.
"""


def fun(days):
    reductions = 0
    increments = 0
    neutral = 0

    for day in days:
        if day == 0:
            neutral += 1
        elif day > 0:
            increments += 1
        else:
            reductions += 1

    reductions /= len(days)
    increments /= len(days)
    neutral /= len(days)

    increments = round(increments * 100, 1)
    if int(increments) == increments:
        increments = int(increments)

    reductions = round(reductions * 100, 1)
    if int(reductions) == reductions:
        reductions = int(reductions)

    neutral = round(neutral * 100, 1)
    if int(neutral) == neutral:
        neutral = int(neutral)

    print(increments)
    print(reductions)
    print(neutral)


n = int(input())
days = [int(x) for x in input().split()]
fun(days)
