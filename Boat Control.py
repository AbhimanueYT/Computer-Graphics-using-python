from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import*
from math import*
from sys import*
from playsound import playsound

win=500
x=y=0
a=35
r=50

def rode(x,y,r,w,h):
	glBegin(GL_TRIANGLE_FAN)
	for i in range (0,360):
		theta=r*i
		xc = x+r*cos(theta)
		yc = y+r*sin(theta)
		glVertex2f(xc,yc-100)
	glEnd()
	glBegin(GL_QUADS)
	glVertex2f(x+w,y+h)
	glVertex2f(x+w,y-h)
	glVertex2f(x-w,y-h)
	glVertex2f(x-w,y+h)
	glEnd()

def frame(x,y):
	glBegin(GL_QUADS)
	glVertex2f(x+300,y+80)
	glVertex2f(x+200,y-80)
	glVertex2f(x-200,y-80)
	glVertex2f(x-300,y+80)
	glEnd()

def water():
	glBegin(GL_QUADS)
	glVertex2f(500,0)
	glVertex2f(500,-500)
	glVertex2f(-500,-500)
	glVertex2f(-500,0)
	glEnd()

def dude(x,y,r,w,h):
	glBegin(GL_TRIANGLE_FAN)
	for i in range (0,360):
		theta=r*i
		xc = x+r*cos(theta)
		yc = y+r*sin(theta)
		glVertex2f(xc,yc+150)
	glEnd()
	glBegin(GL_QUADS)
	glVertex2f(x+w,y+h+100)
	glVertex2f(x+w,y-h)
	glVertex2f(x-w,y-h)
	glVertex2f(x-w,y+h+40)
	glEnd()

def boat():
	global x,y,a
	glClear(GL_COLOR_BUFFER_BIT)
	glColor3f(0,0.8,1)
	water()
	glColor3f(0,0,0)
	dude(x,y,40,50,50)
	glColor3f(0,1,0)
	frame(x,y)
	glPushMatrix()
	glTranslate(x,0,0)
	glRotate(a,0,0,1)
	glTranslate(-x,0,0)
	glColor3f(1,0,0)
	rode(x,y,r,10,150)
	glPopMatrix()
	glFlush()
	glutSwapBuffers()
	

def arrow(key,x,y):
	i=0
	if key==GLUT_KEY_RIGHT:
		i+=1
		animate(i)
	elif key==GLUT_KEY_LEFT:
		i-=1
		animate(i)
	elif key==GLUT_KEY_DOWN:
		i=0
		animate(i)
		
def keyboard(ckey,x,y):
	ckey=ckey.decode()
	if ckey=='h':
		playsound('/home/abhimanue/Desktop/Abhimanue/bushorn.mp3')
	elif ckey=='H':
		playsound('/home/abhimanue/Desktop/Abhimanue/bushorn.mp3')

	
def animate(i):
	global x,y,a,win
	glutPostRedisplay()
	if i==0:
	 return
	if x==win+100:
		x=-win
	elif x==-win-100:
		x=win
	else:
		x+=i
	if a==-45:
		a=40
	elif a==45:
		a=-40
	else:
		a-=i
	
	


def main():
	glutInit(sys.argv)
	glutInitWindowSize(win,win)
	glutInitWindowPosition(0,0)
	glutInitDisplayMode(GLUT_RGBA)
	glutCreateWindow("Boat Control")
	glutDisplayFunc(boat)
	glutIdleFunc(boat)
	glutSpecialFunc(arrow)
	glutKeyboardFunc(keyboard)
	glClearColor(1,1,1,1)
	gluOrtho2D(-win,win,-win,win)
	glutMainLoop()

main()
