import math

class Vector2D:
    def __init__(self, x, y):
        self.X = x
        self.Y = y

    def get_module(self):
        return math.sqrt(self.X*self.X + self.Y*self.Y)

    def make_single(self):
        return Vector2D.scalar_mult(self, 1/self.get_module())

    @staticmethod
    def sum (vector1, vector2):
        return Vector2D(vector1.X+vector2.X, vector1.Y+vector2.Y)

    @staticmethod
    def diff(vector1, vector2):
        return Vector2D(vector1.X - vector2.X, vector1.Y - vector2.Y)

    @staticmethod
    def scalar_mult(vector, scalar):
        return Vector2D(vector.X*scalar, vector.Y*scalar)

    @staticmethod
    def get_distance(vector1, vector2):
        return Vector2D.diff(vector1, vector2).get_module()

class CircleCollider():
    def __init__(self, r, center):
        self.radius = r
        self.center = center

    @staticmethod
    def is_intersects(circle1, circle2):
        #print(circle1.center)
        #print(circle2.center)
        return circle1.radius+circle2.radius >= Vector2D.get_distance(circle1.center, circle2.center)