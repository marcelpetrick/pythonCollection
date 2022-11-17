# first stub to check how pygame and its event loop works

def main():
    import pygame

    pygame.init()
    dis = pygame.display.set_mode((640, 480))
    pygame.display.update()
    pygame.display.set_caption('danger noodle')

    blue = (0, 0, 255)
    red = (255, 0, 0)

    game_over = False
    while not game_over:
        for event in pygame.event.get():
            print("event:", event)  # prints all actions

            if event.type == pygame.QUIT:
                print("closed via X")
                game_over = True

            pygame.draw.rect(dis, blue, [200, 150, 10, 10])
            pygame.display.update()

    pygame.quit()
    quit()

#--------------------------

main()