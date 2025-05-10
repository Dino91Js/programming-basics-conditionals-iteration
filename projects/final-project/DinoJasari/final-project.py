# Chiedere in input la durata (int) e il budget (float) del viaggio
print("")
durata_viaggio = int(input("Quanto dura il viaggio? ")) 
budget_totale = float(input("Quant'è il budget totale per il viaggio? "))

# Creo una variabile con budget fisso per la comparazione finale. (Se il budget è stato superato oppure no)
budget_totale_fisso = budget_totale
print("")

# Creo delle variabili contatore per tenere aggiornate le spese di viaggio
vitto = 0
alloggio = 0
trasporti = 0
varie = 0


# Variabile invio per uscire e rientrare nel ciclo while delle spese
continua_modifica_spese = ""


# Ciclo principale per aggiornare le spese oppure chiudere l’applicazione
while True:

    # Spiegazione del funzionamento dell’applicazione  
    print("- Se si vuole modificare delle spese di viaggio premere 1")
    print("")
    print("     Come inserire l'importo.")
    print("     ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯")
    print("     Per sottrarre delle spese utilizzare un numero negativo")
    print("     Altrimenti un numero positivo per aggiungere delle spese")
    print("")
    print("- Se invece si vuole chiudere il programma e visualizzare il resoconto delle spese totali permere e")
    print("")
    print("     ** ATTENZIONE **")
    print("     Se si chiude il programma non sarà piu possibilie fare alcuna modifica alle spese.")
    print("")
    scelta_iniziale = input("Quale opzione vuoi scegliere? ")
    if scelta_iniziale == "1":

        # Ciclo per continuare ad aggiornare le spese 
        while continua_modifica_spese == "":
            
            # Spiegazione delle categorie di spese e di come scegliere quali modifiche fare
            print("")
            print("- Vitto premere 1 \n"
            "- Alloggio premere 2 \n"
            "- Trasporti premere 3 \n"
            "- Varie (musei, parchi ecc...) premere 4 \n" )
            print("")
            scelta_spesa = input("Quale spesa vuoi modificare? ")
            
            # 4 scelte di spesa possibili 
            if scelta_spesa == "1":
                print("")
                
                # Ciclo per correggere eventuali errori durante l’inserimento dei dati numerici 
                while True:
                    try: 
                        ultimo_vitto = float(input("Inserisci l'importo "))
                        print("")
                    except:
                        print("Hai inserito dei caratteri non validi. Utilizza un numero con massimo 2 cifre dopo la virgola")
                        print("")
                    else:
                        break

                # Riepilogo delle spese aggiornate e del budget rimasto   
                vitto += ultimo_vitto
                budget_totale -= ultimo_vitto
                print(f"    - Le tue spese di vitto attuali sono: {vitto:.2f}€")
                print(f"    - Budget rimasto: {budget_totale:.2f}€" )
                print("")
            
            elif scelta_spesa == "2":
                print("")
                while True:
                    try:
                        ultimo_alloggio = float(input("Inserisci l'importo "))
                        print("")
                    except:
                        print("Hai inserito dei caratteri non validi. Utilizza un numero con massimo 2 cifre dopo la virgola")
                        print("")
                    else:
                        break
                alloggio += ultimo_alloggio
                budget_totale -= ultimo_alloggio
                print(f"    - Le tue spese di alloggio attuali sono: {alloggio:.2f}€")
                print(f"    - Budget rimasto: {budget_totale:.2f}€" )
                print("")
                
            elif scelta_spesa == "3":
                print("")
                while True:
                    try:
                        ultimo_trasporto = float(input("Inserisci l'importo "))
                        print("")
                    except:
                        print("Hai inserito dei caratteri non validi. Utilizza un numero con massimo 2 cifre dopo la virgola")
                        print("")
                    else:
                        break
                trasporti += ultimo_trasporto
                budget_totale -= ultimo_trasporto
                print(f"    - Le tue spese di trasporto attuali sono: {trasporti:.2f}€")
                print(f"    - Budget rimasto: {budget_totale:.2f}€" )
                print("")
                
            else:
                print("")
                while True:
                    try:
                        ultimo_varie = float(input("Inserisci l'importo "))
                        print("")
                    except:
                        print("Hai inserito dei caratteri non validi. Utilizza un numero con massimo 2 cifre dopo la virgola")
                        print("")
                    else:
                        break
                varie += ultimo_varie
                budget_totale -= ultimo_varie
                print(f"    - Le tue spese di trasporto attuali sono: {varie:.2f}€")
                print(f"    - Budget rimasto: {budget_totale:.2f}€" )
                print("")

            # Ulteriore riepilogo spese di tutto il viaggio    
            print("")
            print("Riepilogo delle tue attuali spese: \n" 
            f"- Vitto: {vitto:.2f}€ \n"
            f"- Alloggio: {alloggio:.2f}€ \n"
            f"- Trasporti: {trasporti:.2f}€ \n"
            f"- Varie: {varie:.2f}€")
            print("")
           
            # Scelta se continuare a modificare le spese oppure chiudere il ciclo 
            continua_modifica_spese = input("Per continuare a modificare le spese (premere invio). \n" 
            "Altrimenti premere 0 ")
            print("")
            if continua_modifica_spese == "0":
                break 
        continua_modifica_spese = ""
        
    # Chiusura dell’applicazione e del ciclo principale 
    else:
        
        # Riepilogo spese singole 
        print("")
        print("Ecco il riepilogo delle tue spese per tutto il viaggio")
        print("")
        print(f"- Vitto: {vitto:.2f}€ \n"
            f"- Alloggio: {alloggio:.2f}€ \n"
            f"- Trasporti: {trasporti:.2f}€ \n"
            f"- Varie: {varie:.2f}€")
        
        # Riepilogo spese totali e spesa media al giorno 
        print("")
        spese_totali = vitto + alloggio + trasporti + varie
        print(f"- Spese totali: {spese_totali:.2f}€")
        print("")
        spesa_media_viaggio = spese_totali / durata_viaggio
        print(f"- Durata del viaggio: {durata_viaggio} giorni")
        print(f"    In media hai speso {spesa_media_viaggio:.2f}€ al giorno")
        
        # Conteggio totale spese 
        # Superamento budget oppure no 
        if spese_totali > budget_totale_fisso:
            budget_superato = spese_totali - budget_totale_fisso
            print(f"    Hai speso {budget_superato:.2f}€ in più del budget totale prestabilito" )
            print("")
        else:
            budget_non_superato = budget_totale_fisso - spese_totali
            print(f"    Hai speso {budget_non_superato:.2f}€ in meno del budget totale prestabilito ")
            print("")
        break
         