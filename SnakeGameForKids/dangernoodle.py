# first stub to check how pygame and its event loop works

def main():
    import pygame
    pygame.init()
    dis = pygame.display.set_mode((640, 480))
    pygame.display.update()
    pygame.display.set_caption('danger noodle')
    game_over = False
    while not game_over:
        for event in pygame.event.get():
            print("event:", event)  # prints all actions

            if event.type == pygame.QUIT:
                print("closed via X")
                game_over = True

    pygame.quit()
    quit()

#--------------------------

main()