

def key_format(key):
    if len(key) < 16:
        miss_char = 16 - len(key)  
        


# regarder ceci pour vous inspiré il y a une entrée utilisateur la clé et ensuite il est transformer en une clé constante dans un seul format

# Constantes de SHA-256
K = [
    0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5, 0x3956c25b, 0x59f111f1, 0x923f82a4, 0xab1c5ed5,
    0xd807aa98, 0x12835b01, 0x243185be, 0x550c7dc3, 0x72be5d74, 0x80deb1fe, 0x9bdc06a7, 0xc19bf174,
    0xe49b69c1, 0x319b7ee4, 0x2b8a3d2f, 0x808a2f9b, 0x04b1f0ad, 0xd56fbd49, 0x38490f44, 0x60f6b0b2,
    0xe8d43606, 0xc70129bd, 0x31c8b968, 0x6886c048, 0x2ab9b88e, 0x4b6f7b4e, 0x5e4c7e9d, 0xd070b2e5,
    0x6a5f5375, 0x9f2b55a7, 0x9a0f72c7, 0x3f92a9a4, 0x8d31411b, 0x7f49b5ed, 0x1d14ecb2, 0x228442cb
]

# Initialisation des valeurs H0, H1, H2, ..., H7
H0 = 0x6a09e667
H1 = 0xbb67ae85
H2 = 0x3c6ef372
H3 = 0xa54ff53a
H4 = 0x510e527f
H5 = 0x9b05688c
H6 = 0x1f83d9ab
H7 = 0x5be0cd19

# Fonction de rotation à gauche
def rotate_left(x, n):
    return ((x << n) | (x >> (32 - n))) & 0xFFFFFFFF

# Prétraitement du message (padding et ajout de la longueur)
def pad_message(message):
    # Convertir le message en binaire
    message_bin = ''.join(format(byte, '08b') for byte in message.encode('utf-8'))
    
    # Longueur originale du message en bits
    original_len = len(message_bin)
    
    # Ajouter le bit "1"
    message_bin += '1'
    
    # Compléter avec des zéros jusqu'à ce que la longueur soit 448 mod 512
    while len(message_bin) % 512 != 448:
        message_bin += '0'
    
    # Ajouter la longueur originale du message (64 bits)
    message_bin += format(original_len, '064b')
    
    # Diviser en blocs de 512 bits
    blocks = [message_bin[i:i+512] for i in range(0, len(message_bin), 512)]
    
    return blocks

# Traitement d'un bloc
def process_block(block, H0, H1, H2, H3, H4, H5, H6, H7):
    # Diviser le bloc en 16 mots de 32 bits
    words = [int(block[i:i+32], 2) for i in range(0, len(block), 32)]
    
    # Etendre à 64 mots
    for i in range(16, 64):
        words.append(rotate_left(words[i-2] ^ words[i-7] ^ words[i-15] ^ words[i-16], 1))
    
    # Initialiser les variables de travail
    a, b, c, d, e, f, g, h = H0, H1, H2, H3, H4, H5, H6, H7
    
    # Effectuer les 64 étapes de transformation
    for i in range(64):
        if i < 20:
            f = (b & c) | ((~b) & d)
            k = 0x5A827999
        elif i < 40:
            f = b ^ c ^ d
            k = 0x6ED9EBA1
        elif i < 60:
            f = (b & c) | (b & d) | (c & d)
            k = 0x8F1BBCDC
        else:
            f = b ^ c ^ d
            k = 0xCA62C1D6
        
        temp = (rotate_left(a, 5) + f + e + k + words[i]) & 0xFFFFFFFF
        e = d
        d = c
        c = rotate_left(b, 30)
        b = a
        a = temp
    
    # Ajouter les valeurs de hachage de la ronde à la valeur accumulée
    H0 = (H0 + a) & 0xFFFFFFFF
    H1 = (H1 + b) & 0xFFFFFFFF
    H2 = (H2 + c) & 0xFFFFFFFF
    H3 = (H3 + d) & 0xFFFFFFFF
    H4 = (H4 + e) & 0xFFFFFFFF
    H5 = (H5 + f) & 0xFFFFFFFF
    H6 = (H6 + g) & 0xFFFFFFFF
    H7 = (H7 + h) & 0xFFFFFFFF
    
    return H0, H1, H2, H3, H4, H5, H6, H7

# Fonction principale SHA-256
def sha256(message):
    # Prétraiter le message
    blocks = pad_message(message)
    
    # Variables de hachage initiales
    H0, H1, H2, H3, H4, H5, H6, H7 = H0, H1, H2, H3, H4, H5, H6, H7
    
    # Traitement des blocs
    for block in blocks:
        H0, H1, H2, H3, H4, H5, H6, H7 = process_block(block, H0, H1, H2, H3, H4, H5, H6, H7)
    
    # Résultat final : concaténer les résultats en hexadécimal
    result = ''.join(format(i, '08x') for i in [H0, H1, H2, H3, H4, H5, H6, H7])
    
    return result

# Demander à l'utilisateur d'entrer un message
message = input("Entrez un message à hacher avec SHA-256 : ")

# Calculer et afficher le haché SHA-256
print(f"SHA-256 : {sha256(message)}")