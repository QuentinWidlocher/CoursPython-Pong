from pygame.surface import Surface

# Objet vide qui va servir d'interface aux objets de jeu
class GameObject():

    # Un objet de jeu possède une méthode init qui devra être
    # lancé une seule fois au démarrage du jeu
    def init(self, screen: Surface):
        # Si on n'a pas utilisé de polymorphisme pour implémenter
        # cette méhode, comme on devrait le faire avec une interface,
        # on lance une erreur
        raise NotImplementedError()
    
    # Un objet de jeu possède une méthode update qui devra être
    # lancé à chaque frame du jeu
    def update(self):
        # Si on n'a pas utilisé de polymorphisme pour implémenter
        # cette méhode, comme on devrait le faire avec une interface,
        # on lance une erreur
        raise NotImplementedError()
