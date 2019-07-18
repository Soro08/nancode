#Tableaux

I- Comparaisons et tests de tableaux

1-  Déterminer si deux tableaux sont identiques :

def tableaux_egaux(a, b):
    """
    :entrée a: tableau de float
    :entrée b: tableau de float
    :sortie te: bool
    :post-cond: te est True si et seulement si len(a) == len(b) et
                ∀ i ∈ [0;len(a)[, a[i] == b[i]

    >>> tableaux_egaux([1.0, 2.0, 4.0, 3.0], [1.0, 2.0, 4.0, 3.0])
    True
    >>> tableaux_egaux([1.0, 2.0, 4.0, 3.0], [9.0, 2.0, 4.0, 3.0])
    False
    >>> tableaux_egaux([1.0, 2.0, 4.0, 3.0], [1.0, 2.0, 4.0])
    False
    >>> tableaux_egaux([1.0, 2.0, 4.0], [1.0, 2.0, 4.0, 3.0])
    False
    """

2- Déterminer si le tableau b est un prefixe du tableau a :

def tableau_prefixe(a, b):
    """
    :entrée a: tableau de float
    :entrée b: tableau de float
    :sortie te: bool
    :post-cond: te est True si et seulement si len(a) >= len(b) et
                ∀ i ∈ [0;len(b)[, a[i] == b[i]

    >>> tableaux_prefixe([1.0, 2.0, 4.0, 3.0], [1.0, 2.0, 4.0, 3.0])
    True
    >>> tableaux_prefixe([1.0, 2.0, 4.0, 3.0], [9.0, 2.0, 4.0, 3.0])
    False
    >>> tableaux_prefixe([1.0, 2.0, 4.0, 3.0], [1.0, 2.0, 4.0])
    True
    >>> tableaux_prefixe([1.0, 2.0, 4.0], [1.0, 2.0, 4.0, 3.0])
    False
    """

3- Retourner True si et seulement si le tableau a est un Palindrome :

def tableau_palindrome(a):
    """
    :entrée a: tableau d'int
    :sortie p: bool
    :post-cond: p est True si et seulement si
                ∀ i ∈ [0;len(a)[,  a[i] == a[len(a)-1-i]

    >>> tableau_palindrome([1, 2, 4, 3])
    False
    >>> tableau_palindrome([1, 2, 4, 2, 1])
    True
    >>> tableau_palindrome([1, 2, 2, 1])
    True
    >>> tableau_palindrome([4])
    True
    """
#####################################################################################################

II - Recherche de valeurs


1- Trouver l’indice du plus petit élément d’un tableau :

NB : si le tableau
contient plusieurs minima ex-aequo, cette spécification n’impose pas lequel doit être retourné.

def indice_min(a):
    """
    :entrée a: tableau de float
    :sortie imin: int
    :pré-cond: len(a) > 0
    :post-cond: ∀ i ∈ [0;len(a)[, a[imin] ≤ a[i]

    >>> indice_min([2.0, 1.0, -3.0, 7.0, 3.0, 5.0, 1.0])
    2
    >>> indice_min([2.0, 1.0, -3.0, 7.0, -3.0, 5.0, 1.0])
    2
    >>> # mais 4 est aussi une réponse correcte
    """


2- Trouver l’indice de la n-ème occurence de v dans un tableau :


def indice_n(a, v, n):
    """
    :entrée a: tableau de float
    :entrée v: float
    :entrée n: int
    :sortie ival: int
    :pré-cond: n > 0
    :post-cond: si v apparaît au moins n fois dans a,
                alors a[ival] = v,
                   et a[0:ival] contient v exactement n-1 fois,
                sinon ival = -1

    >>> indice_n([2.0, 1.0, -3.0, 7.0, 3.0, 7.0, 1.0], 2.0, 1)
    0
    >>> indice_n([2.0, 1.0, -3.0, 7.0, 3.0, 7.0, 1.0], 2.0, 2)
    -1
    >>> indice_n([2.0, 1.0, -3.0, 7.0, 3.0, 7.0, 1.0], 7.0, 1)
    3
    >>> indice_n([2.0, 1.0, -3.0, 7.0, 3.0, 7.0, 1.0], 7.0, 2)
    5
    >>> indice_n([2.0, 1.0, -3.0, 7.0, 3.0, 7.0, 1.0], 7.0, 3)
    -1
    >>> indice_n([2.0, 1.0, -3.0, 7.0, 3.0, 7.0, 1.0], 9.0, 1)
    -1
    >>> indice_n([2.0, 1.0, -3.0, 7.0, 3.0, 7.0, 1.0], 9.0, 2)
    -1
    """

3- Compter le nombre d’occurences de v dans un tableau:

def nb_occurences(a, v):
    """
    :entrée a: tableau de float
    :entrée v: float
    :sortie n: int
    :post-conf: n = |{ i | i ∈ [0;len(a)[  et  a[i] = n }|

    >>> nb_occurences([2.0, 1.0, -3.0, 7.0, 3.0, 7.0, 1.0], 2.0)
    1
    >>> nb_occurences([2.0, 1.0, -3.0, 7.0, 3.0, 7.0, 1.0], 7.0)
    2
    >>> nb_occurences([2.0, 1.0, -3.0, 7.0, 3.0, 7.0, 1.0], 9.0)
    0
    """
##################################################################################################

III- Calculs sur les valeurs

1- Calculer la somme des éléments d’un tableau :

def somme(a):
    """
    :entrée a: tableau de float
    :sortie s: float
    :pré-cond: len(a) > 0
    :post-cond: s = Σ a[i]  pour  i ∈ [0;len(a)[

    >>> somme([2.0, 1.0, -3.0, 7.0, 3.0, 7.0, 1.0])
    18.0
    """
2- Calculer la moyenne des éléments d’un tableau :

def moyenne(a):
    """
    :entrée a: tableau de float
    :sortie m: float
    :pré-cond: len(a) > 0
    :post-cond: s est la moyenne des éléments de a

    >>> moyenne([2.0, 1.0, -3.0, 7.0, 3.0, 7.0, 1.0])
    2.5714285714285716
    """
3- Calculer la moyenne pondérée des éléments d’un tableau :

def moyenne_ponderee(a):
    """
    :entrée a: tableau de float
    :entrée poids: tableau de float
    :sortie mp: float
    :pré-cond: len(a) > 0,  len(poids) == len(a),  somme(poids) != 0
    :post-cond: s est la moyenne pondérée des éléments de a telle que
                ∀ i ∈ [0;len(a)[,  a[i] est pondérée par poids[i]

    >>> moyenne_ponderee([10.0, 12.0, 7.0], [1.0, 2.0, 1.0])
    10.25
    """

###################################################################################################

IV- Génération et modification de tableaux

1- Retourner un tableau contenant les n premiers nombres premier :


On rappelle qu’un nombre premier admet exactement deux diviseurs : 1 et lui même.

Par exemple, premiers(10) retournera le tableau [2,3,5,7,11,13,17,19,23,29].

def premiers(n):
    """
    :entrée n: int
    :sortie a: tableau d'int
    :pré-cond: n > 0
    :post-cond: len(a) == n
                ∀ i ∈ [0;n[,  a[i] est le (i+1)-ème nombre premier
    >>> premiers(3)
    array([2, 3, 5])
    >>> premiers(10)
    array([2, 3, 5, 7, 11, 13, 17, 19, 23, 29])
    """



2-  Retourner un tableau contenant les n premiers termes de la suite de Fibonacci :

    












































