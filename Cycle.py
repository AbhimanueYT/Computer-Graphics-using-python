from OpenGL.GL import *   # Import OpenGL functions for drawing.
from OpenGL.GLU import *  # Import OpenGL utility functions.
from OpenGL.GLUT import * # Import GLUT for windowing and event handling.
from sys import *         # Import system library.
from math import *        # Import math library for trigonometric functions.

# Global variables
win = 500  # Window size.
x = y = 0  # Initial coordinates of the center of the wheel.
r = 50     # Radius of the wheels.
t = 0      # Angle for rotation animation.

# Function to draw a circular wheel using points.
def wheel(x, y, r):
    glPointSize(2)           # Set the size of the points.
    glBegin(GL_POINTS)       # Begin drawing points.
    for i in range(0, 360):  # Loop through 360 degrees.
        # Use parametric equations for a circle to calculate points.
        glVertex2f(x + r * cos(pi * i / 180), y + r * sin(pi * i / 180))
    glEnd()

# Function to draw a line representing the rotating spokes of the wheel.
def line(x, r):
    glLineWidth(2)           # Set the width of the line.
    glBegin(GL_LINES)        # Begin drawing lines.
    # Draw a line that rotates based on angle `t`.
    glVertex2f(x - r * cos(t), r * sin(t))
    glVertex2f(x + r * cos(t), -r * sin(t))
    glEnd()

# Function to draw the frame of a cycle.
def frame(x, y):
    glLineWidth(5)           # Set the width of the frame.
    glBegin(GL_LINE_STRIP)   # Begin drawing a continuous line strip.
    # Draw the triangular and rectangular parts of the cycle frame.
    glVertex2f(x, y)
    glVertex2f(x + 70, y + 70)
    glVertex2f(x + 200, y + 70)
    glVertex2f(x + 135, y)
    glVertex2f(x + 70, y + 70)
    glVertex2f(x + 200, y + 70)
    glVertex2f(x + 200, y + 100)
    glVertex2f(x + 190, y + 100)
    glVertex2f(x + 210, y + 100)
    glVertex2f(x + 200, y + 100)
    glVertex2f(x + 200, y + 70)
    glVertex2f(x + 270, y)   # Connect back to the second wheel's center.
    glEnd()

# Function to draw the scene.
def draw():
    glClear(GL_COLOR_BUFFER_BIT) # Clear the window with the background color.
    glColor3f(0, 0, 0)           # Set the drawing color to black.
    wheel(x, y, r)               # Draw the first wheel.
    wheel(x + 270, y, r)         # Draw the second wheel.
    line(x, r)                   # Draw the rotating spokes for the first wheel.
    line(x + 270, r)             # Draw the rotating spokes for the second wheel.
    frame(x, y)                  # Draw the cycle frame.
    glFlush()                    # Force execution of OpenGL commands.

# Function to animate the cycle movement and wheel rotation.
def animate(n):
    global x, y, r, win, t
    glutPostRedisplay()  # Mark the current window for redisplay.
    if x == 500:         # If the cycle moves out of the screen on the right.
        x = -500         # Reset its position to the left.
    else:
        x += n           # Move the cycle forward by `n`.
    if t == 360:         # If the angle completes a full rotation.
        t = 0            # Reset the angle.
    else:
        t += n - 0.8     # Increment the angle for wheel rotation.
    glutTimerFunc(16, animate, 1)  # Call this function every 16 ms (approx 60 FPS).

# Main function to initialize and run the OpenGL application.
def main():
    glutInit(argv)                   # Initialize GLUT.
    glutInitWindowSize(win, win)     # Set the window size.
    glutInitDisplayMode(GLUT_RGB)    # Set the display mode to RGB.
    glutCreateWindow("Cycle")        # Create a window with a title.
    glClearColor(1, 1, 1, 1)         # Set the background color to white.
    gluOrtho2D(-win, win, -win, win) # Set the 2D orthographic projection.
    glutDisplayFunc(draw)            # Register the display callback function.
    glutTimerFunc(0, animate, 0)     # Register the animation timer function.
    glutMainLoop()                   # Enter the GLUT event processing loop.

main()  # Run the program.
