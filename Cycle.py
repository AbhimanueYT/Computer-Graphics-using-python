from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import*
from sys import*
from math import*

win = 500
x=y=0
r=50
t=0

def wheel(x,y,r):
	glPointSize(2)
	glBegin(GL_POINTS)
	for i in range(0,360):
		glVertex2f(x+r*cos(pi*i/180),y+r*sin(pi*i/180))
	glEnd()

def line(x,r):
	glLineWidth(2)
	glBegin(GL_LINES)
	glVertex2f(x-r*cos(t),r*sin(t))
	glVertex2f(x--r*cos(t),-r*sin(t))
	glEnd()

def frame(x,y):
	glLineWidth(5)
	glBegin(GL_LINE_STRIP)
	glVertex2f(x,y)
	glVertex2f(x+70,y+70)
	glVertex2f(x+200,y+70)
	glVertex2f(x+135,y)
	glVertex2f(x+70,y+70)
	glVertex2f(x+200,y+70)
	glVertex2f(x+200,y+100)
	glVertex2f(x+190,y+100)
	glVertex2f(x+210,y+100)
	glVertex2f(x+200,y+100)
	glVertex2f(x+200,y+70)
	glVertex2f(x+270,y)
	glEnd()

def draw():
	glClear(GL_COLOR_BUFFER_BIT)
	glColor3f(0,0,0)
	wheel(x,y,r)
	wheel(x+270,y,r)
	line(x,r)
	line(x+270,r)
	frame(x,y)
	glFlush()

def animate(n):
	global x,y,r,win,t
	glutPostRedisplay()
	if x==500:
		x=-500
	else:
		x+=n
	if t==360:
		t=0
	else:
		t+=n-0.8
	glutTimerFunc(16,animate,1)
	
def main():
	glutInit(argv)
	glutInitWindowSize(win,win)
	glutInitDisplayMode(GLUT_RGB)
	glutCreateWindow("Cycle")
	glClearColor(1,1,1,1)
	gluOrtho2D(-win,win,-win,win)
	glutDisplayFunc(draw)
	glutTimerFunc(0,animate,0)
	glutMainLoop()
main()
