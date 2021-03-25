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
        self.size = Vector2(5, 100)
        # La raquette est controlée par le joueur ? O/N
        self.is_player = is_player
        # Quelle est la balle du jeu (pour l'IA)
        self.ball = ball
        # Vitesse de déplacement de la raquette
        self.speed = 0.5

    # Méthode d'initialisation de l'objet, à exécuter une fois au début
    def init(self, screen: Surface):

        self.screen = screen

        if self.is_player:
            # Si la raquette est controllée par le joueur
            # elle se place à gauche de l'écran
            self.pos.x = self.size.x
            self.pos.y = self.size.y
        else:
            # Sinon elle se place à droite
            self.pos.x = screen.get_width() - self.size.x
            self.pos.y = self.size.y

    # Méthode de mise à jour de l'objet, à exécuter à chaque image
    def update(self):
        # Il existe une fonction par type de joueur, manuel ou IA
        if (self.is_player):
            self.manual_control()
        else:
            self.automatic_control()

        # Maintenant que les coordonées ont changés, on dessine la raquette
        draw.rect(self.screen, (255,255,255), self.as_rect())

    def manual_control(self):
        # Si on appuis sur la flèche du haut et qu'on a pas dépassé le haut
        # de l'écran, on monte de "speed" pixels par frame
        if (key.get_pressed()[K_UP] and self.pos.y > 0):
            self.pos.y -= self.speed

        # On calcule le bas de la raquette
        bottom = self.pos.y + self.size.x

        # Si on appuis sur la flèche du bas et qu'on a pas dépassé le bas
        # de l'écran, on descend de "speed" pixels par frame
        if ((key.get_pressed()[K_DOWN]) and (bottom < self.screen.get_height())):
            self.pos.y += self.speed

    # Imbattable, la raquette suis la balle directement sans faute
    def automatic_control(self):
        if (self.ball != None):
            self.pos.y = self.ball.pos.y - (self.size.x/2)

    # Retourne un rectangle aux dimensions et position de la raquette
    def as_rect(self):
        return Rect(self.pos, self.size)
