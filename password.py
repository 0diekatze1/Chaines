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
    >>> getNext('')
    'a'
    >>> getNext('zz')
    'aaa'
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
		   
    
    return ''.join(pwd) #3 il renvoie le nouveau mot de passe en concaténant tous les caractères (en insérant une chaine vide entre chacun)



# Grâce à ce fragment de code, si vous exécutez ce fichier, les tests doctests seront exécutés également. 
# Si vous ne voulez plus que les tests s'exécutent, commentez les deux lignes ci-dessous. 
# Si vous préférez lancer vos tests à la main, commentez également les lignes, et utilisez "python -m doctest pass.py" en console. 
if __name__ == "__main__":
    import doctest
    doctest.testmod()
