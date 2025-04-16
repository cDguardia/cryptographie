# rsa.py

# Ce fichier contient les fonctions principales liées au système RSA
# Génération des clés (e, d, n), chiffrement et déchiffrement d'entiers

from utils import derive_graine_depuis_mot_de_passe, generateur_pseudo_aleatoire, generer_nombre_premier, pgcd, modinv

# Taille en bits des nombres premiers à générer (sécurité raisonnable)
TAILLE_CLE = 512

# Exposant public standard
EXPONENT_PUBLIC = 65537

def generer_cles_depuis_mot_de_passe(mot_de_passe):
    # Étape 1 : dériver une graine depuis le mot de passe
    graine = derive_graine_depuis_mot_de_passe(mot_de_passe)
    prng = generateur_pseudo_aleatoire(graine)

    # Étape 2 : générer deux grands nombres premiers distincts
    p = generer_nombre_premier(TAILLE_CLE, prng)
    q = generer_nombre_premier(TAILLE_CLE, prng)
    while p == q:
        q = generer_nombre_premier(TAILLE_CLE, prng)

    n = p * q
    phi = (p - 1) * (q - 1)

    e = EXPONENT_PUBLIC
    if pgcd(e, phi) != 1:
        raise ValueError("e et phi(n) ne sont pas premiers entre eux")

    d = modinv(e, phi)

    return (e, d, n)

def chiffrer_bloc(bloc, e, n):
    return pow(bloc, e, n)

def dechiffrer_bloc(bloc, d, n):
    return pow(bloc, d, n)
