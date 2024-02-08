import simplegui
import random

# Game dimensions
CANVAS_WIDTH = 800
CANVAS_HEIGHT = 600

# Player spaceship properties
SPACESHIP_CENTER = (CANVAS_WIDTH // 2, CANVAS_HEIGHT - 30)
SPACESHIP_RADIUS = 30
SPACESHIP_VELOCITY = 3
SPACESHIP_ANGLE = 0
SPACESHIP_IMAGE = None

# Projectiles (bullets) properties
PROJECTILE_RADIUS = 5
PROJECTILE_VELOCITY = 10
PROJECTILE_LIFETIME = 60

# Enemies (asteroids) properties
ENEMY_RADIUS = 20
ENEMY_VELOCITY = 2
ENEMY_SPAWN_RATE = 30

# Game state variables
score = 0
lives = 3
game_over = False

def load_assets():
    global SPACESHIP_IMAGE

    # Replace with your desired image path
    SPACESHIP_IMAGE = simplegui.load_image("spaceship.png")

def draw(canvas):
    global score, lives, game_over, SPACESHIP_CENTER, SPACESHIP_ANGLE

    # Clear the canvas
    canvas.draw_rectangle((0, 0), (CANVAS_WIDTH, CANVAS_HEIGHT), "black")

    # Draw score and lives
    canvas.draw_text("Score: " + str(score), (10, 20), 20, "white")
    canvas.draw_text("Lives: " + str(lives), (CANVAS_WIDTH - 60, 20), 20, "white")

    # Draw the spaceship
    canvas.draw_image(SPACESHIP_IMAGE, SPACESHIP_CENTER, SPACESHIP_ANGLE,
                      2 * SPACESHIP_RADIUS, 2 * SPACESHIP_RADIUS)

def input_handler(event):
    global SPACESHIP_ANGLE

    if event.key == simplegui.KEY_LEFT:
        SPACESHIP_ANGLE -= 0.1
    elif event.key == simplegui.KEY_RIGHT:
        SPACESHIP_ANGLE += 0.1
    elif event.key == simplegui.KEY_SPACE:
        # Fire a projectile
        # ... (Add logic to create and track projectiles here)

    def tick():
        global SPACESHIP_CENTER, SPACESHIP_VELOCITY, ENEMY_SPAWN_RATE

# Initialize game
load_assets()

# Register event handlers
frame = simplegui.create_frame("Space Shooter", CANVAS_WIDTH, CANVAS_HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(input_handler)
frame.set_timer_handler(tick, 100)  # Update every 100 milliseconds

# Start the game
frame.start()
