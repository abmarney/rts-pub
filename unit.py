import pygame

# A class that handles the unit object.
class Unit:

    # Initializes a unit object.
    #   x,y = the unit's coordinates within the game window
    #   color = the unit's color
    #
    def __init__(self, x, y, color):
        self.x = x
        self.x_target = x
        self.y = y
        self.y_target = y
        self.velocity = 1
        self.body = (self.x,self.y,10,10)
        self.color = color
        self.rect = None
    
    # Draws the unit on the game window.
    #   window = the game window
    #
    def draw(self, window):
        self.rect = pygame.draw.rect(window, self.color, self.body)

    # Moves the unit based on it's relation to the target coordinates and velocity.
    #
    def move(self):
        if abs(self.x_target - self.x) < self.velocity:
            self.x = self.x_target
        elif self.x_target < self.x:
            self.x -= self.velocity
        elif self.x_target > self.x:
            self.x += self.velocity
        if abs(self.y_target - self.y) < self.velocity:
            self.y = self.y_target
        elif self.y_target < self.y:
            self.y -= self.velocity
        elif self.y_target > self.y:
            self.y += self.velocity
        
        self.update()

    # Updates the unit's display properties.
    #
    def update(self):
        self.body = (self.x,self.y, 10, 10)

    # Returns the unit's target position.
    #
    def get_unit_position(self):
        return [self.x_target, self.y_target]

    # Updates the unit's target positioin.
    #   target_position = the position this unit is moving to
    #
    def update_unit_target_position(self, target_position):
        self.x_target = target_position[0]
        self.y_target = target_position[1]