from OpenGL.GL import*                   # Import OpenGL functions for rendering
from OpenGL.GLU import*                  # Import OpenGL utility functions
from OpenGL.GLUT import*                 # Import OpenGL GLUT functions for window and event handling
from sys import*                         # Import system functions
from math import*                        # Import mathematical functions

win = 500                                # Window size
i=90                                     # Initial angle for seconds hand
r=400                                    # Radius of the clock circle
h=90                                     # Initial angle for minutes hand
m=90                                     # Initial angle for hours hand

def circle(r):                          # Function to draw the clock circle
	glPointSize(6)                        # Set point size
	glBegin(GL_POINTS)                    # Begin drawing points
	for i in range(0,360):                # Loop through 360 degrees
		glVertex2f(r*cos((pi*i)/180),r*sin((pi*i)/180)) # Calculate and plot points on the circle
	glEnd()

def hand(r,i):                          # Function to draw clock hands
	glLineWidth(5)                        # Set line width
	glBegin(GL_LINES)                     # Begin drawing a line
	glVertex2f(0,0)                       # Start point of the line (center of the clock)
	glVertex2f(r*cos((pi*i)/180),r*sin((pi*i/180))) # End point of the line
	glEnd()

def clock():                            # Function to draw the clock
	glClear(GL_COLOR_BUFFER_BIT)          # Clear the screen
	glColor3f(0,0,0)                      # Set color to black
	str='Clock'                           # Title string
	glRasterPos2f(-50,450)                # Position the title
	for char in str:                      # Loop through each character in the title
		glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24,ord(char)) # Render each character
	circle(r)                             # Draw the clock circle
	glColor3f(1,0,0)                      # Set color to red
	hand(r-50,i)                          # Draw the seconds hand
	glColor3f(0,1,0)                      # Set color to green
	hand(r-100,h)                         # Draw the minutes hand
	glColor3f(0,0,1)                      # Set color to blue
	hand(r-150,m)                         # Draw the hours hand
	glFlush()                             # Flush the OpenGL commands

def animate(n):                         # Function to animate the clock hands
	global i,h,m                          # Use global variables for hand angles
	glutPostRedisplay()                   # Request to redisplay the window
	if i==-270:                           # Reset seconds hand when it completes a circle
		i=90
		if h==-270:                        # Reset minutes hand when it completes a circle
			h=90
			if m==-270:                    # Reset hours hand when it completes a circle
				m=90
			else:
				m-=n                        # Move hours hand
		else:
			h-=n                            # Move minutes hand
	else:
		i-=n                                # Move seconds hand
	glutTimerFunc(1,animate,1)            # Set timer to call animate function

def main():                             # Main function
	glutInit(sys.argv)                    # Initialize GLUT
	glutInitWindowSize(win,win)           # Set the window size
	glutInitDisplayMode(GLUT_RGB)         # Set the display mode to RGB
	glutCreateWindow("Clock")            # Create a window with title "Clock"
	glutDisplayFunc(clock)                # Register the display function
	glutTimerFunc(0,animate,1)            # Register the timer function
	glClearColor(1,1,1,1)                 # Set background color to white
	gluOrtho2D(-win,win,-win,win)         # Set the orthographic projection
	glutMainLoop()                        # Enter the GLUT event processing loop

main()
