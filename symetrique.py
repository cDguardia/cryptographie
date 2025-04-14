import os 


def manip_message(methode, message):
    if methode == 1:
        return message
    else:
        try:
            with open(message, "rb") as f:
                return f.readlines()
        except Exception as e:
            return e


def vigenere(message, key):
    
    
    pass



def no_xor_function(message, key):
    
    
    pass

def xor_function(message, key):
    
    
    
    pass







def main():
    

    if 1 :
        # Choix du message et de la clef -----------------------------------------------------------------
        message = int(input("Choisis si c'est une chaine de caractere : 1, ou un fichier : 2"))
        

        # Entrer un message à la main
        if message == 1:
            message = input("Entrez votre message : ")
            manip_message(1, message)

        # Entrer un chemin vers un fichier en .txt
        elif message == 2:
            message = input("Entrez votre chemin de fichier : ")
            message = manip_message(2, message)
            if "Error" in  manip_message:
                print("Mauvais chemin de fichier.")
                main()
                return None
        
        # En cas de mauvaise entrée
        else:
            print("Mauvaise entrée.")
            main()
            return None
        

        # Algorithme de chiffrement ------------------------------------------------------------------------


        key = input("Entrez une clef : ")
        cipher_text = xor_function(message, key)
        print(f"Message chiffré : {cipher_text} / Clé : {key}")

        # Algorithme de déchiffrement ----------------------------------------------------------------------

        message_chiffre = input("Entrez votre message chiffré : ")
        key = input("Entrez une clef : ")
        cipher_text = no_xor_function(message_chiffre, key)
        print(f"Message déchiffré : {cipher_text}")

    if 2 :


main()