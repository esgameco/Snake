import sys, pygame, time
from pygame import image
from pygame.draw import rect
pygame.init()

size = width, height = 501, 500
screen = pygame.display.set_mode(size)

square_dim = 20

color = 255, 255, 255

w, h = int(input("Insert Width: ")), int(input("Insert Height: "))
# board = [[0 for x in range(w)] for y in range(h)] 
board_offset = 12, 12 

# this makes out lives easier
class GameObject:
    """ 
        GameObject

            file_path: str - the image path
            size: list - size of the image
    """
    def __init__(self, file_path, size):
        self.image = self.make_image(file_path, size)
        self.rect = self.image.get_rect()
        self.size = size

    def make_image(self, file_path, size):
        return pygame.transform.scale(
            pygame.image.load(file_path), size)
    
    def display(self, screen, position):
        # making the snake ass 
        screen.blit(self.image,
            dest=(position[0]*self.size[0], position[1]*self.size[1]),
            area=self.rect)

class Snake: 
    """ 
        GameObject

            image: GameObject - the snake image class
    """
    def __init__(self, image, direction=[1, 0]):
        self.parts = []
        self.image = image
        self.direction = direction

    def display(self, screen):
        for i in range(len(self.parts)):
            self.image.display(screen, self.parts[i])
    
    def add_part(self, position, remove_first=True):
        if remove_first: 
            if len(self.parts):
                del self.parts[0]
        self.parts.append(position)

    def change_direction(self, direction):
        if not (self.direction[0] == -direction[0] 
            and self.direction[1] == -direction[1]):
            self.direction = direction
    
    def next_frame(self):
        position = (self.parts[-1][0] + self.direction[0],
             self.parts[-1][1] + self.direction[1])
        self.add_part(position)

snake = GameObject("src/assets/snakebody.png", (square_dim, square_dim))
apple = GameObject("src/assets/appleshit.png", (square_dim, square_dim))

apple_position = [1, 6]

snakeshit = Snake(snake)
snakeshit.add_part((1, 1))

while 1:
    # checking the system for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.KEYDOWN: 
            
    
    # making the screen black
    screen.fill((0,0,0))
    
    # making the lines for the rows
    for i in range(h+1):
        pygame.draw.line(screen, color, (0, i*square_dim), (square_dim*(h), i*square_dim), 1)  
    # making the lines for the columns
    for i in range(w+1):
        pygame.draw.line(screen, color, (i*square_dim, 0), (i*square_dim, square_dim*(w)), 1)  

    snakeshit.next_frame()

    snakeshit.display(screen)
    apple.display(screen, apple_position)
    
    # displying to the screen
    pygame.display.flip()

    time.sleep(50/60)