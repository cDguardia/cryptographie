# chiffreur_dechiffreur.py

# Module de lecture de fichiers, conversion en blocs, chiffrement/déchiffrement RSA

from rsa import generer_cles_depuis_mot_de_passe, chiffrer_bloc, dechiffrer_bloc
from utils import texte_vers_blocs, blocs_vers_texte, chiffrer_texte_simple, dechiffrer_texte_simple
import os

# Taille du bloc à convertir en entier pour RSA (maximal = (n.bit_length() // 8) - 1)
def taille_bloc_maximale(n):
    return (n.bit_length() // 8) - 1

def chiffrer_fichier(chemin_entree, mot_de_passe, dossier_sortie="fichiers"):
    with open(chemin_entree, 'rb') as f:
        donnees = f.read()

    e, d, n = generer_cles_depuis_mot_de_passe(mot_de_passe)
    taille_bloc = taille_bloc_maximale(n)

    blocs = texte_vers_blocs(donnees, taille_bloc, n)
    blocs_chiffres = [chiffrer_bloc(b, e, n) for b in blocs]

    # Sauvegarde des blocs chiffrés sous forme binaire
    chemin_chiffre = os.path.join(dossier_sortie, "texte_chiffre.bin")
    with open(chemin_chiffre, 'w') as f:
        for bloc in blocs_chiffres:
            f.write(str(bloc) + '\n')

    # Chiffrement des clés avant sauvegarde
    cle_publique_texte = f"{e}\n{n}"
    cle_privee_texte = f"{d}\n{n}"

    cle_publique_chiffree = chiffrer_texte_simple(cle_publique_texte, mot_de_passe)
    cle_privee_chiffree = chiffrer_texte_simple(cle_privee_texte, mot_de_passe)

    with open(os.path.join("cles", "cle_publique.txt"), 'w') as f:
        f.write(cle_publique_chiffree)
    with open(os.path.join("cles", "cle_privee.txt"), 'w') as f:
        f.write(cle_privee_chiffree)

    return chemin_chiffre

def dechiffrer_fichier(chemin_chiffre, mot_de_passe, dossier_sortie="fichiers"):
    with open(chemin_chiffre, 'r') as f:
        lignes = f.readlines()
        blocs_chiffres = [int(l.strip()) for l in lignes]

    # Lecture des clés chiffrées et déchiffrement
    with open(os.path.join("cles", "cle_privee.txt"), 'r') as f:
        cle_privee_chiffree = f.read().strip()

    try:
        cle_privee = dechiffrer_texte_simple(cle_privee_chiffree, mot_de_passe)
        d, n = [int(x) for x in cle_privee.split('\n')]
    except:
        raise ValueError("Mot de passe incorrect ou clé invalide.")

    taille_bloc = taille_bloc_maximale(n)

    blocs_dechiffres = [dechiffrer_bloc(b, d, n) for b in blocs_chiffres]
    donnees_reconstituees = blocs_vers_texte(blocs_dechiffres, taille_bloc)

    chemin_dechiffre = os.path.join(dossier_sortie, "texte_dechiffre.txt")
    with open(chemin_dechiffre, 'wb') as f:
        f.write(donnees_reconstituees)

    return chemin_dechiffre
