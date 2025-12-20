import turtle
import time

# Screen setup
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 1000

# Create screen
screen = turtle.Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor("blue")
screen.title("Millie's Square Game")

# Character class
class Character:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.velocity_x = 0
        self.velocity_y = 0
        
        # Create turtle for renderingx
        self.turtle = turtle.Turtle()
        self.turtle.shape("turtle")
        self.turtle.color(color)
        self.turtle.speed(0)
        self.turtle.shapesize(height/20, width/20)
        self.update_position()
    
    def handle_input(self):
        """Handle keyboard input"""
        self.velocity_x = 0
        self.velocity_y = 0
    
    def update(self, keys_pressed):
        """Update character position based on input"""
        # Reset velocity each frame
        self.velocity_x = 0
        self.velocity_y = 0
        
        if 'Left' in keys_pressed or 'a' in keys_pressed:
            self.turtle.left(5)
        if 'Right' in keys_pressed or 'd' in keys_pressed:
            self.turtle.right(5)
        if 'Up' in keys_pressed or 'w' in keys_pressed:
            self.turtle.forward(5)
        if 'Down' in keys_pressed or 's' in keys_pressed:
            self.turtle.forward(-5)
        
        # Update position
        self.x += self.velocity_x
        self.y += self.velocity_y
        
        # Keep character on screen
        self.x = max(-SCREEN_WIDTH//2 + self.width//2, min(self.x, SCREEN_WIDTH//2 - self.width//2))
        self.y = max(-SCREEN_HEIGHT//2 + self.height//2, min(self.y, SCREEN_HEIGHT//2 - self.height//2))
        
        self.update_position()
    
    def update_position(self):
        """Update turtle position"""
        #self.turtle.goto(self.x, self.y)
        pass

# Create character at center
character = Character(
    x=0,
    y=0,
    width=50,
    height=50,
    color="green"
)

# Key tracking
keys_pressed = set()

def on_key_press(key):
    keys_pressed.add(key)

def on_key_release(key):
    keys_pressed.discard(key)

# Bind keys using tkinter for proper press/release detection
canvas = screen.getcanvas()
canvas.focus_set()
canvas.bind('<KeyPress>', lambda e: on_key_press(e.keysym))
canvas.bind('<KeyRelease>', lambda e: on_key_release(e.keysym))

screen.listen()

# Main loop
running = True
try:
    while running:
        character.update(keys_pressed)
        screen.update()
        time.sleep(0.03)  # ~33 FPS
except KeyboardInterrupt:
    running = False

turtle.done()
