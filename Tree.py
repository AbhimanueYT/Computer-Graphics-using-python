from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import*
from sys import*
from math import*
from random import*

win = 500
x=0
y=-400
r=50
v=w=1
c=k=0
g=g1=50

def trunk(x,y,v,w):
	glColor3f(0.74,0.45,0)
	glBegin(GL_QUADS)
	glVertex2f(x+10+w,y+10+v)
	glVertex2f(x+10+w,y-100-v)
	glVertex2f(x-10-w,y-100-v)
	glVertex2f(x-10-w,y+10+v)
	glEnd()

def leaf(x,y,r):
	
	glBegin(GL_TRIANGLE_FAN)
	for i in range(0,360):
		t=r*i
		xc=x+r*cos(t)
		yc=y+r*sin(t)
		glVertex2f(xc,yc)
	glEnd()
	

def draw():
	glClear(GL_COLOR_BUFFER_BIT)
	glPushMatrix()
	glTranslate(0,v,1)
	trunk(x,y,v,w)
	if c==1:
		glColor3f(0,0.9,0)
		leaf(x+g,y+w,r)
		leaf(x-g,y+w,r)
		if k==1:
			leaf(x-g1,y+g1+w,r)
			leaf(x,y+g1+w,r)
			leaf(x+g1,y+g1+w,r)	
	glColor3f(0,1,0)
	leaf(x+50,y+w,r)
	leaf(x-50,y+w,r)
	leaf(x,y+50+w,r)
	glPopMatrix()
	glutSwapBuffers()
	glFlush()
	
def animate(n):
	global x,y,r,v,w,c,k,g,g1
	glutPostRedisplay()
	if v<=200:
		v+=n
	if w<=50:
		w+=0.5
	if r<=200:
		r+=1
	if r>=100 and r<=150:
		c=1
		g+=1
	if r>=150 and r<=200:
		k=1
		g1+=1
	glutTimerFunc(100,animate,2)
	

def main():
	glutInit(argv)
	glutInitWindowSize(win,win)
	glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE)
	glutCreateWindow("Tree")
	glClearColor(1,1,1,1)
	gluOrtho2D(-win,win,-win,win)
	glutDisplayFunc(draw)
	glutTimerFunc(0,animate,0)
	glutMainLoop()

main()
