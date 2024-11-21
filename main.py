"""
Ce programme a pour objectif d'encoder une chaîne de caractères par une liste de tuples.
Chaque tuple est composé d’un caractère (et d’un seul) et du nombre d’occurences 
consécutives de ce caractère. Par exemple :
        - la chaîne MMMMaaacXolloMM ;
        - est représentée par la liste : 
        [('M', 4), ('a', 3), ('c', 1), ('X', 1), ('o', 1), ('l', 2), ('o', 1), ('M', 2)]

Ce fichier contient deux fonctions secondaires :
        - artcode_i(s) et;
        - artcode_r(s).
    qui tous deux encodent la chaîne de caractères passée en paramètre, l'un à l'aide
    d'un algorithme itératif, l'autre récursif.

et aussi une fonction principale main(), serant à faire des tests d'appel.
"""

#### Imports et définition des variables globales


#### Fonctions secondaires


def artcode_i(s):
    """retourne la liste de tuples encodant une chaîne de caractères 
    passée en argument selon un algorithme itératif

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
"""
    # initialisation
    c = [s[0]]
    o = [1]
    # continuité
    k = 1
    while k < len(s):
        if s[k] == s[k-1]:
            o[-1] += 1
        else :
            c = c + [s[k]]
            o = o + [1]
        k += 1
    # retour de la liste de tuples
    return list(zip(c,o))


def artcode_r(s):
    """retourne la liste de tuples encodant une chaîne de caractères 
    passée en argument selon un algorithme récursif

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
"""
    code = []
    # cas de base
    if s == "":
        return code
    # calculer le nombre d'occurences du premier caractère de la chaîne
    c = [s[0]]
    o = [1]
    # si le premier caractère est '\' --> retour à la ligne
    if s.startswith('\n'):
        c = ['\n']
    else :
        k = 1
        while k<len(s) and s[k]==s[k-1]:
            o[0] += 1
            k += 1
    code = list(zip(c,o))
    # appel récursif
    return code + artcode_r(s.replace(s[0],'',o[0]))

#### Fonction principale


def main():
    """
    Effectue des tests d'appel
    """
    print("Appel itératif : ")
    print(artcode_i('MMMMaaacXolloMM'))
    print("Appel récursif: ")
    print(artcode_r('MMMMaaacXolloMM'))

if __name__ == "__main__":
    main()
