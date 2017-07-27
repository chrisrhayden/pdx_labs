# validart passwed


import string



def valpaswrod(paswd: str):
    spe = False
    low = False
    upp = False
    dig = False
    if len(paswd) > 5 or < 12:
        continue
    else:
        print('invalid pasword')
    for cha in paswd:
        if cha in string.punctuation:
            spe = True
        elif cha in string.ascii_lowercase:
            low = True
        elif cha in string.ascii_uppercase:
            upp = True
        elif cha in string.digits:
            dig = True
    if  all(spe, low, upp, dig) is True:
        return True



def getpword():
    user_input = input('give pword ')
    return user_input



def lord_func():
    
