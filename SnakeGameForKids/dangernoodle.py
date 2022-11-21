# first stub to check how pygame and its event loop works

def main():
    import pygame

    pygame.init()
    boardWidth = 640
    boardHeight = 480
    dis = pygame.display.set_mode((boardWidth, boardHeight))
    pygame.display.update()
    pygame.display.set_caption('danger noodle')

    blue = (0, 0, 255)
    white = (255, 255, 255)

    xPos = boardWidth / 2
    yPos = boardHeight / 2

    xDiff = 0
    yDiff = 0

    clock = pygame.time.Clock()

    game_over = False
    while not game_over:
        for event in pygame.event.get():
            print("event:", event)  # prints all actions

            if event.type == pygame.QUIT:
                print("closed via X")
                game_over = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    xDiff = -10
                    yDiff = 0
                elif event.key == pygame.K_RIGHT:
                    xDiff = 10
                    yDiff = 0
                elif event.key == pygame.K_UP:
                    xDiff = 0
                    yDiff = -10
                elif event.key == pygame.K_DOWN:
                    xDiff = 0
                    yDiff = 10

            xPos += xDiff
            yPos += yDiff
            dis.fill(white)
            pygame.draw.rect(dis, blue, [xPos, yPos, 10, 10])
            pygame.display.update()

            clock.tick(25)

    pygame.quit()
    quit()

#--------------------------

main()
