import pygame
pygame.init()

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Set font and font size
font = pygame.font.Font(None, 36)

# Create buttons
button1 = pygame.image.load("Assets/Dino/DinoStart.png")
button1_rect = button1.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/4))

button2 = pygame.image.load("Assets/Dino/DoreamonStart.png")
button2_rect = button2.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2))

button3 = pygame.image.load("Assets/Dino/MarioStart.png")
button3_rect = button3.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT*3/4))

# Main loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Check if button1 is clicked
            if button1_rect.collidepoint(event.pos):
                # Link to Python file 1
                import main
            # Check if button2 is clicked
            elif button2_rect.collidepoint(event.pos):
                # Link to Python file 2
                import doreamon
            # Check if button3 is clicked
            elif button3_rect.collidepoint(event.pos):
                # Link to Python file 3
                import mario

    # Draw buttons
    screen.fill(WHITE)
    screen.blit(button1, button1_rect)
    screen.blit(button2, button2_rect)
    screen.blit(button3, button3_rect)

    # Update screen
    pygame.display.flip()

pygame.quit()






