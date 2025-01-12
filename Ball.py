from OpenGL.GL import *  # Core OpenGL functions
from OpenGL.GLU import *  # Utility library for OpenGL
from OpenGL.GLUT import *  # Toolkit for creating windows and handling input
from math import *  # Provides mathematical functions like sin, cos, and pi

# Window size and initial parameters
win = 500  # Width and height of the window
x = y = 0  # Initial position of the ball (centered at origin)
r = 50  # Radius of the ball
t = 0  # Angle for the rotating line
n = 1  # Step size for animation

# Function to draw a ball (circle) using triangle fans
def ball(x, y, r):
    glBegin(GL_TRIANGLE_FAN)  # Begin drawing a filled circle
    for i in range(0, 360):  # Loop through angles from 0 to 360 degrees
        # Calculate the x and y coordinates for each point on the circle
        xc = x + r * cos(pi * i / 180)
        yc = y + r * sin(pi * i / 180)
        glVertex2f(xc, yc)  # Define a vertex of the circle
    glEnd()  # End the drawing of the circle

# Function to draw a rotating line across the ball
def line(x, y, r):
    glLineWidth(3)  # Set line width
    glBegin(GL_LINES)  # Begin drawing lines
    # First endpoint of the line (rotating based on angle `t`)
    glVertex2f(x - r * cos(t), y + r * sin(t))
    # Second endpoint of the line
    glVertex2f(x + r * cos(t), y - r * sin(t))
    glEnd()  # End the line drawing

# Function to draw a base platform as a polygon
def base():
    glBegin(GL_POLYGON)  # Begin drawing a filled polygon
    # Define the vertices of the platform
    glVertex2f(-500, -500)  # Bottom-left
    glVertex2f(-500, 500)  # Top-left
    glVertex2f(-100, -100)  # Top-right
    glVertex2f(500, -100)  # Middle-right
    glVertex2f(500, -500)  # Bottom-right
    glEnd()  # End the polygon drawing

# Function to draw all elements (ball, line, and base) in the window
def draw():
    glClear(GL_COLOR_BUFFER_BIT)  # Clear the screen
    glColor3f(1, 0, 0)  # Set color to red
    ball(x, y, r)  # Draw the ball
    glColor3f(0, 0, 0)  # Set color to black
    line(x, y, r)  # Draw the rotating line
    glColor3f(0, 1, 0)  # Set color to green
    base()  # Draw the base platform
    glFlush()  # Ensure all commands are executed

# Function to animate the ball and line
def animate(n):
    global x, y, r, t  # Use global variables for animation
    glutPostRedisplay()  # Trigger the `draw` function to redraw the frame

    # Update the ball's position
    if x >= 500:  # If the ball moves off the right edge of the window
        x = -450  # Reset its horizontal position
        y = 500  # Reset its vertical position
    else:
        x += n  # Move the ball to the right
        if y > -50:  # If the ball is above the platform
            y -= n + 0.4  # Move the ball downward

    # Update the rotation angle of the line
    if t >= 360:  # Reset the angle after a full rotation
        t = 0
    else:
        t += n  # Increment the angle for rotation

    # Schedule the next animation frame
    glutTimerFunc(1, animate, 1)

# Main function to initialize the OpenGL context and start the application
def main():
    glutInit(sys.argv)  # Initialize the GLUT library
    glutInitWindowSize(win, win)  # Set the window size
    glutInitDisplayMode(GLUT_RGB)  # Use RGB color mode
    glutCreateWindow("Ball")  # Create the window with a title
    glutDisplayFunc(draw)  # Register the `draw` function as the display callback
    glutTimerFunc(10, animate, 1)  # Start the animation with a timer callback
    glClearColor(1, 1, 1, 1)  # Set the background color to white
    gluOrtho2D(-win, win, -win, win)  # Define a 2D orthographic projection
    glutMainLoop()  # Start the GLUT event loop

# Entry point of the program
main()
