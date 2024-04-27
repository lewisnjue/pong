
import pygame 
pygame.init()


# constants 
WIDTH, HEIGHT = 600, 600 
WHITE = (255, 255,255)
BLACK = (0, 0, 0)
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('PONG')
FPS = 60 
VELOCITY = 10
SCORE_FONT = pygame.font.Font(None,20)

RIGHT_SCORE = 0 
LEFT_SCORE = 0 


class Ball:
    y_velocity = 0.
    x_velocity = 10
    def __init__(self,x,y,radius,color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
    def draw(self):
        pygame.draw.circle(WIN, self.color, (self.x, self.y), self.radius)
    def move(self):
        

        if self.y - self.radius <= 0:
            self.y_velocity *= -1
        if self.y + self.radius >= HEIGHT:
            self.y_velocity *= -1
        
        self.x += self.x_velocity
        self.y += self.y_velocity
        if (  # Collision with left paddle
                self.x - self.radius < left_paddle.x + left_paddle.width and
                self.y + self.radius < left_paddle.y  + left_paddle.height and
                self.y - self.radius > left_paddle.y and 
                self.x - self.radius > 0
                
        ):
          
            self.x_velocity *= -1
            H = left_paddle.y + left_paddle.height//2 
            y_pos= self.y 
            D = y_pos - H 
            max_height = left_paddle.height//2 
            
            self.y_velocity = (D // 20) * 10 

           

            

        if (  # Collision with right paddle
                self.x + self.radius > right_paddle.x and
                self.y + self.radius < right_paddle.y + right_paddle.height  and
                self.y - self.radius > right_paddle.y and 
                self.x +self.radius < WIDTH 
                
        ):
            
            self.x_velocity *= -1

            H = right_paddle.y + right_paddle.height//2 
            y_pos= self.y 
            D = y_pos - H 
            max_height = right_paddle.height//2 
            
            self.y_velocity = (D // 20) * 10 

    def Score(self):
        if self.x < 0:
            global RIGHT_SCORE
            RIGHT_SCORE +=1 
            self.x = WIDTH// 2 
            self.y = HEIGHT// 2
            self.x_velocity *= -1 
            self.y_velocity = 0

        if self.x > WIDTH:
            global LEFT_SCORE
            LEFT_SCORE +=1 
            self.x = WIDTH// 2
            self.y = HEIGHT// 2
            self.x_velocity *= -1 
            self.y_velocity = 0

        





class Paddle:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
    def draw_rect(self):
        pygame.draw.rect(WIN, self.color, (self.x, self.y, self.width, self.height))
    def move_up(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and left_paddle.y >  0:
            left_paddle.y -= VELOCITY
        if keys[pygame.K_UP] and right_paddle.y > 0:
            right_paddle.y -= VELOCITY
    def move_down(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_s] and left_paddle.y + self.height <  WIDTH:
            left_paddle.y += VELOCITY
        if keys[pygame.K_DOWN] and right_paddle.y + self.height < WIDTH:
            right_paddle.y += VELOCITY


   
left_paddle = Paddle(0,WIDTH//2 - 50,10,100,WHITE)
right_paddle = Paddle(WIDTH - 10,HEIGHT//2 - 50,10,100,WHITE)



ball=Ball(WIDTH//2,HEIGHT//2,7,WHITE)
def draw_border():
    i=0
    while i < 600:
        pygame.draw.rect(WIN,WHITE,(WIDTH//2 - 5,i,10,20))


        i += 30

def draw_score():
    LEFT_SCORE_TEXT=SCORE_FONT.render(f'SCORE:  {LEFT_SCORE}',0,WHITE)
    RIGHT_SCORE_TEXT=SCORE_FONT.render(f'SCORE: {RIGHT_SCORE}',0,WHITE)
    LEFT_SCORE_TEXT_RECT = LEFT_SCORE_TEXT.get_rect(center=(WIDTH//4,50))
    RIGHT_SCORE_TEXT_RECT=RIGHT_SCORE_TEXT.get_rect(center=(3 * WIDTH//4,50))
    WIN.blit(LEFT_SCORE_TEXT,LEFT_SCORE_TEXT_RECT)
    WIN.blit(RIGHT_SCORE_TEXT,RIGHT_SCORE_TEXT_RECT)


def draw():
    WIN.fill(BLACK)
    ball.draw()
    ball.move()
    ball.Score()
    draw_border()
    draw_score()
    left_paddle.draw_rect()
    right_paddle.draw_rect()
    left_paddle.move_up()
    right_paddle.move_up()
    left_paddle.move_down()
    right_paddle.move_down()

    
    pygame.display.update()
def main():
    run = True 
    clock = pygame.time.Clock()
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False 
                break 
        draw()
        
    pygame.quit()

        


if __name__ == "__main__":
    main()
