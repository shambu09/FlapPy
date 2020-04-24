import pygame


class Pipe(object):
    def __init__(self, x, y, pipe):
        self.x = x
        self.y = y
        self.gap = 120
        self.pipe = pipe
        self.downH = 512 - (self.y + 108)
        self.upH = self.downH - self.gap
        self.Hoff = -(self.pipe.get_height() - self.upH)

    def show(self, win):
        win.blit(self.pipe, (self.x, self.downH))
        win.blit(pygame.transform.flip(
            self.pipe, False, True), (self.x, self.Hoff))

    def update(self):
        self.x -= 3

    def OUT(self):
        return self.x + 50 <= 0

    def rect1(self):
        return pygame.Rect(self.x, self.downH, self.pipe.get_width(), self.y)

    def rect2(self):
        return pygame.Rect(self.x, 0, self.pipe.get_width(), self.upH)

    def score(self):
        return pygame.Rect(self.x + self.pipe.get_width(), self.upH, 0, self.gap)


class Foot(object):
    def __init__(self, x, foot):
        self.x = x
        self.foot = foot

    def show(self, win):
        win.blit(self.foot, (self.x, 512 - self.foot.get_height()))

    def update(self):
        self.x -= 3

    def OUT(self):
        return self.x + 336 <= 0


class Flappy(object):
    def __init__(self, y, bird, image):
        self.y = y
        self.m = 1
        self.speed = 6
        self.v = 55
        self.voff = 40
        self.bird = bird
        self.imageU = []
        self.imageD = []
        self.life = True
        self.Up = True
        self.score = 0
        self.scoreArray = []
        for i in range(len(image)):
            self.imageU.append(pygame.transform.rotate(image[i], 45))
            self.imageD.append(pygame.transform.rotate(image[i], -45))

    def show(self, win):
        win.blit(self.bird, (50, self.y))
        return win.blit(self.bird, (50, self.y))

    def Jump(self):
        F = 0.5 * self.m * (self.v**2) * 0.014
        self.y -= F

    def rect(self):
        return pygame.Rect(50, self.y, self.bird.get_width() - 15, self.bird.get_height() - 15)

    def gravity(self):
        F = -(0.5 * self.m * (self.v**2)) * 0.007
        self.y -= F
