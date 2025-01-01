from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import*
from sys import*
from math import*

win = 500
i=90
r=400
h=90
m=90

def circle(r):
	glPointSize(6)
	glBegin(GL_POINTS)
	for i in range (0,360):
		glVertex2f(r*cos((pi*i)/180),r*sin((pi*i)/180))
	glEnd()
	
	
def hand(r,i):
	glLineWidth(5)
	glBegin(GL_LINES)
	glVertex2f(0,0)
	glVertex2f(r*cos((pi*i)/180),r*sin((pi*i/180)))
	glEnd()
	
def clock():
	glClear(GL_COLOR_BUFFER_BIT)
	glColor3f(0,0,0)
	str='Clock'
	glRasterPos2f(-50,450)
	for char in str:
		glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24,ord(char))
	circle(r)
	glColor3f(1,0,0)
	hand(r-50,i)
	glColor3f(0,1,0)
	hand(r-100,h)
	glColor3f(0,0,1)
	hand(r-150,m)
	glFlush()

def animate(n):
	global i,h,m
	glutPostRedisplay()
	if i==-270:
		i=90
		if h==-270:
			h=90
			if m==-270:
				m=90
			else:
				m-=n
		else:
			h-=n
	else:
		i-=n
	glutTimerFunc(1,animate,1)

def main():
	glutInit(sys.argv)
	glutInitWindowSize(win,win)
	glutInitDisplayMode(GLUT_RGB)
	glutCreateWindow("Clock")
	glutDisplayFunc(clock)
	glutTimerFunc(0,animate,1)
	glClearColor(1,1,1,1)
	gluOrtho2D(-win,win,-win,win)
	glutMainLoop()
main()
