"""Write a code that will take (AnyString) and substitute all vowels with
character's like $#%^&* etc..... but DO NOT USE ' or " as any of your characters."""
import random
def replace_letters(s):
    vowels = "aeiouAEIOU"
    consonants = "bcdfghjklmnpqrstvxzBCDFGHJKLMNPQRSTVXZ"
    word = ""
    for x in s:
        if x in vowels:
            x = random.randint(1, 6)
            if x == 1:
                x = "$"
            if x == 2:
                x = "#"
            if x == 3:
                x = "%"
            if x == 4:
                x = "^"
            if x == 5:
                x = "&"
            if x == 6:
                x = "*"
        #for x in s:
            #if x in consonants:
                #x = random.randint(1, 6)
                #if x == 1:
                    #x = "$"
                #if x == 2:
                    #x = "#"
                #if x == 3:
                    #x = "%"
                #if x == 4:
                    #x = "^"
                #if x == 5:
                    #x = "&"
                #if x == 6:
                    #x = "*"
        word += x
    return word
print(replace_letters('Compsci yeah'))
