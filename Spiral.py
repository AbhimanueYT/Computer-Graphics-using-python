from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import*
from sys import*
from math import*


win = 500
r=500
ang=0
an=10
tx = []
ty = []
x=y=0
ne=0
while r>=0:
	x=r*cos(ang)
	y=r*sin(ang)
	tx.append(x)
	ty.append(y)
	r-=1
	ang-=0.1

def spiral(tx,ty):
	glColor3f(1,0,0)
	glBegin(GL_LINE_STRIP)
	for l in range(0,len(tx)):
		glVertex2f(tx[l],ty[l])
	glEnd()
	
def ball(x,y,an):
	glColor3f(0,0,0)
	glBegin(GL_TRIANGLE_FAN)		
	for i in range(0,360):
		t=an*i
		glVertex2f(x+an*cos(t),y+an*sin(t))
	glEnd()
	
def draw():
	glClear(GL_COLOR_BUFFER_BIT)
	spiral(tx,ty)
	ball(x,y,an)
	glFlush()
	glutPostRedisplay()

def animate(n):
	global tx,ty,x,y,an,ne
	if ne<len(tx):
		x=tx[ne]
		y=ty[ne]
		ne+=n
	
	glutTimerFunc(16,animate,1)
		

def main():
	glutInit(argv)
	glutInitWindowSize(win,win)
	glutInitDisplayMode(GLUT_RGB)
	glutCreateWindow("Spiral")
	glutDisplayFunc(draw)
	glutTimerFunc(0,animate,0)
	glClearColor(1,1,1,1)
	gluOrtho2D(-win,win,-win,win)
	glutMainLoop()
main()
