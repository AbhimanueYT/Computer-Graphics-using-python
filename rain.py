from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import*
from math import*
from sys import*
from random import*

s=2
v=0
z=-40
p=0
win=500
rain=[]
k=y=0


for i in range (-500,500,10):
	speed=randint(10,20)
	rain.append([i,500+randint(1,10),speed])
	



def rains(x,y):
	glColor3f(0,0,0)
	glPointSize(1.6)
	glBegin(GL_POINTS)
	glVertex2f(x,y)
	glEnd()
	
	
def box(x,y,r,c=[1,0,0]):
	glColor3f(c[0],c[1],c[2])
	glBegin(GL_TRIANGLE_FAN)
	for i in range (0,360):
		t=r*i
		xc=x+r*cos(t)
		yc=y+r*sin(t)
		glVertex(xc,yc)
	glEnd()
	
def rode(x,y,w,h):
	glColor(0,0,0)
	glBegin(GL_QUADS)
	glVertex2f(x+w,y+h)
	glVertex2f(x+w,y-h)
	glVertex2f(x-w,y-h)
	glVertex2f(x-w,y+h)
	glEnd()
	
def draw():
	global rain,k,y
	glClear(GL_COLOR_BUFFER_BIT)
	for x in rain:
		rains(x[0],x[1])
	box(k,y,100)
	box(k,y-20,100,c=[1,1,1])
	rode(k,y-20,5,100)
	box(k,y-120,10,c=[0,0,0])
	
	glFlush()
	glutSwapBuffers()
	glutPostRedisplay()
	
def keyboard(value):
	global k
	k+=value
	
	
def animate(value):
	global rain,k
	k+=value
	for x in rain:
		x[1]=x[1]-x[2]
		if x[1]<-500:
			x[1]=500
			x[2]=randint(10,20)
	glutTimerFunc(100,animate,0)
	
def arrow(key,k,y):
	i=0
	if key==GLUT_KEY_LEFT:
		i-=1
		keyboard(i)
	elif key==GLUT_KEY_RIGHT:
		i+=1
		keyboard(i)
	elif key==GLUT_KEY_DOWN:
		i=0
		keyboard(i)
		

def main():
	glutInit(sys.argv)
	glutInitWindowSize(win,win)
	glutInitDisplayMode(GLUT_RGBA)
	glutCreateWindow("Rain")
	glutDisplayFunc(draw)
	glutSpecialFunc(arrow)
	glutTimerFunc(0,animate,0)
	glClearColor(1,1,1,1)
	gluOrtho2D(-win,win,-win,win)
	glutMainLoop()
	
main()
