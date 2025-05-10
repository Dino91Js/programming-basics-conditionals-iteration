# - Ciclo FOR per controllare i numeri da 1 a 101 con la funzione RANGE
# - SE il numero è divisibile per 3 e per 5 (operatore modulo %) STAMPA ("fizz buzz"). Prima controllo la doppia divisibilità
# - ALTRIMENTI SE il numero è divisibile per 3 (operatore modulo %) STAMPA ("fizz")
# - ALTRIMENTI SE il numero è divisibile per 5 (operatore modulo %) STAMPA ("buzz")
# - ALTRIMENTI STAMPA numero

print("")
for numero in range (1, 101):
    if numero % 3 == 0 and numero % 5 == 0:
        print("fizz buzz")
    elif numero % 3 == 0:
        print("fizz")
    elif numero % 5 == 0:
        print("buzz")
    else:
        print(numero)
print("")