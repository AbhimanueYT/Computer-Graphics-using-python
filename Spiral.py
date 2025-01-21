# Importing necessary modules for OpenGL rendering, math functions, and system operations
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from sys import *
from math import *

# Window size and initial parameters for the spiral and ball animation
win = 500  # Window size (500x500)
r = 500  # Initial radius of the spiral
ang = 0  # Initial angle for the spiral
an = 10  # Radius of the moving ball
tx = []  # List to store x-coordinates of the spiral points
ty = []  # List to store y-coordinates of the spiral points
x = y = 0  # Initial coordinates of the moving ball
ne = 0  # Index to track the position of the ball along the spiral

# Generating points for the spiral
while r >= 0:
    x = r * cos(ang)  # Compute x-coordinate using polar coordinates
    y = r * sin(ang)  # Compute y-coordinate using polar coordinates
    tx.append(x)  # Append x-coordinate to the list
    ty.append(y)  # Append y-coordinate to the list
    r -= 1  # Decrease the radius to create a spiral effect
    ang -= 0.1  # Decrease the angle to generate the spiral

# Function to draw the spiral
def spiral(tx, ty):
    glColor3f(1, 0, 0)  # Set the color of the spiral to red
    glBegin(GL_LINE_STRIP)  # Begin drawing a line strip
    for l in range(0, len(tx)):  # Loop through all points of the spiral
        glVertex2f(tx[l], ty[l])  # Specify each vertex of the spiral
    glEnd()  # End drawing

# Function to draw the moving ball
def ball(x, y, an):
    glColor3f(0, 0, 0)  # Set the color of the ball to black
    glBegin(GL_TRIANGLE_FAN)  # Begin drawing a filled circle
    for i in range(0, 360):  # Loop through angles to create the circular shape
        t = an * i  # Calculate angle in radians
        glVertex2f(x + an * cos(t), y + an * sin(t))  # Compute and specify the vertices of the circle
    glEnd()  # End drawing

# Function to handle drawing on the screen
def draw():
    glClear(GL_COLOR_BUFFER_BIT)  # Clear the color buffer
    spiral(tx, ty)  # Draw the spiral
    ball(x, y, an)  # Draw the moving ball
    glFlush()  # Flush the OpenGL commands
    glutPostRedisplay()  # Request to redraw the screen

# Timer function to animate the ball along the spiral
def animate(n):
    global tx, ty, x, y, an, ne
    if ne < len(tx):  # Check if the ball has not reached the end of the spiral
        x = tx[ne]  # Update x-coordinate of the ball
        y = ty[ne]  # Update y-coordinate of the ball
        ne += n  # Increment the index to move the ball along the spiral
    glutTimerFunc(16, animate, 1)  # Set a timer to call animate every 16ms

# Main function to initialize OpenGL and start the application
def main():
    glutInit(argv)  # Initialize the GLUT library
    glutInitWindowSize(win, win)  # Set the window size
    glutInitDisplayMode(GLUT_RGB)  # Set the display mode to RGB
    glutCreateWindow("Spiral")  # Create a window with the title "Spiral"
    glutDisplayFunc(draw)  # Register the display callback function
    glutTimerFunc(0, animate, 0)  # Register the timer callback for animation
    glClearColor(1, 1, 1, 1)  # Set the background color to white
    gluOrtho2D(-win, win, -win, win)  # Set up an orthogonal projection
    glutMainLoop()  # Enter the GLUT main loop to run the application

# Run the main function to start the program
main()
