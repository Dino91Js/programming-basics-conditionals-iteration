# Is a String a Palindrome?

# A string is a palindrome if it is identical forward and backward.    
# For example “anna”, “civic”, “level” and “hannah” are all examples of palindromic words. 

# Write a program that **reads a string from the user** and **uses a loop to determine whether it is a palindrome**. 
# Display the result, including a meaningful output message.

# "Aibohphobia" is the extreme or irrational fear of palindromes.   
# This word was constructed by prepending the -phobia suffix with its reverse, resulting in a palindrome.   

# "Ailihphilia" is the fondness for or love of palindromes.  
# It was constructed in the same manner from the -philia suffix.

# Example:  
# Input: cat  
# Output:  cat is not a palindrome

# Input: wow  
# Output: wow is a palindrome

# - Salvo una parola come input (str)

# - WHILE parola [0:] == parola [::-1] STAMPA parola, ("la parola è un palindromo").  # Controllo se la parola letta al contrario è = alla parola letta normalmente.
# - ALTRIMENTI STAMPA parola, ("la parola non è un palindromo").

print("")
parola = input("Scrivi una parola ").lower()

print("")
while parola[0:] == parola[::-1]:
    print("La parola", parola, "è un palindromo")
    break
else:
    print("La parola", parola, "non è un palindromo")
print("")