import sys, unicodedata

palindrome = sys.argv[1].lower().replace(" ","") #nemusi byt kulate zavorky, neni funkce
palindrome = unicodedata.normalize("NFKD", palindrome)
palindrome_bez_diakritiky = ''
for znak in palindrome:
    if not unicodedata.combining(znak):
        palindrome_bez_diakritiky += znak

def is_palindrome (palindrome_bez_diakritiky):
    for index,letter in enumerate(palindrome_bez_diakritiky):    
        #print (index,letter)
        #print (f"{letter} ? {palindrome [index*-1-1]}")
        if letter == (palindrome_bez_diakritiky [index*-1-1]):
            pass
        else: 
            return "není"
    return "je"

result = is_palindrome (palindrome_bez_diakritiky)
print ("Toto", result, "palindrom.")








