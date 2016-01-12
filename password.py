# coding: utf-8 
def getNext(password):
    """
    Série de tests exprimés en doctest
    >>> getNext('a')
    'b'
    >>> getNext('az')
    'ba'
    >>> getNext('bc')
    'bd'
    """
    pwd = list(password)  #1 Création d'une liste des caractères du mot de passe
    found = False
    i=len(pwd)-1 

	
    while not found:
        if pwd[i] < 'z':
           pwd[i] = chr(ord(pwd[i])+1)  #2   Si le caractère est inférieur à 'z' on l'incrémente de 1
           found = True             
        else:
            pwd[i] = 'a'
            i = i-1
            if(i==-1):
                raise ValueError("Limite de mots de passes atteinte.")
		   
    
    return ''.join(pwd) #3 il renvoie le nouveau mot de passe en concaténant tous les caractères (en insérant une chaine vide entre chacun)



def hasNoBadChar(password):

    pwd = list(password)  

    for i in pwd:
        if i in 'iol':
            return False
        
    return True

def hasTwoPairs(password):

    pwd = list(password) 
    i=len(pwd)-1
    countpairs = 0

    if (i<3):
        return False
    
    while (i >= 0):
        if(pwd[i] == pwd[i-1]):
            countpairs += 1
            i -= 2
        else:
            i -= 1
    
    return (countpairs >= 2)

def hasSeries(password):

    pwd = list(password) 
    i=len(pwd)-1

    while (i >= 0):
        if(pwd[i] == chr(ord(pwd[i-1])+1) and pwd[i] == chr(ord(pwd[i-2])+2)):
            return True
        else:
            i -= 1

    return False

# Grâce à ce fragment de code, si vous exécutez ce fichier, les tests doctests seront exécutés également. 
# Si vous ne voulez plus que les tests s'exécutent, commentez les deux lignes ci-dessous. 
# Si vous préférez lancer vos tests à la main, commentez également les lignes, et utilisez "python -m doctest pass.py" en console. 
if __name__ == "__main__":
    import doctest
    doctest.testmod()
