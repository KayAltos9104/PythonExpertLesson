import physics
from physics import *


class Parent:
    def __init__(self, pos):
        self.pos = pos

    def update(self):
        pass


class Character(Parent):
    def __init__(self, pos, size, color):
        super().__init__(pos)
        self.collider = CircleCollider(center=pos, r=size)
        self.sprite = color
        self.speed = Vector2D(0, 0)

    def move(self):
        self.pos = \
        Vector2D.sum(self.pos, self.speed)
        self.collider.center = self.pos

    def update(self):
        self.move()