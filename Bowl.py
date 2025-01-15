# Import necessary modules for OpenGL rendering, math operations, and system functions
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from math import *
from sys import *

# Global variables
win = 500  # Window size
r = 20     # Radius of the ball
t = 0      # Angle for the line movement (pendulum effect)
c = 60     # Maximum rotation angle
f = 0      # Direction of rotation (0 = clockwise, 1 = counterclockwise)
angle = 0  # Current rotation angle of the ball

# Function to draw a filled circle (ball)
def ball(r):
    glBegin(GL_TRIANGLE_FAN)  # Start drawing a triangle fan
    for i in range(0, 360):  # Loop through 360 degrees
        xc = r * cos(pi * i / 180)  # X-coordinate of the circle
        yc = r * sin(pi * i / 180)  # Y-coordinate of the circle
        glVertex2f(xc, yc)  # Plot the vertex
    glEnd()  # End the drawing

# Function to draw a line (representing a string attached to the ball)
def line(r):
    glLineWidth(3)  # Set line width
    glBegin(GL_LINES)  # Start drawing lines
    glVertex2f(-r * cos(t), r * sin(t))  # Start point of the line
    glVertex2f(r * cos(t), -r * sin(t))  # End point of the line
    glEnd()  # End the drawing

# Function to draw the bowl (semi-circle)
def bowl(r):
    glLineWidth(2)  # Set line width
    glBegin(GL_LINE_STRIP)  # Start drawing connected lines
    theta = 0  # Initialize angle
    for i in range(0, 180):  # Loop through 180 degrees
        glVertex2f(r * cos(pi * theta / 180), r * sin(pi * theta / 180))  # Plot the vertex
        theta -= 1  # Decrease angle by 1 degree
    glEnd()  # End the drawing

# Function to handle drawing and rendering
def draw():
    glClear(GL_COLOR_BUFFER_BIT)  # Clear the screen
    glPushMatrix()  # Save the current transformation matrix

    glScalef(2, 2, 0)  # Scale the objects for better visibility
    glPushMatrix()  # Save the scaled matrix
    glRotatef(angle, 0, 0, 1)  # Rotate the ball and string based on the angle
    glTranslatef(0, -100, 0)  # Translate the ball downwards
    glColor3f(1, 0, 0)  # Set color to red
    ball(r)  # Draw the ball
    glColor3f(0, 0, 0)  # Set color to black
    line(r)  # Draw the string
    glPopMatrix()  # Restore the previous transformation matrix

    glColor3f(0, 1, 0)  # Set color to green
    bowl(r + 100)  # Draw the bowl
    glPopMatrix()  # Restore the original transformation matrix

    glFlush()  # Flush the OpenGL commands to the screen

# Function to handle animation
def animate(n):
    global t, c, angle, f
    glutPostRedisplay()  # Mark the window as needing to be redisplayed

    if c <= 5:  # If the maximum rotation angle is too small, stop the animation
        c = 0
        return

    if angle >= c:  # If the angle reaches the maximum, change direction
        f = 1
    if angle <= -c:  # If the angle reaches the negative maximum, change direction
        f = 0

    if f == 0:  # Clockwise rotation
        angle += n
        t += n - 0.8
    if f == 1:  # Counterclockwise rotation
        angle -= n
        t -= n - 0.8

    if angle == 0:  # Reduce the maximum angle slightly when passing the center
        c -= 2

    glutTimerFunc(16, animate, 1)  # Set a timer for the next animation frame (16ms)

# Main function to initialize the program
def main():
    glutInit(argv)  # Initialize GLUT with system arguments
    glutInitWindowSize(win, win)  # Set the window size
    glutInitDisplayMode(GLUT_RGB)  # Use RGB color mode
    glutCreateWindow("Ball in Bowl")  # Create the window with a title
    glutDisplayFunc(draw)  # Set the display callback function
    glutTimerFunc(0, animate, 0)  # Set the timer callback for animation
    glClearColor(1, 1, 1, 1)  # Set the background color to white
    gluOrtho2D(-win, win, -win, win)  # Set the orthographic projection for 2D rendering
    glutMainLoop()  # Enter the GLUT main loop

# Start the program
main()
