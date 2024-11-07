import pygame
import sys

from board import Board

pygame.init()

SCREEN_WIDTH = 470
SCREEN_HEIGHT = 680

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

pygame.display.set_caption("Tic Tac Toe")

main_board = Board(screen)
can_play = True

while True:
    
    m_pos = pygame.mouse.get_pos()

    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0] and can_play:
                main_board.select(m_pos)
                main_board.set_value()

            elif pygame.mouse.get_pressed()[2]:
                main_board.reset()
                can_play = True
                 

    # update screen
    screen.fill((0, 0, 0))
    main_board.draw(m_pos)
    main_board.draw_cross()
    main_board.draw_zero()
    main_board.draw_cur_player()


    if main_board.game_over():
        can_play = False


    #update display
    pygame.display.update()

    #set max FPS to 60
    clock.tick(30)
