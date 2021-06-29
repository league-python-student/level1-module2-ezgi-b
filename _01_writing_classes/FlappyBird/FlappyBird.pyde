"""
Create the classic Flappy Bird game!
"""

# 0. Do the other exercises in this folder before starting this one!

def setup():
    pass
    # 1. Use the size function to set the width and height of the program
    size(500, 500)
    # 2. Remove the comment (the '#') in the line below 
    global bg, bird, lower_pipe, upper_pipe, score, passed
    
    # 3. Use the loadImage function to inialize the bg variable with the
    # flappyBackground.jpg image 
    bg = loadImage("flappyBackground.jpg")
    # 4. Resize the background to the width and height of the program
    bg.resize(500, 500)
    # 5. Use the Bird class defined below to create a Bird object.
    # The bird image is named 'bird.png'
    bird = Bird("bird.png", 250, 250)
    # 6. Use the Pipe class defined below to create 2 Pipe objects,
    # one pipe at the top and one at the bottom.
    # The pipe images are named, "topPipe.png" and "bottomPipe.png"  
    lower_pipe = Pipe(image_file = "bottomPipe.png", pipe_height = 100)
    upper_pipe = Pipe(image_file = "topPipe.png", pipe_y = 400, pipe_height = 100)
    # 7. Call the reset_pipes function to set the initial positions
    # of the pipes
    reset_pipes(lower_pipe, upper_pipe)
    score = 0
    passed = False

def draw():
    pass
    # 8. Remove the comment (the '#') in the line below
    global bg, bird, lower_pipe, upper_pipe, score, passed
    
    # 9. Use the background function to draw the game's background
    background(bg)
    # 10. Find the Bird class below and follow the instructions
    # there to complete the Bird class before continuing
    
    # 18. Call the bird's update and draw methods.
    # Is the bird displayed and move up when the mouse is clicked?
    bird.update()
    bird.draw()
    # 19. Call the upper and lower pipe's update methods.
    upper_pipe.update()
    lower_pipe.update()
    upper_pipe.draw()
    lower_pipe.draw()
    # 20. Call the upper and lower pipe's draw methods. 
    # Do the pipes move across the screen?
    textSize(30)
    text("Score: " + str(score), 100, 80)
    # 21. Call the reset_pipes function defined below when the pipes
    # move past the screen to reset their position. 
    if upper_pipe.x < random(-100, -20):
        reset_pipes(lower_pipe, upper_pipe)
        passed = False
    # 22. Call the intersects_pipes function defined below to check if
    # the bird collided with one of the pipes. If there's a collision,
    # stop the game by calling noLoop()  
    if intersects_pipes(bird, lower_pipe, upper_pipe) or bird.y < 0 or bird.y > height - bird.height:
        noLoop()
    # 23. End the game if the bird flies too low (hitting the ground)
    # OR flies too high (above the screen)
    if bird.x > lower_pipe.x + lower_pipe.width and not passed:
        score += 1
        passed = True
    

class Bird:
    def __init__(self, image_file, bird_x, bird_y):
        self.x = bird_x
        self.y = bird_y
        self.width = 50
        self.height = ( 3 * self.width ) / 4
        self.image = loadImage(image_file)
        self.image.resize(self.width, self.height)
        self.time = 10
        
        # 11. Initialize a member variable for gravity (typically 1 to 5)
        self.gravity = 3
        # 12. Add a member variable for the distance the bird travels
        # upward when it flaps (jumps)
        self.jump_height = 60
    # 13. Create an update method that will update the bird's position
    # while the game runs
    def update(self):
        self.y += self.gravity
        if mousePressed and self.time >= 10:
            self.y -= self.jump_height
            self.time = 0
        else:
            self.time += 1
        # 14. Move the bird downward by the gravity member variable to make
        # it look like the bird is falling
        
        # 15. Use the boolean mousePressed variable to flap (jump) the bird
        # up by flap distance member variable the when the mouse is pressed
    
    # 16. Create a draw method that shows the bird on the program
    def draw(self):
        image(self.image, self.x, self.y)
        # 17. Use the image function and the class's member variables to
        # draw the bird
        # image( <image>, <x positon>, <y position> )
        

class Pipe:
    pipe_gap = 200
    
    def __init__(self, image_file, pipe_y=0, pipe_height=0):
        self.x = width
        self.y = pipe_y
        self.width = 50
        self.height = pipe_height
        self.image = loadImage(image_file)
        self.image.resize(self.width, self.height)
    
    def update(self):
        self.x -= 3
    
    def draw(self):
        image(self.image, self.x, self.y)

    def teleport(self, pipe_y, pipe_height):
        self.x = width
        self.y = pipe_y
        self.height = pipe_height
        self.image.resize(self.width, self.height)
        

def reset_pipes(lower_pipe, upper_pipe):
    random_height = int((2 * random(height) / 3) + 50)
    upper_pipe.teleport(0, random_height)
    lower_pipe.teleport(random_height + Pipe.pipe_gap, height - random_height)
    
    
def intersects_pipes(bird, lower_pipe, upper_pipe):
    # Check upper pipe collision
    if (bird.x + bird.width >= upper_pipe.x and
        bird.x <= upper_pipe.x + upper_pipe.width and
        bird.y + bird.height >= upper_pipe.y and
        bird.y <= upper_pipe.y + upper_pipe.height):
        return True

    # Check lower pipe collision
    if (bird.x + bird.width >= lower_pipe.x and
        bird.x <= lower_pipe.x + lower_pipe.width and
        bird.y + bird.height >= lower_pipe.y and
        bird.y <= lower_pipe.y + lower_pipe.height):
        return True

    return False
