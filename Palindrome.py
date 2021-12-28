import sys, unicodedata

def normalize (input_string, to_lower_case=True, remove_spaces=True, remove_accents=True):
    if to_lower_case:
        input_string = input_string.lower()
    if remove_spaces:
        input_string = input_string.replace(" ","")
    if remove_accents:
        input_string = unicodedata.normalize("NFKD", input_string)
        palindrome_bez_diakritiky = ''
        for znak in input_string:
            if not unicodedata.combining(znak):
                palindrome_bez_diakritiky += znak
        input_string = palindrome_bez_diakritiky        
    return input_string

def is_palindrome (palindrome_bez_diakritiky):
    for index,letter in enumerate(palindrome_bez_diakritiky):    
        if letter == (palindrome_bez_diakritiky [index*-1-1]):
            pass
        else: 
            return False
    return True

if (len(sys.argv)) == 1:
    print ("\n\n!!! Nebyl zadán vstupní parametr !!!\n\n")
    
palindrome = sys.argv[1]

palindrome_bez_diakritiky = normalize (palindrome)
result = is_palindrome (palindrome_bez_diakritiky)
print (f"Zadaný řetězec: {palindrome} ({palindrome_bez_diakritiky}) {'je' if result else 'není'} palindrom.")

