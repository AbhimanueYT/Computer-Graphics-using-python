from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import*
from math import*

win = 500
x=y=0
r=50
t=0
n=1


def ball(x,y,r):
	glBegin(GL_TRIANGLE_FAN)
	for i in range(0,360):
		xc=x+r*cos(pi*i/180)
		yc=y+r*sin(pi*i/180)
		glVertex2f(xc,yc)
	glEnd()
	
def line(x,y,r):
	glLineWidth(3)
	glBegin(GL_LINES)
	glVertex2f(x-r*cos(t),y+r*sin(t))
	glVertex2f(x--r*cos(t),y-r*sin(t))
	glEnd()
	
def base():
	glBegin(GL_POLYGON)
	glVertex2f(-500,-500)
	glVertex2f(-500,500)
	glVertex2f(-100,-100)
	glVertex2f(500,-100)
	glVertex2f(500,-500)
	glEnd()
	
def draw():
	glClear(GL_COLOR_BUFFER_BIT)
	glColor3f(1,0,0)
	ball(x,y,r)
	glColor3f(0,0,0)
	line(x,y,r)
	glColor3f(0,1,0)
	base()
	glFlush()
	
def animate(n):
	global x,y,r,t
	glutPostRedisplay()
	if x>=500:
		x=-450
		y=500
	else:
		x+=n
		if y>-50:
			y-=n+0.4
	if t>=360:
		t=0
	else:
		t+=n
	glutTimerFunc(1,animate,1)
			

def main():
	glutInit(sys.argv)
	glutInitWindowSize(win,win)
	glutInitDisplayMode(GLUT_RGB)
	glutCreateWindow("Ball")
	glutDisplayFunc(draw)
	glutTimerFunc(10,animate,1)
	glClearColor(1,1,1,1)
	gluOrtho2D(-win,win,-win,win)
	glutMainLoop()
	
main()
