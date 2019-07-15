# I - Mathematique Géométrie

"""
1 
Calculer le diamètre, le périmètre et la surface d’un cercle à partir de son rayon :
"""

def dia_cercle(r):
    """
    :entrée r: float
    :sortie (d, p, s): tuple
    
    :pré-cond: r ≥ 0
    :post-conf: d contient le diamètre d'un cercle de centre r,
                p contient le périèmtre d'un cercle de centre r,
                s contient la surface d'un cercle de centre r
    """

"""

Calculer les coefficients d’une droite à partir de deux points :

"""

def coef_droite(x1, y1, x2, y2):
    """
    :entrée x1: float
    :entrée y1: float
    :entrée x2: float
    :entrée y2: float
    :sortie a: float
    :sortie b: float
    :pré-cond: les deux points de coordonnées (x1, y1) et (x2, y2)
               sont distincts et ne sont pas alignés verticalements,
               autrement dit x1 ≠ x2
    :post-cond: a et b sont les coefficients de la droite passant par
                les deux points de coordonnées (x1, y1) et (x2, y2),
                autrement dit y1 = a×x1 + b et y2 = a×x2 + b

    """


# II - Conditions et calcul
"""
1  Calculer le plus petit parmi trois nombres :
"""
def plus_petit(a, b, c):
    """
    :entree a: int
    :entree b: int
    :entree c: int
    :sortie pp: int
    :pré-cond: (aucune)
    :post-cond: pp = le plus petit nombre de l'ensemble {a, b, c}
    """

"""

2 Calculer si elles existent les racines d’une équation du second degré :
NB: pour calculer les racines, il est nécessaire de calculer une racine carrée.
On pourra pour cela utiliser la fonction racine_carree ci-dessous ou la
fonction sqrt fournie par Python (inclure la ligne from math import sqrt en haut de votre programme).
"""

def racines_2nd_degre(a, b, c):
    """
    :entrée a: float
    :entrée b: float
    :entrée c: float
    :sortie (r1,r2): tuple
   
    :pré-cond: a ≠ 0
    :post-cond: si l'équation ax²+bx + c n'a pas de racine réelle,
                r1 = r2 = None,
                sinon, si elle a exactement une racine réelle,
                r1 a pour valeur cette racine et r2 = None,
                sinon (l'équation a deux racine réelles),
                r1 et r2 ont pour valeur ces deux racines,
                avec r1 > r2
    """

# III -  Durées et dates

"""
1 Convertir une durée en secondes :
"""

def duree_en_secondes(j, h, m, s):
    """
    :entrée j: int
    :entrée h: int
    :entrée m: int
    :entrée s: float
    :sortie ds: float
    :pré-cond: j > 0 , 0 ≤ h < 24 , 0 ≤ m < 60, 0 ≤ s < 60
    :post-cond: ds est le nombre de secondes correspond à
                une durée de j jours, h heures, m minutes et s secondes.
    """
"""
2 Calculer la différence entre deux heures de la journée :

Variante : relâcher la contrainte sur l’ordre des heures de la journée passées en entrée,
en retournant une valeur négative si la première est antérieure à la deuxième.
"""
def difference_heures(h1, m1, s1, h2, m2, s2):
    """
    :entrée h1: int
    :entrée m1: int
    :entrée s1: int
    :entrée h2: int
    :entrée m2: int
    :entrée s2: int
    :sortie d: int
    :pré-cond: 0 ≤ h1 < 24 , 0 ≤ m1 < 60 , 0 ≤ s1 < 60 ,
               0 ≤ h2 < 24 , 0 ≤ m2 < 60 , 0 ≤ s2 < 60 ,
               ordre_heures(h1, m1, s1, h2, m2, s2) ≥ 0
    :post-cond: d est le nombre de secondes entre h2:m2:s2 et h1:m1:s1 .
    """

"""
3  Déterminer si une année est bissextile :
NB : on rappelle que les années bissextiles sont

	les années multiples de 4,
	sauf les années multiples de 100 qui ne le sont pas,
	sauf les années multiples de 400 qui le sont tout de même.
"""
def annee_bissextile(a):
    """
    :entrée a: int
    :sortie b: bool
    :pré-cond: a > 0
    :post-cond: b est True ssi l'année a est bissextile.
    """

"""
4 Déterminer le nombre de jours d’une année donnée :

NB : attention aux années bissextiles –voir l’exercie annee_bissextile.
"""

def jours_par_annee(a):
    """
    :entrée a: int
    :sortie j: int
    :pré-cond: a > 0
    :post-cond: j est le nombre de jour de l'année a.
    """


"""
5 Déterminer le nombre de jours d’un mois :
"""

def jours_par_mois(m):
    """
    :entrée m: int
    :sortie j: int
    :pré-cond: 1 ≤ m ≤ 12
    :post-cond: j est le nombre de jour du m-ième mois
                d'une année non bissextile.
    """

"""
6 Déterminer le nombre de jours d’un mois d’une année donnée 

NB : attention aux années bissextiles –voir l’exercie annee_bissextile.
"""
def jours_par_annee_mois(a, m):
    """
    :entrée a: int
    :entrée m: int
    :sortie j: int
    :pré-cond: a > 0 , 1 ≤ m ≤ 12
    :post-cond: j est le nombre de jour du m-ième mois de l'année a.
    """

"""

"""

