class Affichage:
    def __init__(self):
        self._ligne = "-------------------------------------------------\n"

    def ligne(self, nbr:int=1):
        print(self._ligne*nbr)

    def saut(self, nbr:int=1):
        print("\n"*nbr)

    def continuer(self, vide:bool=True):
        if vide:
            input()
        else:
            input("Appuyez sur 'Entrer' pour continuer...")

