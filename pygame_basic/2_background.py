import pygame

pygame.init()  # initialize (initialize must be done)

# setting screen size
screen_width = 480  # horizontal size of screen
screen_height = 640  # vertical size of screen
screen = pygame.display.set_mode((screen_width, screen_height))  # use tuple

# screen title
pygame.display.set_caption("Nado Gmae")

# upload background image to game screen
background = pygame.image.load("/Users/Hwiyoul/PycharmProjects/PYTHONWORKSPACE/pygame_basic/background.jpg")

# event loop
# evnet loop : monitor what users are done such as keyboard typing, mouse moving to avoid game quit
running = True  # is game running?
while running:
    for event in pygame.event.get():  # this phrase must be written to use pygame package : what kind of events are occured?
        if event.type == pygame.QUIT:  # user quit game : the event of game screen is closed?
            running = False  # game is finished

    # screen.fill((34, 154, 21)) # fill screen with color RGB values of tuple

    screen.blit(background, (0, 0))  # write background image

    pygame.display.update()  # update screen per every frame to show <- must be written

# finish pygame
pygame.quit()

# source : https://www.youtube.com/watch?v=Dkx8Pl6QKW0&t=0s