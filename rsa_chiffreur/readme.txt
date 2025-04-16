# Projet : Chiffrement de fichiers RSA avec interface graphique

## 🔐 Description
Ce projet est une application Python permettant de chiffrer et déchiffrer n'importe quel fichier (texte, image, etc.) à l'aide de l'algorithme RSA. L'utilisateur définit son propre mot de passe, à partir duquel les clés sont dérivées. L'interface graphique intuitive permet de manipuler les fichiers sans ligne de commande.

Le chiffrement est entièrement fait **sans aucune bibliothèque externe**, pour une meilleure compréhension des mécanismes internes.

---

## 💾 Fonctionnalités
- Génération de clés RSA à partir d'un mot de passe
- Chiffrement/déchiffrement de n'importe quel fichier
- Interface graphique avec Tkinter
- Protection des clés RSA par chiffrement dérivé du mot de passe
- Barre de progression de l'opération

---

## 📁 Structure du projet
```
rsa_chiffreur/
├── main.py                # Interface graphique
├── rsa.py                 # Logique RSA (génération, chiffrement, déchiffrement)
├── utils.py               # Fonctions utilitaires : PRNG, KDF, conversions, XOR
├── chiffreur_dechiffreur.py  # Traitement de fichiers et clés
├── fichiers/              # Dossier de sortie pour les fichiers chiffrés/déchiffrés
└── cles/                  # Contient les clés RSA chiffrées avec le mot de passe
```

---

## ⚙️ Installation et exécution
**Prérequis** : Python 3 (aucune bibliothèque externe requise)

```bash
python main.py
```

---

## 🤔 Fonctionnement
1. L'utilisateur entre un **mot de passe personnel**.
2. Il choisit un fichier à chiffrer.
3. Le programme :
   - Dérive une graine à partir du mot de passe
   - Génère les clés RSA
   - Chiffre le fichier par blocs entiers
   - Chiffre les clés RSA avec le mot de passe et les stocke dans `/cles`

Pour déchiffrer, le programme utilise le fichier `.bin` et la clé privée protégée. Le bon mot de passe est nécessaire pour réussir.

---

## ⚠️ Limitations
- Pas adapté pour des fichiers très volumineux (RSA est lent pour ça)
- Pas de vérification d'intégrité ou de signature numérique
- Algorithme de protection des clés simple (XOR pseudo-aléatoire)

---

## 🚀 Idées d'évolution
- Intégration d'un journal de logs des opérations
- Ajout de signature numérique pour authentifier l'expéditeur
- Passage à un modèle hybride RSA + chiffrement symétrique (AES fait maison)
- Export/Import des clés sous format portable (base64 ou hex)

---

## ✅ Auteur
Projet conçu avec amour, rigueur et algorithmes ♥

---

## 🔧 Licence
Projet libre d'utilisation et d'étude, dans un cadre personnel ou pédagogique.

