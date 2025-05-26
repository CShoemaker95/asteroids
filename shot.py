from circleshape import *

class Shot(CircleShape):
    containers = ()
    def __init__(self, x, y, velocity):
        SHOT_RADIUS = 5
        super().__init__(x, y, SHOT_RADIUS)
        self.velocity = velocity

    def update(self, dt):
        self.position += self.velocity * dt

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius)