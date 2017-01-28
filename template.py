import pygame


def main():
    pygame.init()
    # set screen width/height and caption
    size = [1366, 720]
    screen = pygame.display.set_mode(size) # (size,pygame.FULLSCREEN)
    pygame.display.set_caption('My Game')
    # initialize clock. used later in the loop.
    clock = pygame.time.Clock()
    done = False
    while done == False:
        # mover a controls
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    done = True
        # game mechanics
        # drawing routines

if __name__ == "__main__":
    main()        
