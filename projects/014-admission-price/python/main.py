# # Admission Price

# A particular zoo determines the price of admission based on the age of the guest.   
# - Guests 2 years of age and less are admitted without charge. 
# - Children between 3 and 12 years of age cost $14.00.
# - Seniors aged 65 years and over cost $18.00. 
# - Admission for all other guests is $23.00.  

# Create a program that begins by **reading the ages of all the guests in a group from the user**, 
# with one age entered on each line.   
# The user will enter a **blank line** (a newline character) to indicate that there are no more guests in the group.    
# Then your program should display the admission cost for the group with an appropriate message.   
# The cost should be displayed using **two decimal places**.



# - Creo una lista anni_ospiti vuota
# - Creo una variabie somma_biglietti = 0 (Andranno inseriti il totale del prezzo dei biglietti)

# - Ciclo WHILE TRUE che prende in input("Inserisci gli anni di un ospite (premi Invio per terminare): ")
# Per continuare a prendere gli anni dei visitatori
# - SE l'input "" (tasto invio) BREAK (fermo il ciclo)
# - Con la funzione .append metto nella lista anni_ospiti, i dati presi dal ciclo e li cambio da (str) a (int)

# - Ciclo FOR per controllare ogni elemento della lista 
# - SE anni > 2 AND anni <= 12 agginugni + 14 in somma_biglietti
# - AlTRIMENTI SE anni > 65 agginugni + 18 in somma_biglietti
# - AlTRIMENTI agginugni + 23 in somma_biglietti

# - STAMPA totale. Formato $00.00



print("")

# Lista anni_ospiti vuota e variabie somma_biglietti 
anni_ospiti = []
somma_biglietti = 0

# Ciclo per prendere gli anni dei visitatori e salvarli in lista (int) 
while True:
    anni = input("Inserisci gli anni di un ospite (premi Invio per terminare): ")
    if anni == "":
        break
    anni_ospiti.append(int(anni))

# Stampo il prezzo del biglietto per ogni range di età
print("")
print("Per i bambini di anni 2 o inferiore l'entrata è gratuita.")
print("Per i bambini compresi tra i 3 e i 12 anni il costo è $14.00.")
print("Per gli adulti sopra i 65 anni il costo è $18.00.")
print("Per tutti gli altri il costo é $23.00.")
print("")

# Ciclo per controllare ogni elemento della lista e aggiungere il prezzo (nella variabile somma_biglietti) per ogni range di età
for anni in anni_ospiti:
    if anni > 2 and anni <= 12:
        somma_biglietti += 14 
    elif anni >= 65:
        somma_biglietti += 18 
    else:
        somma_biglietti += 23 

# Stampo il totale con il formato richesto 
print("Totale:", f"{somma_biglietti:.2f}$")
