from game_object import GameObject
from objects.paddle import Paddle
from pygame.surface import Surface
from objects.ball import Ball

# Une classe qui va gérer la logique du jeu
class Game(GameObject):
    # On crée nos objets
    ball = Ball()
    player_paddle = Paddle(ball, True)
    enemy_paddle = Paddle(ball, False)

    # Indique si la boucle de jeu doit tourner ou non
    should_run = True

    # Lance les init de chaque objet au démarrage du jeu
    def init(self, screen: Surface):
        self.ball.init(screen)
        self.player_paddle.init(screen)
        self.enemy_paddle.init(screen)

    # Lance les update de chaque objet à chaque frame et gère la 
    # relation entre les objets
    def update(self, screen: Surface):
        self.ball.update(screen)
        self.player_paddle.update(screen)
        self.enemy_paddle.update(screen)

        # Si la balle touche un coté de l'écran, c'est perdu !
        if (self.ball.is_touching_x_side(screen)):
            # On stop le jeu comme un gros crado
            # TODO: Faire plus propre, pourquoi pas ? ;)
            self.should_run = False

        # Si la balle touche une raquette, sa direction s'inverse, elle rebondit
        if (
            self.ball.is_touching_rect(self.player_paddle.as_rect())
            or self.ball.is_touching_rect(self.enemy_paddle.as_rect())
        ):
            self.ball.dir.x = -self.ball.dir.x
