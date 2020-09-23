import pygame

pygame.font.init()
font = pygame.font.SysFont('comicsans', 75)

pygame.init()

SCREEN_TITLE = 'TicTacToe'
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

WHITE_COLOR = (255, 255, 255)
BLACK_COLOR = (0, 0, 0)

clock = pygame.time.Clock()

possibilities = ["y" for n in range (9)]

def winCondition(type):
    if (possibilities[0] == type and possibilities[1] == type) and possibilities[2] == type:
        return True
    elif (possibilities[3] == type and possibilities[4] == type) and possibilities[5] == type:
        return True
    elif (possibilities[6] == type and possibilities[7] == type) and possibilities[8] == type:
        return True
    elif (possibilities[0] == type and possibilities[3] == type) and possibilities[6] == type:
        return True
    elif (possibilities[1] == type and possibilities[4] == type) and possibilities[7] == type:
        return True
    elif (possibilities[2] == type and possibilities[5] == type) and possibilities[8] == type:
        return True
    elif (possibilities[0] == type and possibilities[4] == type) and possibilities[8] == type:
        return True
    elif (possibilities[2] == type and possibilities[4] == type) and possibilities[6] == type:
        return True
    else:
        return False

def typeConverter(type):
    if type % 2 == 1:
        return "X"
    else:
        return "O"
def checkPosition(x,type):

    type = typeConverter(type)
    checker = False


    if x == 0:
        if possibilities[0] == "y":
            checker = True
            possibilities[0] = type

    elif x == 1:
        if possibilities[1] == "y":
            checker = True
            possibilities[1] = type
    elif x == 2:
        if possibilities[2] == "y":
            checker = True
            possibilities[2] = type
    elif x == 3:
        if possibilities[3] == "y":
            checker = True
            possibilities[3] = type
    elif x == 4:
        if possibilities[4] == "y":
            checker = True
            possibilities[4] = type
    elif x == 5:
        if possibilities[5] == "y":
            checker = True
            possibilities[5] = type
    elif x == 6:
        if possibilities[6] == "y":
            checker = True
            possibilities[6] = type
    elif x == 7:
        if possibilities[7] == "y":
            checker = True
            possibilities[7] = type
    elif x == 8:
        if possibilities[8] == "y":
            checker = True
            possibilities[8] = type
    return checker

def clickDetection(possition):
    if possition[0] >= 100 and possition[0] < 300:
        if possition[1] >= 100 and possition[1] < 300:
            return 0
        elif possition[1] > 300 and possition[1] < 500:
            return 3
        elif possition[1] > 500 and possition[1] <= 700:
            return 6
    elif possition[0] > 300 and possition[0] < 500:
        if possition[1] >= 100 and possition[1] < 300:
            return 1
        elif possition[1] > 300 and possition[1] < 500:
            return 4
        elif possition[1] > 500 and possition[1] <= 700:
            return 7
    elif possition[0] > 500 and possition[0] <= 700:
        if possition[1] >= 100 and possition[1] < 300:
            return 2
        elif possition[1] > 300 and possition[1] < 500:
            return 5
        elif possition[1] > 500 and possition[1] <= 700:
            return 8

def detectionToY(detect):
    if detect == 0:
        return 110
    elif detect == 1:
        return 110
    elif detect == 2:
        return 110
    elif detect == 3:
        return 310
    elif detect == 4:
        return 310
    elif detect == 5:
        return 310
    elif detect == 6:
        return 510
    elif detect == 7:
        return 510
    elif detect == 8:
        return 510

def detectionToX(detect):
    if detect == 0:
        return 110
    elif detect == 3:
        return 110
    elif detect == 6:
        return 110
    elif detect == 1:
        return 310
    elif detect == 4:
        return 310
    elif detect == 7:
        return 310
    elif detect == 2:
        return 510
    elif detect == 5:
        return 510
    elif detect == 8:
        return 510
class Game:
    TICK_RATE = 60

    def __init__(self, image_path, title, width, height):
        self.title = title
        self.width = width
        self.height = height

        self.game_screen = pygame.display.set_mode((width, height))

        self.game_screen.fill(WHITE_COLOR)
        pygame.display.set_caption(title)

        background_image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(background_image, (width, height))

    def run_game_loop(self):
        isGameOver = False
        didWin = False
        turn = 1

        self.game_screen.fill(WHITE_COLOR)
        self.game_screen.blit(self.image, (0, 0))

        while not isGameOver:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    isGameOver = True
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        getPossition = pygame.mouse.get_pos()
                        pos = clickDetection(getPossition)
                        isPossible = checkPosition(pos,turn)
                        if isPossible == True:
                            if turn % 2 == 1:
                                field10_o = GameObject('o.png',detectionToX(pos),detectionToY(pos),180,180)
                                field10_o.draw(self.game_screen)
                                pygame.display.update()
                                isGameOver = winCondition(typeConverter(turn))
                                turn += 1
                            else:
                                field10_x = GameObject('x.png',detectionToX(pos),detectionToY(pos), 180, 180)
                                field10_x.draw(self.game_screen)
                                pygame.display.update()
                                isGameOver = winCondition(typeConverter(turn))
                                turn +=1





            pygame.display.update()
            clock.tick(self.TICK_RATE)


class GameObject:

    def __init__(self, image_path, x, y, width, height):
        object_image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(object_image, (width, height))

        self.x_pos = x
        self.y_pos = y

        self.width = width
        self.height = height

    def draw(self, background):
        background.blit(self.image, (self.x_pos, self.y_pos))

new_game = Game('board.png', SCREEN_TITLE, SCREEN_WIDTH, SCREEN_HEIGHT)
new_game.run_game_loop()
