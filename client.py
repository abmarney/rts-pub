import pygame
from network import Network

# Creates and displays a new game window with given width and height.
width = 500
height = 500
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")

# Updates the game window after rebuilding with new object information.
#   window = the game window
#   player, player2 = the individual players in the game
#
def redrawWindow(window, player, player2):
    window.fill((255,255,255))
    player.draw(window)
    player2.draw(window)
    pygame.display.update()

# The main client instance of a players game. Handles game behavior based off of user input.
#   
def main():
    run = True
    network = Network()
    player = network.get_player()
    clock = pygame.time.Clock()
    position = player.get_player_spawn_position()
    while run:
        clock.tick(60)
        player2 = network.send(player)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 3:
                    position = pygame.mouse.get_pos()
                elif event.button == 1:
                    player.select_unit(pygame.mouse.get_pos())
                    if player.selected_unit:
                        position = player.selected_unit.get_unit_position()
            if event.type == pygame.KEYDOWN:
                if event.key == 115:
                    player.spawn_unit()
        player.move(position)

        redrawWindow(window, player, player2)

main()