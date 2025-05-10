
# Importo la funzione random per simulare i lanci della moneta
import random

# Dichiarazione delle variabili necessarie al ciclo 
print("")
testa = 0 # contatore delle volte che esce tesa (T)
croce = 0 # contatore delle volte che esce croce (C)
contatore_serie = 0 # contatore delle 10 serie richieste dal test
lanci_per_riga = 0 # contatore dei lanci per ogni serie
media = 0 # somma di tutti i lanci per la media finale


# Dichiarazione ciclo per la simulazione
while contatore_serie < 10: 
    lancio_moneta = random.randrange(2) # simulazione lancio moneta 
    
    if lancio_moneta == 0: # quando esce 0 STAMPA (T)
        print("T", end = " ")
        lanci_per_riga += 1 # aggiungo +1 al contatore dei lanci per ogni riga 
        media += 1 # aggiungo +1 al contatore della media finale 
        testa += 1 # aggiungo +1 al contatore della testa
        croce = 0 # azzero ogni volta il contatore della croce (per non superare il 3)
        
        if testa == 3: # quando contatore testa arriva a 3 lanci uguali, 
            testa = 0 # azzero in contatore (per non superare il 3)
            print ("(" + str(lanci_per_riga) + " lanci)") # STAMPO i lanci necessari per la seguente riga 
            lanci_per_riga = 0 # azzero i lanci della riga seguente (per evitare che si sommino alla prossima serie)
            contatore_serie += 1 # aggiungo +1 al contatore delle serie di tutto il ciclo 
            
            if contatore_serie == 10: # quando arrivo a 10 serie faccio la media totale di tutti i lanci e STAMPO il risultato finale  
                print("")
                print("In media sono necessari", media / 10, "lanci.")

    # Ripeto gli stessi passaggi quando esce croce (C)       
    else:
        print("C", end = " ")
        lanci_per_riga += 1
        media += 1
        croce += 1 
        testa = 0
        if croce == 3:
            croce = 0
            print ("(" + str(lanci_per_riga) + " lanci)")
            lanci_per_riga = 0
            contatore_serie += 1
            if contatore_serie == 10:
                print("")
                print("In media sono necessari", media / 10, "lanci.")