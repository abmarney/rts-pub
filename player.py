import pygame
from unit import Unit

# A class that handles all player information and manipulation.
#
class Player:

    # Initalizes the player object.
    #   spawn_x, spawn_y = the location new units are created at
    #   color = the default color for this player's units
    #   selected_color = the default color for a player's unit when it is selected.
    #
    def __init__(self, spawn_x, spawn_y, color, selected_color):
        self.spawn_x = spawn_x
        self.spawn_y = spawn_y
        self.color = color
        self.selected_color = selected_color
        self.units = []
        self.selected_unit = None

    # Updates the individual unit object on the game screen.
    #   window = the game window
    #
    def draw(self, window):
        for unit in self.units:
            unit.draw(window)

    # Returns the player's current spawn position.
    #
    def get_player_spawn_position(self):
        return [self.spawn_x, self.spawn_y]

    # Updates a selected unit's target position and handles unit movement.
    #   target_position = the x,y coordinates the unit will travel to
    #
    def move(self, target_position):
        if self.selected_unit != None:
            self.selected_unit.update_unit_target_position(target_position)
        for unit in self.units:
            unit.move()

    # Spawns a unit at the current player spawn location and adds it to the list of units.
    #
    def spawn_unit(self):
        self.units.append(Unit(self.spawn_x, self.spawn_y, self.color))

    # Selects a unit and handles color shifting behavior.
    #   position = the position of the cursor to check for unit collision.
    #
    def select_unit(self,position):
        for unit in self.units:
            if unit.rect.collidepoint(position):
                if self.selected_unit is not None:
                    self.selected_unit.color = self.color
                self.selected_unit = unit
                self.selected_unit.color = self.selected_color
                return
        if self.selected_unit is not None:
            self.selected_unit.color = self.color
        self.selected_unit == None
                
