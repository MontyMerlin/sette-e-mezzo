import random, pygame, sys 
from pygame.locals import *
from classes import *

pygame.init()
pygame.display.set_caption("Sette e Mezzo")

# Colour variables (UPPERCASE)
#            R    G    B
GRAY     = (100, 100, 100)
NAVYBLUE = ( 60,  60, 100)
WHITE    = (255, 255, 255)
RED      = (255,   0,   0)
GREEN    = (  0, 255,   0)
BLUE     = (  0,   0, 255)
YELLOW   = (255, 255,   0)
ORANGE   = (255, 128,   0)
PURPLE   = (255,   0, 255)
CYAN     = (  0, 255, 255)
BLACK    = (  0,   0,   0)

# constants (CamelCase)
WindowWidth      =  800
WindowHeight     =  500
GameSpeed        =  20
FPS              =  pygame.time.Clock()
DisplaySurf      =  pygame.display.set_mode((WindowWidth,WindowHeight))
StdFont          =  pygame.font.Font("fonts/Archivo-SemiBold.ttf",20)  
Values           =  [i.split(",") for i in open("values.txt").read().split("\n")]
Cards            =  {i[0] : Card(i[0],i[1],i[2],i[3]) for i in Values}
CardNameLoc      =  (5,5)
DeckInfoLoc      =  (300,300)
ScoreLoc         =  (100,300)
deck             =  pygame.image.load("images/deck.jpg")
icon             =  pygame.image.load("images/icon.png")

pygame.display.set_icon(icon)

# throwaways (lowercase)
deal = True
hand = []

# Game loop
while True:

        # available cards 
        available = [code for code in Cards if not Cards[code].drawn == True]
    
        # User input
        for event in pygame.event.get():
                if event.type == QUIT:
                        pygame.quit()
                        sys.exit()
                if event.type == KEYDOWN:
                        if event.key == K_SPACE:
                                deal = True
                        
        # white background               
        DisplaySurf.fill(WHITE)
        
        # deal a new card
        if deal == True and available:
                newcard = random.choice(available)
                hand.append(newcard)
                Cards[newcard].drawn = True
                deal = False
        
        # keep score
        score = sum([float(Cards[code].value) for code in hand])

        # --print the cards info to the display surface--

        # latest card name and value
        DisplaySurf.blit(StdFont.render(Cards[newcard].name + "  " + Cards[newcard].value,True,BLACK),pygame.Rect(CardNameLoc,(1,1)))

        # score
        if score <= 7.5:
                scorecolor = GREEN
        else:
                scorecolor = RED

        DisplaySurf.blit(StdFont.render("Score = " + str(score),True, scorecolor),pygame.Rect(ScoreLoc,(1,1)))

        # cards and codes
        for count, code in enumerate(hand):
                DisplaySurf.blit(Cards[code].img,pygame.Rect((60*count),50,60,110))
                DisplaySurf.blit(StdFont.render(code,True,scorecolor,GRAY),pygame.Rect((18 + 60*count),160,1,1))

        
        # remaining deck
        DisplaySurf.blit(deck,pygame.Rect(DeckInfoLoc,(1,1)))
        DisplaySurf.blit(StdFont.render("Remaining deck = " + str(len(available)),True,BLACK),pygame.Rect(DeckInfoLoc,(1,1)))

        
        
        # game speed
        FPS.tick(GameSpeed)

        # update screen
        pygame.display.update()
