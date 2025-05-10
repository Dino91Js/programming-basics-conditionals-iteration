# The length of a month varies from 28 to 31 days.
# In this exercise you will create a program that reads the name of a month from the user as a string.
# Then your program should display the number of days in that month.
# Display 28 or 29 days for February so that leap years are addressed.

# Example:  
# Input = April  
# Output = 30


# Chiedere all'utente di inserire il nome del mese (str)
# SE mese == "Febbraio":
# STAMPA "Inserire anche l'anno per poter determinare se Febbraio contiene 28 o 29 giorni"

# Creo delle liste con i nomi dei mesi in base alla loro durata espressa in giorni 
# mesi_31_giorni = [gennaio, marzo, maggio, luglio, agosto, ottobre, dicembre]
# mesi_30_giorni = [aprile, giugno, settembre, novembre]

# SE mese in mesi_31_giorni ALLORA stampa "Il mese contiene 31 giorni"
# ALTRIMENTI SE mese in mesi_30_giorni ALLORA stampa "Il mese contiene 30 giorni"
# ALTRIMENTI SE mese == febbraio 
#       SE anno % 400 == 0 STAMPA "Il mese contiene 29 giorni"
#       ALTRIMENTI SE anno % 4 == 0 and not anno % 100 == 0 STAMPA "Il mese contiene 29 giorni"
#       **Se l'anno è divisibile per 4 e non divisibile per 100 allore l'anno è bisestile**
#       ATRIMENTI STAMPA "Il mese contiene 28 giorni"


# Chiedere all'utente di inserire il nome del mese 
print("")
mese = input("Inserire il nome del mese ").lower()

# Se il mese è febbraio chiedere all'utente l'anno per poter determinare se bisestile oppure no 
if mese == "febbraio":
    anno = int(input("Inserire anche l'anno per poter determinare se febbraio contiene 28 o 29 giorni "))
print("")

# Creazione di 2 liste per i mesi da 30 e 31 giorni 
mesi_31_giorni = ["gennaio", "marzo", "maggio", "luglio", "agosto", "ottobre", "dicembre"]
mesi_30_giorni = ["aprile", "giugno", "settembre", "novembre"]

# In base all'input usare le condizioni per determinare in quale lista è contenuto il mese inserito
# Stampare la lunghezza del mese  
if mese in mesi_31_giorni:
    print("Il mese contiene 31 giorni")
    print("")
elif mese in mesi_30_giorni:
    print("Il mese contiene 30 giorni")
    print("")

# Per il mese di febbraio calcolo matematico per determinare la lunghezza del mese
# Stampare la lunghezza del mese   
else:
    if anno % 400 == 0:
        print("Il mese contiene 29 giorni")
    elif anno % 4 == 0 and not anno % 100 == 0: # Se l'anno è divisibile per 4 e non divisibile per 100 allora l'anno è bisestile
        print("Il mese contiene 29 giorni")
    else:
        print("Il mese contiene 28 giorni")