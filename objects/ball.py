from game_object import GameObject
from pygame import Rect, Surface, Vector2, draw

# Définition de la classe Ball
class Ball(GameObject):

    # Constructeur de la classe
    def __init__(self, pos=Vector2(0, 0)):
        # La position de la balle (Vecteur)
        self.pos = pos
        # La direction de la balle (Vecteur normalisé)
        self.dir = Vector2(1, 1)
        # La vitesse de déplacement de la balle
        self.speed = 0.3
        # Le diamètre de la balle en pixel
        self.size = 5

    # Méthode d'initialisation de l'objet, à exécuter une fois au début
    def init(self, screen: Surface):
        self.screen = screen
        # On place la balle au centre de l'écran
        self.pos = Vector2(screen.get_width()/2, screen.get_height()/2)

    # Méthode de mise à jour de l'objet, à exécuter à chaque image
    def update(self):

        # Si la balle va sortir de l'écran verticalement
        if (self.is_touching_y_side()):

            # On la remet à la bordure la plus proche (haut ou bas)
            self.pos.y = min(self.pos.y, self.screen.get_height())
            self.pos.y = max(self.pos.y, 0)

            # On inverse sa direction pour faire un rebond
            self.dir.y = -self.dir.y

        # Maintenant qu'on a calculé la direction, on fait bouger la balle
        # dans cette direction, à raison de "speed" pixels par frame
        self.pos = Vector2(
            self.pos.x + (self.dir.x * self.speed),
            self.pos.y + (self.dir.y * self.speed)
        )

        # On dessine un cercle là où se tient la balle
        draw.circle(self.screen, (255, 255, 255), self.pos, self.size)

    # Retourne True si la balle touche le coté gauche ou droit de l'écran
    def is_touching_x_side(self):
        return (self.pos.x < 0 or self.pos.x > self.screen.get_width())

    # Retourne True si la balle touche le coté haut ou bas de l'écran
    def is_touching_y_side(self):
        return (self.pos.y < 0 or self.pos.y > self.screen.get_height())

    # Retourne True si la balle touche un rectangle
    def is_touching_rect(self, rect: Rect):
        # Pour ça on crée un rectangle aux même dimensions et position que le cercle
        return rect.colliderect(Rect(self.pos, Vector2(self.size)))
