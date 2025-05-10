
# A particular cell phone plan includes for € 15.00 a month: 
# - 50 minutes of air time 
# - 50 text messages    
# - Each additional minute of air time costs € 0.25
# - Each additional text messages cost € 0.15  
# - All cell phone bills include an additional charge of € 0.44 to support 911 call centers

# The entire bill (including the 911 charge) is subject to **5 percent sales tax**.  

# Write a program that **reads the number of minutes and text messages used in a month** from the user.  
# Display:
# - Base charge,
# - Extra minutes charge (if any),
# - Extra text message charge (if any),
# - 911 fee, 
# - Tax,
# - Total bill amount.   

# Only display the additional minute and text message charges if the user incurred costs in these categories. 
# Ensure that all the charges are displayed **using 2 decimal places**.

# Example:   
# Input minutes: 500  
# Input messages: 55  

# Output:  
# Base charge: 15.00€  
# Extra minutes charge: 112.50€  
# Extra messages charge: 0.75€  
# 911 fee: 0.44€  
# Tax: 6.43€  
# Total bill amount: 135.12€


# Chiedere all'utente di inserire la quantità di minuti usati (int) e messaggi usati (int)
minuti = int(input("Inserire i minuti usati questo mese "))
messaggi = int(input("Inserire i messaggi mandati questo mese "))

# Tariffa base uguale per tutti 
print("")
print("Tariffa base: 15.00€")

# Se i minuti <= 500 e i messaggi <= 50 non ci sono modifiche sulla fattura
# quindi restituisco i valori fissi senza fare calcoli     
if minuti <= 500 and messaggi <= 50:
    print("Minuti extra: 00.00€")
    print("Messaggi extra: 00.00€")
    print("Tassa 911: 0.44€")
    print("Imposta sulle vendite 0.77€")
    print("Totale fattura: 16.21€")
    print("")
    
# Quando i minuti > 500 e messaggi <= 50
# calcolo i minuti extra, imposte al 5% e il totale   
elif minuti > 500 and messaggi <= 50:
    minuti_extra_telefonate = (minuti - 500) * 0.25
    print("Minuti extra:", f"{minuti_extra_telefonate:.2f}€")
    
    print("Messaggi extra: 00.00€")
    print("Tassa 911: 0.44€")
    
    imposta_vendite = 5 / 100 * (15.00 + minuti_extra_telefonate + 0.44)
    print("Imposta sulle vendite:", f"{imposta_vendite:.2f}€")
    
    print("Totale fattura:", f"{15.00 + minuti_extra_telefonate + 0.44 + imposta_vendite:.2f}€")
    print("")

# Quando i messaggi sono > 50 e i minuti <= 500
# calcolo i messaggi extra, imposte al 5% e il totale  
elif minuti <= 500 and messaggi > 50:
    print("Minuti extra: 00.00€")
   
    messaggi_extra = (messaggi - 50) * 0.15
    print("Messaggi extra:", f"{messaggi_extra:.2f}€") 
    
    print("Tassa 911: 0.44€")
    
    imposta_vendite = 5 / 100 * (15.00 + messaggi_extra + 0.44)
    print("Imposta sulle vendite:", f"{imposta_vendite:.2f}€")
    
    print("Totale fattura:", f"{15.00 + messaggi_extra + 0.44 + imposta_vendite:.2f}€")
    print("")

# Quando i minuti > 500 e messaggi > 50
# calcolo i messaggi extra, minuti extra, imposte al 5% e il totale 
else:
    minuti_extra_telefonate = (minuti - 500) * 0.25
    print("Minuti extra:", f"{minuti_extra_telefonate:.2f}€")
    
    messaggi_extra = (messaggi - 50) * 0.15 
    print("Messaggi extra:", f"{messaggi_extra:.2f}€")
    
    print("Tassa 911: 0.44€")    
    
    imposta_vendite = 5 / 100 * (15.00 + minuti_extra_telefonate + messaggi_extra + 0.44)
    print("Imposta sulle vendite:", f"{imposta_vendite:.2f}€")
    
    print("Totale fattura:", f"{15.00 + minuti_extra_telefonate + messaggi_extra + 0.44 + imposta_vendite:.2f}€")
    print("")

