# utils.py

# Fonctions utilitaires pour le chiffrement RSA
# Conversion, PRNG, génération de nombres premiers, etc.

# Dérivation simple d'une graine pseudo-aléatoire à partir du mot de passe (sans hashlib)
def derive_graine_depuis_mot_de_passe(mot_de_passe):
    graine = 0
    for i, caractere in enumerate(mot_de_passe):
        graine += (ord(caractere) ** 2) * (i + 1)
        graine = graine % (10**18)  # pour rester dans des bornes raisonnables
    return graine

# Générateur pseudo-aléatoire déterministe simple (congruence linéaire)
def generateur_pseudo_aleatoire(graine):
    a = 1103515245
    c = 12345
    m = 2 ** 31
    valeur = graine % m
    while True:
        valeur = (a * valeur + c) % m
        yield valeur

# Génération d'un nombre premier probabiliste (test de primalité naïf amélioré)
def generer_nombre_premier(bits, prng):
    while True:
        candidat = next(prng) | 1  # assure un nombre impair
        candidat = candidat % (2 ** bits)
        if est_premier(candidat):
            return candidat

# Test de primalité simple (Miller-Rabin recommandé pour production)
def est_premier(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

# PGCD (algorithme d'Euclide)
def pgcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Inverse modulaire (algorithme d'Euclide étendu)
def modinv(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        a, m = m, a % m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

# Conversion texte vers blocs entiers (pour RSA), avec vérification
def texte_vers_blocs(data, taille_bloc, n):
    blocs = []
    for i in range(0, len(data), taille_bloc):
        bloc = int.from_bytes(data[i:i+taille_bloc], byteorder='big')
        if bloc >= n:
            raise ValueError("Un bloc est trop grand pour être chiffré avec la clé RSA actuelle.")
        blocs.append(bloc)
    return blocs

# Conversion blocs entiers vers texte binaire
def blocs_vers_texte(blocs, taille_bloc):
    data = b''
    for bloc in blocs:
        data += bloc.to_bytes(taille_bloc, byteorder='big')
    return data

# Chiffrement simplifié d'une chaîne de caractères avec un mot de passe (XOR pseudo-aléatoire)
def chiffrer_texte_simple(texte, mot_de_passe):
    graine = derive_graine_depuis_mot_de_passe(mot_de_passe)
    prng = generateur_pseudo_aleatoire(graine)
    texte_bytes = texte.encode('utf-8')
    chiffre = bytearray()
    for b in texte_bytes:
        chiffre.append(b ^ (next(prng) % 256))
    return chiffre.hex()

# Déchiffrement de texte chiffré avec la même méthode
def dechiffrer_texte_simple(texte_chiffre_hex, mot_de_passe):
    graine = derive_graine_depuis_mot_de_passe(mot_de_passe)
    prng = generateur_pseudo_aleatoire(graine)
    texte_bytes = bytearray.fromhex(texte_chiffre_hex)
    dechiffre = bytearray()
    for b in texte_bytes:
        dechiffre.append(b ^ (next(prng) % 256))
    return dechiffre.decode('utf-8')
