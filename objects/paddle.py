from pygame import key, Rect, Surface, Vector2, draw
from pygame.constants import K_DOWN, K_UP
from game_object import GameObject
from objects.ball import Ball

# Définition de la classe Paddle
class Paddle(GameObject):

    # Constructeur de la classe
    def __init__(self, ball: Ball = None, is_player = True):
        # Position de la raquette
        self.pos = Vector2(0, 0)
        # Dimensions de la raquette
        self.rect = Vector2(5, 100)
        # La raquette est controlée par le joueur ? O/N
        self.is_player = is_player
        # Quelle est la balle du jeu (pour l'IA)
        self.ball = ball
        # Vitesse de déplacement de la raquette
        self.speed = 0.5

    # Méthode d'initialisation de l'objet, à exécuter une fois au début
    def init(self, screen: Surface):
        if self.is_player:
            # Si la raquette est controllée par le joueur
            # elle se place à gauche de l'écran
            self.pos.x = self.rect.x
            self.pos.y = self.rect.y
        else:
            # Sinon elle se place à droite
            self.pos.x = screen.get_width() - self.rect.x
            self.pos.y = self.rect.y

    # Méthode de mise à jour de l'objet, à exécuter à chaque image
    def update(self, screen: Surface):
        # Il existe une fonction par type de joueur, manuel ou IA
        if (self.is_player):
            self.manual_control(screen)
        else:
            self.automatic_control()

        # Maintenant que les coordonées ont changés, on dessine la raquette
        draw.rect(screen, (255,255,255), self.as_rect())

    def manual_control(self, screen: Surface):
        # Si on appuis sur la flèche du haut et qu'on a pas dépassé le haut
        # de l'écran, on monte de "speed" pixels par frame
        if (key.get_pressed()[K_UP] and self.pos.y > 0):
            self.pos.y = self.pos.y - self.speed

        # On calcul le bas de la raquette
        bottom = self.pos.y + self.rect.y

        # Si on appuis sur la flèche du bas et qu'on a pas dépassé le bas
        # de l'écran, on descend de "speed" pixels par frame
        if (key.get_pressed()[K_DOWN] and bottom < screen.get_height()):
            self.pos.y = self.pos.y + self.speed

    # Imbattable, la raquette suis la balle directement sans faute
    def automatic_control(self):
        if (self.ball != None):
            self.pos.y = self.ball.pos.y - (self.rect.y/2)

    # Retourne un Rect de PyGame pour gérer les dessins et les collisions
    def as_rect(self):
        # Pour créer un Rect il faut donner deux vecteur
        # Le premier est le vecteur de position du coin haut/gauche, notre pos
        # Le second est le vecteur de taille, largeur/hauteur, notre rect
        return Rect(self.pos, self.rect)
