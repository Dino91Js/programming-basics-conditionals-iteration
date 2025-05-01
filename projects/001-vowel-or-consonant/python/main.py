
# chiedere all'utente di inserire una lettera
# verificare se la lettera è una vocale o una consonante 
#   SE lettera == vocale ALLORA stampa "The entered letter is a vowel"
#   ALTRIMENTI SE lettera == y ALLORA stampa "Sometimes y is a vowel Sometimes y is a consonant"
#   ALTRIMENTI stampa "The entered letter is a consonant"


vowels = {'a','e','i','o','u','a','e'}

letter = input("Enter a letter ").lower()

if letter in vowels:
    print("The entered letter is a vowel")
elif letter == "y":
    print("Sometimes y is a vowel sometimes y is a consonant")
else:
    print("The entered letter is a consonant")
