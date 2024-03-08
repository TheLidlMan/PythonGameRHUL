import PySimpleGUI
from collections import deque
import random

class Spritesheet:
    def __init__(self, rows, cols, frame_duration, num_frames):
        # Added num_frames as arg
        self.image = PySimpleGUI.load_image("https://i.ibb.co/gvrrbWW/Screenshot-2024-02-17-at-3-30-06-pm.png")
        if self.image.get_width() <= 0 or self.image.get_height() <= 0:
            raise ValueError("Image dimensions must be > 0")
        self.rows = rows
        self.cols = cols
        self.width = self.image.get_width() // self.cols
        self.height = self.image.get_height() // self.rows
        self.center_x = self.width // 2
        self.center_y = self.height // 2
        # Put num_frames in as variable
        self.queue = [(i % self.cols, i // self.cols) for i in range(num_frames)]
        self.frame_num = 0
        self.frame_duration = frame_duration
        self.clock = Clock(frame_duration)
        self.pos = (500, 500)  # Initial position of the sprite
        self.move_left = False
        self.move_right = False
        self.move_up = False
        self.move_down = False
    
    def done(self): # return boolean if last frame reached
        return False
    
    def draw(self, canvas):
        current_frame = self.queue[self.frame_num]
        orientation = 0  # Default orientation (upwards)
        
        if self.move_left:
            orientation = 1  # Left orientation
        elif self.move_right:
            orientation = 2  # Right orientation
        elif self.move_down:
            orientation = 3  # Down orientation
        
        canvas.draw_image(self.image,
                          (self.center_x + current_frame[0] * self.width + orientation * self.width,
                           self.center_y + current_frame[1] * self.height),
                          (self.width, self.height),
                          self.pos,
                          (self.width, self.height))
    
    def update(self):
        # checks if condition met to move to next frame based on frame duration
        if self.clock.tick() and not self.done():
            # increments in order to move to next frame
            self.frame_num = (self.frame_num + 1) % len(self.queue)
        
        # Update position based on movement flags
        if self.move_left:
            self.left(1)
        if self.move_right:
            self.right(1)
        if self.move_up:
            self.up(1)
        if self.move_down:
            self.down(1)
    
    def left(self, distance):
        x, y = self.pos
        self.pos = (x - distance, y)
    
    def right(self, distance):
        x, y = self.pos
        self.pos = (x + distance, y)
    
    def up(self, distance):
        x, y = self.pos
        self.pos = (x, y - distance)
    
    def down(self, distance):
        x, y = self.pos
        self.pos = (x, y + distance)

class Clock:
    def __init__(self, frame_duration):
        self.time = 0
        self.frame_duration = frame_duration
    
    def tick(self):
        self.time += 1
        return self.time % self.frame_duration == 0
    
    def transition(self, frame_duration):
        return self.time % frame_duration == 0

def draw_handler(canvas):
    canvas.draw_polygon([(0, 0), (1000, 0), (1000, 1000), (0, 1000)], 1, '#081830', '#081830')
    run.update()
    run.draw(canvas)

def keydown_handler(key):
    if key == PySimpleGUI.KEY_MAP['left']:
        run.move_left = True
    elif key == PySimpleGUI.KEY_MAP['right']:
        run.move_right = True
    elif key == PySimpleGUI.KEY_MAP['up']:
        run.move_up = True
    elif key == PySimpleGUI.KEY_MAP['down']:
        run.move_down = True

def keyup_handler(key):
    if key == PySimpleGUI.KEY_MAP['left']:
        run.move_left = False
    elif key == PySimpleGUI.KEY_MAP['right']:
        run.move_right = False
    elif key == PySimpleGUI.KEY_MAP['up']:
        run.move_up = False
    elif key == PySimpleGUI.KEY_MAP['down']:
        run.move_down = False

def draw_handler(canvas):
    # Draw background
    canvas.draw_polygon([(0, 0), (1000, 0), (1000, 1000), (0, 1000)], 1, '#081830', '#081830')
    
    # Draw stars
    for star in stars:
        star.draw(canvas)
    
    # Update and draw the sprite
    run.update()
    run.draw(canvas)

class Star:
    def __init__(self, pos, radius, color):
        self.pos = pos
        self.radius = radius
        self.color = color
        self.alpha = 0
        self.fade_in = True
    
    def update(self):
        if self.fade_in:
            self.alpha += 5
            if self.alpha >= 255:
                self.alpha = 255
                self.fade_in = False
        else:
            self.alpha -= 5
            if self.alpha <= 0:
                self.alpha = 0
                self.fade_in = True
    
    def draw(self, canvas):
        canvas.draw_circle(self.pos, self.radius, 1, self.color, f'rgba(255, 255, 255, {self.alpha / 255})')

# Create a list to store the stars
stars = []

# Generate random stars
for _ in range(100):
    x = random.randint(0, 1000)
    y = random.randint(0, 1000)
    radius = random.randint(1, 3)
    color = random.choice(['#FFFFFF', '#FFFFCC', '#FFFF99'])
    star = Star((x, y), radius, color)
    stars.append(star)


# the columns and rows of the img
run = Spritesheet(1, 6, 10, 6) # Adjust speed here and num of frames now
width = run.width
height = run.height
frame = PySimpleGUI.create_frame("Spritesheet", 1000, 1000)
frame.set_draw_handler(draw_handler)
frame.set_keydown_handler(keydown_handler)  # Add keydown handler
frame.set_keyup_handler(keyup_handler)  # Add keyup handler
frame.start()
