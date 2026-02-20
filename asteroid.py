import pygame
import random
from circleshape import CircleShape
from constants import *
from logger import log_event

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += (self.velocity * dt) 

    #asteroid sizes = large, med, small, we split med and large, and destroy small
    def split(self):
        self.kill() # destroy itself ...
        if self.radius <= ASTEROID_MIN_RADIUS: #is asteroid smallest size?
            return 
        else: #spawn new asteroids
            log_event("asteroid_split")
            rand_angle = random.uniform(20, 50) #generate random angle between 20 and 50 degrees
            new_ast_1_vector = self.velocity.rotate(rand_angle) #rotate new asteroid vector
            new_ast_2_vector = self.velocity.rotate(-rand_angle) #rotate other new asteroid vector in opposite direction
            new_asts_radius = self.radius - ASTEROID_MIN_RADIUS
            new_ast_1 = Asteroid(self.position.x, self.position.y, new_asts_radius)
            new_ast_2 = Asteroid(self.position.x, self.position.y, new_asts_radius)
            new_ast_1.velocity = new_ast_1_vector * 1.2
            new_ast_2.velocity = new_ast_2_vector * 1.2