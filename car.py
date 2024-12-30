from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import*
from math import*

win=500
x=y=0
r=20
t=0
c=1
s=0.01


def body(x,y):
	glBegin(GL_POLYGON)
	glVertex2f(x,y)
	glVertex2f(x,y+25)
	glVertex2f(x+75,y+100)
	glVertex2f(x+300,y+25)
	glVertex2f(x+300,y)
	glEnd()

def line(x,r,t):
	glBegin(GL_LINES)
	glVertex2f(x-r*cos(t),r*sin(t))
	glVertex2f(x-(-r)*cos(t),-r*sin(t))
	glEnd()

def wheel(x,y,r):
	glBegin(GL_TRIANGLE_FAN)
	for i in range(0,360):
		glVertex2f(x+r*cos((pi*i)/180),y+r*sin((pi*i)/180))
	glEnd()

def draw():
	glClear(GL_COLOR_BUFFER_BIT)
	glColor3f(0,1,1)
	body(x,y)
	glColor3f(0,0,0)
	wheel(x+50,y,r)
	wheel(x+200,y,r)
	glColor3f(1,0,0)
	line(x+50,r,t)
	line(x+200,r,t)
	animation()
	glFlush()
	glutSwapBuffers()
	glutPostRedisplay()
	
def animation():
	global t,x,y,c,s
	if c==0:
		if x>=-500:
			x-=s+0.05
		else:
			x=500
		if t>=-360:
			t-=s
		else:
			t=0
	elif c==1:
		if x<=500:
			x+=s+0.05
		else:
			x=-500
		if t<=360:
			t+=s
		else:
			t=0
	
def keyboard(key,x,y):
	global c,s
	key=key.decode()
	if key=='d':
		c=1
		s+=0.01
	elif key=='a':
		c=0
		s-=0.01

def main():
	glutInit(sys.argv)
	glutInitWindowSize(win,win)
	glutInitDisplayMode(GLUT_RGB)
	glutCreateWindow("CAR")
	glClearColor(1,1,1,1)
	gluOrtho2D(-win,win,-win,win)
	glutDisplayFunc(draw)
	glutKeyboardFunc(keyboard)
	glutMainLoop()
main()
