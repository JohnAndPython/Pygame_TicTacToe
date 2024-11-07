import pygame
import random

class Board:
    def __init__(self, surf: pygame.Surface) -> None:
        self.surf = surf # Screen

        self.play_board = dict()

        # Fill dict with rects
        left, top, width, heigth = (0, 0, 150, 200)

        for key in range(1, 10):
            self.play_board[key] = pygame.rect.Rect(left, top, width, heigth)

            left += 160
            if key % 3 == 0:
                left = 0
                top += 210


        # Rect top left pos of a specific rect in self.play_board
        self.pos_xy_rect = None

        # Images
        self.cross_surf = pygame.image.load(r"Assets\Cross.png").convert()
        self.cross_surf.set_colorkey((255,255,255))
        self.lst_cross = [] #Reset

        self.zero_surf = pygame.image.load(r"Assets\Zero.png").convert()
        self.zero_surf.set_colorkey((255,255,255))
        self.lst_zeros = [] #Reset

        # Matrix / Reset
        self.matrix = [[None, None, None],
                       [None, None, None],
                       [None, None, None]]
        
        # Variables / Reset
        self.first_player = random.choice(["Player 1", "Player 2"])
        self.cur_player = self.first_player
        self.value = None # Value: 1 = Cross, 0 = Zero

        # Set with Numbers 1-9 / Reset
        self.open_fields = set(range(1, 10))
        self.number = None # Current Number

        #Reset
        if self.cur_player == "Player 1":
            self.value = 1
        else:
            self.value = 0

        # Font
        self._font = pygame.font.Font(None, 40)
        self._font_surf = self._font.render(f"{self.cur_player}", True, (255, 255, 255))

        # Winner / Reset
        self.winner = None


    def check_winner(self, matrix: list[list[None | int]]) -> str:

        # Check Winner horizontal
        for row in matrix:
            if all(map(lambda x: x == 1, row)):
                return 1
            if all(map(lambda x: x == 0, row)):
                return 0

        # Check Winner Vertical
        if all(map(lambda x: x == 1, [matrix[0][0], matrix[1][0], matrix[2][0]])) or \
           all(map(lambda x: x == 1, [matrix[0][1], matrix[1][1], matrix[2][1]])) or \
           all(map(lambda x: x == 1, [matrix[0][2], matrix[1][2], matrix[2][2]])):
            return 1
        
        if all(map(lambda x: x == 0, [matrix[0][0], matrix[1][0], matrix[2][0]])) or \
           all(map(lambda x: x == 0, [matrix[0][1], matrix[1][1], matrix[2][1]])) or \
           all(map(lambda x: x == 0, [matrix[0][2], matrix[1][2], matrix[2][2]])):
            return 0

        # Check Winner diagonal
        if all(map(lambda x: x == 1, [matrix[0][0], matrix[1][1], matrix[2][2]])) or all(map(lambda x: x == 1, [matrix[0][2], matrix[1][1], matrix[2][0]])):
            return 1
        if all(map(lambda x: x == 0, [matrix[0][0], matrix[1][1], matrix[2][2]])) or all(map(lambda x: x == 0, [matrix[0][2], matrix[1][1], matrix[2][0]])):
            return 0
        
        # Check for Tie
        if len([value for row in matrix for value in row if value == None]) == 0:
            return 2

        return None


    def set_value(self) -> None:
        if self.number in self.open_fields:
            match self.number:
                case 1: self.matrix[0][0] = self.value
                case 2: self.matrix[0][1] = self.value
                case 3: self.matrix[0][2] = self.value
                case 4: self.matrix[1][0] = self.value
                case 5: self.matrix[1][1] = self.value
                case 6: self.matrix[1][2] = self.value
                case 7: self.matrix[2][0] = self.value
                case 8: self.matrix[2][1] = self.value
                case 9: self.matrix[2][2] = self.value
            
            if self.value == 1:
                self.lst_cross.append(self.pos_xy_rect)
            else:
                self.lst_zeros.append(self.pos_xy_rect)

            self.open_fields.remove(self.number)
            winner = self.check_winner(self.matrix)

            if winner == None:
                if self.cur_player == "Player 1":
                    self.cur_player = "Player 2"
                    self.value = 0
                    self._font_surf = self._font.render(f"{self.cur_player} : O", True, (255, 255, 255))
                else:
                    self.cur_player = "Player 1"
                    self.value = 1
                    self._font_surf = self._font.render(f"{self.cur_player} : X", True, (255, 255, 255))
            else:
                self.winner = winner
                winner_str = None
                if self.winner == 1:
                    winner_str = "Player 1 Wins!!"
                elif self.winner == 0:
                    winner_str = "Player 2 Wins!!"
                else:
                    winner_str = "Tie"
                self._font_surf = self._font.render(winner_str, True, (255, 255, 255))


    def draw(self, pos) -> None:
        for _, play_board_rect in self.play_board.items():
            pygame.draw.rect(self.surf, (255, 255, 255), play_board_rect, border_radius=4)
            if play_board_rect.collidepoint(pos):
                pygame.draw.rect(self.surf, (240, 25, 0), play_board_rect, width=3, border_radius=4)
                

    def select(self, pos) -> None:
        for num, play_board_rect in self.play_board.items():
            if play_board_rect.collidepoint(pos):
                
                self.number = num
                self.pos_xy_rect = play_board_rect.topleft


    def draw_cross(self) -> None:
        for pos_cross in self.lst_cross:
            self.surf.blit(self.cross_surf, pos_cross)


    def draw_zero(self) -> None:
        for pos_zero in self.lst_zeros:
            self.surf.blit(self.zero_surf, pos_zero)


    def draw_cur_player(self) -> None:
        self.surf.blit(self._font_surf, (10, 635))


    def game_over(self) -> bool:
        if self.winner == 1 or self.winner == 0 or self.winner == 2:
            return True
        
        return False
    

    def reset(self) -> None:
        self.pos_xy_rect = None
        self.lst_cross = []
        self.lst_zeros = []
        self.matrix = [[None, None, None],
                       [None, None, None],
                       [None, None, None]]
        
        self.first_player = random.choice(["Player 1", "Player 2"])
        self.cur_player = self.first_player
        self.value = None 

        self.open_fields = set(range(1, 10))
        self.number = None # Current Number

        if self.cur_player == "Player 1":
            self.value = 1
        else:
            self.value = 0

        self.winner = None

        self._font_surf = self._font.render(f"{self.cur_player}", True, (255, 255, 255))