from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import*
from sys import*

win = 500
c=0
a=0

def rope(x1,y1,x2,y2):
	glLineWidth(2)
	glBegin(GL_LINES)
	glVertex2f(x1,y1)
	glVertex2f(x2,y2)
	glEnd()

def seat(x,y,h,w):
	glBegin(GL_QUADS)
	glVertex2f(20+x+w,y+h)
	glVertex2f(x+w,y-h)
	glVertex2f(x-w,y-h)
	glVertex2f(20+x-w,y+h)
	glEnd()
	
def swing():
	glClear(GL_COLOR_BUFFER_BIT)
	glColor3f(0,0,0)
	glPushMatrix()
	glRotatef(a,0,0,1)
	rope(50,-350,50,10)
	rope(240,-350,240,10)
	glColor3f(1,0,0)
	seat(130,-350,30,100)
	glPopMatrix()
	animate(0.05)
	glFlush()
	glutSwapBuffers()
	
	
def animate(s):
	global c,a
	glutPostRedisplay()
	if c==1:
		if a>=30:
			c=0
			a-=s
		else:
			a+=s
	elif c==0:
		if a<=-30:
			c=1
			a+=s
		else:
			a-=s

def main():
	glutInit(sys.argv)
	glutInitWindowSize(win,win)
	glutInitDisplayMode(GLUT_RGBA)
	glutCreateWindow("Swing")
	glutDisplayFunc(swing)
	glClearColor(1,1,1,1)
	gluOrtho2D(-win,win,-win,win)
	glutMainLoop()
	
main()
