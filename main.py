import pygame
from pygame import display
from game import Game

def main():

    # On initialise PyGame
    pygame.init()
    display.set_caption("Pong")

    # Crée une surface sur l'écran
    screen = display.set_mode((800, 600))

    # On instancie notre objet qui va gérer les règles du jeu
    game = Game()

    # On lance l'initialisation du jeu
    game.init(screen)

    # Tant qu'on indique pas le contraire, on reste dans la boucle de jeu
    # Chaque tour de boucle représente une frame
    while game.should_run:

        # On efface l'ecran (on le rempli de noir, c'est pareil)
        screen.fill((0,0,0))

        # On lance la fonction update du jeu
        game.update(screen)

        # On met à jour l'affichage de l'écran pour afficher les modifs
        display.update()

        # On récupère tous les évènement de pygame
        for event in pygame.event.get():
            # On s'occupe uniquement de l'évènement QUIT (croix, alt+f4)
            if event.type == pygame.QUIT:
                # On met la variable running à False ce qui annule la boucle
                game.should_run = False


# On exécute la fonction main() uniquement si on lance le fichier main.py
# Si on importe le fichier main.py dans un autre fichier, __name__ ne
# sera pas égal à "__main__" et on n'exécutera pas le jeu
if __name__ == "__main__":
    main()
