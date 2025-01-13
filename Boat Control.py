from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from math import *
from sys import *
from playsound import playsound

# Define window size and initial position of objects
win = 500
x = y = 0
r = 50 # Radius for circular shapes

# Angle for rotation
a = 35

# Function to draw the rotating "rode" (pole or arm)
def rode(x, y, r, w, h):
    # Draw circular base of the rod
    glBegin(GL_TRIANGLE_FAN)
    for i in range(0, 360):
        theta = radians(i)  # Convert degree to radians
        xc = x + r * cos(theta)
        yc = y + r * sin(theta)
        glVertex2f(xc, yc - 100)  # Offset circle vertically
    glEnd()

    # Draw rectangular rod
    glBegin(GL_QUADS)
    glVertex2f(x + w, y + h)
    glVertex2f(x + w, y - h)
    glVertex2f(x - w, y - h)
    glVertex2f(x - w, y + h)
    glEnd()

# Function to draw the boat frame
def frame(x, y):
    glBegin(GL_QUADS)
    glVertex2f(x + 300, y + 80)  # Top-right corner
    glVertex2f(x + 200, y - 80)  # Bottom-right corner
    glVertex2f(x - 200, y - 80)  # Bottom-left corner
    glVertex2f(x - 300, y + 80)  # Top-left corner
    glEnd()

# Function to draw the water background
def water():
    glBegin(GL_QUADS)
    glVertex2f(500, 0)     # Top-right
    glVertex2f(500, -500)  # Bottom-right
    glVertex2f(-500, -500) # Bottom-left
    glVertex2f(-500, 0)    # Top-left
    glEnd()

# Function to draw the "dude" (a person-like figure) on the boat
def dude(x, y, r, w, h):
    # Draw the circular head
    glBegin(GL_TRIANGLE_FAN)
    for i in range(0, 360):
        theta = radians(i)
        xc = x + r * cos(theta)
        yc = y + r * sin(theta)
        glVertex2f(xc, yc + 150)  # Offset head vertically
    glEnd()

    # Draw rectangular body
    glBegin(GL_QUADS)
    glVertex2f(x + w, y + h + 100)
    glVertex2f(x + w, y - h)
    glVertex2f(x - w, y - h)
    glVertex2f(x - w, y + h + 40)
    glEnd()

# Main function to draw the boat and its components
def boat():
    global x, y, a
    glClear(GL_COLOR_BUFFER_BIT)  # Clear the screen

    # Draw water
    glColor3f(0, 0.8, 1)
    water()

    # Draw the "dude" (black)
    glColor3f(0, 0, 0)
    dude(x, y, 40, 50, 50)

    # Draw the boat frame (green)
    glColor3f(0, 1, 0)
    frame(x, y)

    # Draw and animate the rotating rod (red)
    glPushMatrix()
    glTranslate(x, 0, 0)  # Translate to the boat's position
    glRotate(a, 0, 0, 1)  # Rotate around the Z-axis
    glTranslate(-x, 0, 0) # Translate back
    glColor3f(1, 0, 0)
    rode(x, y, r, 10, 150)
    glPopMatrix()

    glFlush()
    glutSwapBuffers()

# Handle arrow key inputs to move or stop the boat
def arrow(key, x, y):
    i = 0
    if key == GLUT_KEY_RIGHT:  # Move right
        i += 1
        animate(i)
    elif key == GLUT_KEY_LEFT:  # Move left
        i -= 1
        animate(i)
    elif key == GLUT_KEY_DOWN:  # Stop movement
        i = 0
        animate(i)

# Handle keyboard inputs for sound playback
def keyboard(ckey, x, y):
    ckey = ckey.decode()
    if ckey == 'h' or ckey == 'H':
        playsound('/home/abhimanue/Desktop/Abhimanue/bushorn.mp3')

# Animate the boat and rotating rod
def animate(i):
    global x, y, a, win
    glutPostRedisplay()  # Redraw the screen
    if i == 0:
        return

    # Update boat position with wrap-around effect
    if x == win + 100:
        x = -win
    elif x == -win - 100:
        x = win
    else:
        x += i

    # Update rod rotation angle
    if a == -45:
        a = 40
    elif a == 45:
        a = -40
    else:
        a -= i

# Main function to initialize and run the program
def main():
    glutInit(sys.argv)
    glutInitWindowSize(win, win)  # Set window size
    glutInitWindowPosition(0, 0) # Set window position
    glutInitDisplayMode(GLUT_RGBA)  # Use RGBA color mode
    glutCreateWindow("Boat Control")  # Create window

    glutDisplayFunc(boat)    # Set display callback
    glutIdleFunc(boat)       # Set idle callback
    glutSpecialFunc(arrow)   # Set special key callback
    glutKeyboardFunc(keyboard) # Set keyboard callback

    glClearColor(1, 1, 1, 1)  # Set background color to white
    gluOrtho2D(-win, win, -win, win)  # Set 2D orthographic projection

    glutMainLoop()  # Start the GLUT event loop

main()
