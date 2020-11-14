"""
Tutored vuole acquistare dei nuovi crediti per Google Ads, che verranno usati nelle campagne pubblicitarie invernali. Si vuole sfruttare questo periodo per usufruire degli sconti che sono offerti ai clienti secondo la seguente politica:
Dopo l'acquisto di un pacchetto di crediti, il successivo costa `s` euro in meno. Si può arrivare fino ad un costo minimo di `m`.
Sapendo che il budget è di `b` euro, ed il costo di partenza è di `c`, trovare il numero massimo di pacchetti acquistabili.

Input Format

La prima riga contiene quattro interi,

c = il costo iniziale
s = lo sconto ad ogni acquisto
m = il prezzo minimo raggiungibile
b = il budget

Constraints

Output Format

La funzione deve fornire un intero, rappresentante il massimo numero di pacchetti acquistabili.
"""


def fun(cost, sale, minimum, budget):
    packNum = 0
    while budget > 0:
        # compro
        if cost > budget:
            break
        packNum += 1
        budget -= cost
        cost -= sale
        if cost < minimum:
            cost = minimum
    return packNum


c, s, m, b = str(input()).split()
print(fun(int(c), int(s), int(m), int(b)))
