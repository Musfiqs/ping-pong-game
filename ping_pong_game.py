import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PADDLE_WIDTH = 15
PADDLE_HEIGHT = 90
BALL_SIZE = 15
PADDLE_SPEED = 5
BALL_SPEED = 7

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)

class Paddle:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, PADDLE_WIDTH, PADDLE_HEIGHT)
        self.speed = PADDLE_SPEED
    
    def move_up(self):
        if self.rect.top > 0:
            self.rect.y -= self.speed
    
    def move_down(self):
        if self.rect.bottom < SCREEN_HEIGHT:
            self.rect.y += self.speed
    
    def draw(self, screen):
        pygame.draw.rect(screen, WHITE, self.rect)

class Ball:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, BALL_SIZE, BALL_SIZE)
        self.speed_x = BALL_SPEED * random.choice([-1, 1])
        self.speed_y = BALL_SPEED * random.choice([-1, 1])
    
    def move(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
    
    def bounce_y(self):
        self.speed_y = -self.speed_y
    
    def bounce_x(self):
        self.speed_x = -self.speed_x
    
    def reset_position(self):
        self.rect.x = SCREEN_WIDTH // 2
        self.rect.y = SCREEN_HEIGHT // 2
        self.speed_x = BALL_SPEED * random.choice([-1, 1])
        self.speed_y = BALL_SPEED * random.choice([-1, 1])
    
    def draw(self, screen):
        pygame.draw.rect(screen, WHITE, self.rect)

class PingPongGame:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Ping Pong Game")
        self.clock = pygame.time.Clock()
        
        # Create paddles
        self.left_paddle = Paddle(30, SCREEN_HEIGHT // 2 - PADDLE_HEIGHT // 2)
        self.right_paddle = Paddle(SCREEN_WIDTH - 30 - PADDLE_WIDTH, SCREEN_HEIGHT // 2 - PADDLE_HEIGHT // 2)
        
        # Create ball
        self.ball = Ball(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        
        # Scores
        self.left_score = 0
        self.right_score = 0
        self.font = pygame.font.Font(None, 74)
        
        # Game state
        self.running = True
    
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
        
        # Handle continuous key presses
        keys = pygame.key.get_pressed()
        
        # Left paddle controls (W/S)
        if keys[pygame.K_w]:
            self.left_paddle.move_up()
        if keys[pygame.K_s]:
            self.left_paddle.move_down()
        
        # Right paddle controls (UP/DOWN arrows)
        if keys[pygame.K_UP]:
            self.right_paddle.move_up()
        if keys[pygame.K_DOWN]:
            self.right_paddle.move_down()
    
    def update_game(self):
        # Move ball
        self.ball.move()
        
        # Ball collision with top and bottom walls
        if self.ball.rect.top <= 0 or self.ball.rect.bottom >= SCREEN_HEIGHT:
            self.ball.bounce_y()
        
        # Ball collision with paddles
        if self.ball.rect.colliderect(self.left_paddle.rect) or self.ball.rect.colliderect(self.right_paddle.rect):
            self.ball.bounce_x()
        
        # Ball goes off screen (scoring)
        if self.ball.rect.left <= 0:
            self.right_score += 1
            self.ball.reset_position()
        elif self.ball.rect.right >= SCREEN_WIDTH:
            self.left_score += 1
            self.ball.reset_position()
    
    def draw_everything(self):
        # Clear screen
        self.screen.fill(BLACK)
        
        # Draw center line
        pygame.draw.aaline(self.screen, GRAY, (SCREEN_WIDTH // 2, 0), (SCREEN_WIDTH // 2, SCREEN_HEIGHT))
        
        # Draw paddles and ball
        self.left_paddle.draw(self.screen)
        self.right_paddle.draw(self.screen)
        self.ball.draw(self.screen)
        
        # Draw scores
        left_text = self.font.render(str(self.left_score), True, WHITE)
        right_text = self.font.render(str(self.right_score), True, WHITE)
        
        self.screen.blit(left_text, (SCREEN_WIDTH // 4, 50))
        self.screen.blit(right_text, (3 * SCREEN_WIDTH // 4, 50))
        
        # Draw controls text
        control_font = pygame.font.Font(None, 36)
        controls_text = control_font.render("Left: W/S | Right: UP/DOWN", True, GRAY)
        self.screen.blit(controls_text, (SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT - 50))
        
        # Update display
        pygame.display.flip()
    
    def run(self):
        while self.running:
            self.handle_events()
            self.update_game()
            self.draw_everything()
            self.clock.tick(60)  # 60 FPS
        
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    game = PingPongGame()
    game.run() 