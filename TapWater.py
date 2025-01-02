from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import*
from sys import*

win = 500
n=y=x=0
f=1

def water(x,y,n):
	glBegin(GL_POLYGON)
	glVertex2f(x,y)
	glVertex2f(x+100,y)
	glVertex2f(x+100,y+n)
	glVertex2f(x,y+n)
	glEnd()

def bucket(x,y):
	glLineWidth(2)
	glBegin(GL_LINE_STRIP)
	glVertex(x,y+300)
	glVertex(x,y)
	glVertex2f(x+100,y)
	glVertex2f(x+100,y+300)
	glEnd()

def tap(x,y):
	glLineWidth(5)
	glBegin(GL_LINE_STRIP)
	glVertex2f(x,y)
	glVertex2f(x+30,y)
	glVertex2f(x+30,y-10)
	glVertex2f(x+30,y)
	glVertex2f(x+19,y)
	glVertex2f(x+19,y+2)
	glVertex2f(x+10,y+2)
	glVertex2f(x+10,y-2)
	glVertex2f(x+19,y-2)
	glVertex2f(x+19,y)
	glVertex2f(x,y)
	glEnd()
	
def lid(x,y):
	glBegin(GL_QUADS)
	glVertex2f(x+5,y+2)
	glVertex2f(x+5,y-2)
	glVertex2f(x-5,y-2)
	glVertex2f(x-5,y+2)
	glEnd()

def line(x,y):
	glLineWidth(4)
	glBegin(GL_LINES)
	glVertex2f(x,y)
	glVertex2f(x,y-65)
	glEnd()

def draw():
	glClear(GL_COLOR_BUFFER_BIT)
	glColor3f(0,0.6,1)
	water(x,y,n)
	glColor3f(0,0,0)
	bucket(x,y)
	glPushMatrix()
	glTranslatef(-100,330,0)
	glScalef(5,5,1)
	glColor3f(0,1,0)
	if f==1:
		glPushMatrix()
		glTranslatef(15,5,0)
		glRotatef(45,0,0,1)
		glTranslatef(-15,-5,0)
		lid(x+15,y+5)
		glPopMatrix()
	else:
		lid(x+20,y+5)
		glColor3f(0,0.6,1)
		line(x+30,y)
	glColor3f(1,0,0)
	tap(x,y)
	glPopMatrix()
	
	glFlush()

def animate(v):
	global x,y,n,f
	glutPostRedisplay()
	if n<=200:
		n+=v
		f=0
	else:
		f=1
	glutTimerFunc(16,animate,1)

def main():
	glutInit(argv)
	glutInitWindowSize(win,win)
	glutInitDisplayMode(GLUT_RGB)
	glutCreateWindow("Water")
	glutDisplayFunc(draw)
	glutTimerFunc(1000,animate,0)
	glClearColor(1,1,1,1)
	gluOrtho2D(-win,win,-win,win)
	glutMainLoop()
	
main()
