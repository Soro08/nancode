#Chaînes de caractères

1- Calculer le nombre d’occurences d’un caractère :

Exemple :

compte_car("hello", "l") # retourne 2
compte_car("hello", "z") # retourne 0
compte_car("hello", "H") # retourne 0 (différence entre "h" et "H")


def compte_car(s, c):
    """
    :entrée s: str
    :entrée c: str
    :sortie n: int
    :pré-cond: len(c) == 1
    :post-cond: n est le nombre de valeurs i telles que s[i] == c
    """
2- Calculer le nombre de lettres minuscules :

Pour cet exercice, on se limitera aux

26 lettres simples de l’alphabet, sans considérer les caractères accentués ou altérés.
def compte_minuscules(s):
    """
    :entrée s: str
    :sortie n: int
    :post-cond: n est le nombre valeurs de i telles que
                s[i] est une minuscule.
    """

 3- Détermine si une chaîne est un palindrome :

 def palindrome(s):
    """
    :entrée s: str
    :sortie p: bool
    :post-cond: p est True si et seulement si
                pour tout i tel que 0 ≤ i < len(s), s[i] == s[-i-1] .
    """

4- Vérifier si une chaîne de caractères est bien parenthésées :

"""
Toute parenthèse ouverte doit ensuite être fermée,
et une parenthèse ne peut pas être fermée si elle n’a pas 
été préalablement ouverte[#tip_bien_parenthesee].
 Le tableau ci-dessous donne des exemples de chaînes bien et mal parenthésées.

Bien parenthésées	Mal parenthésées
abc						(
(abc)					)
ab(cd)ef				abc)
a(b)c(d)e				ab)c
a((b)c)d				a(b(c)d
a(b(c()e)f)g	a(b)c)d(e)f

"""
def bien_parenthesee(txt):
    """
    :entrée txt: str
    :sortie bp: bool
    :post-cond: bp est True si et seulement si txt est bien parenthésée
    """