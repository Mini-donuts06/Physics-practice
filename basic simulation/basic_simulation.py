import pygame,sys, pymunk # importing modules

def create_cookie(space):
    body = pymunk.Body(1, 100, body_type = pymunk.Body.DYNAMIC) #(mass, intertia, body_type)
    body.position = (200, 0)
    shape = pymunk.Circle(body, 40)
    space.add(body,shape)
    return shape

def draw_cookies(cookies):
    for cookie in cookies:
        pos_x = int(cookie.body.position.x)
        pos_y = int(cookie.body.position.y)
        pygame.draw.circle(screen,(0,0,0),(pos_x, pos_y),40)

def static_ball(space):
    body = pymunk.Body(body_type = pymunk.Body.STATIC)
    body.position = (200,200)
    shape = pymunk.Circle(body,30)
    space.add(body,shape)
    return shape

def draw_static_ball(balls):
    for ball in balls:
        pos_x = int(ball.body.position.x)
        pos_y = int(ball.body.position.y)
        pygame.draw.circle(screen,(0,0,0),(pos_x, pos_y),30)


pygame.init() # initiating pygame 
screen = pygame.display.set_mode((400,400)) # creating screen display
clock = pygame.time.Clock()  # creating the game clock
space = pymunk.Space()
space.gravity = (0,500)
cookies = []
cookies.append(create_cookie(space))

balls = []
balls.append(static_ball(space))

while True:     # Game loop
    for event in pygame.event.get():  # checking for user input
        if event.type == pygame.QUIT: # input to close the game
            pygame.quit()
            sys.exit()

    screen.fill((217,217,217))     # background color
    draw_cookies(cookies)
    draw_static_ball(balls)
    space.step(1/50)
    pygame.display.update()        # rendering the frame
    clock.tick(120)                # limiting the frames per second to 120
