from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

win=500

def display():

    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 1.0, 1.0)
    
    text="Hello World!"
    glRasterPos2f(-0.2, 0)
    for i in text:
        glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24, ord(i))
    text=123456
    glRasterPos2f(-0.2, -0.2)
    for i in str(text):
        glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24, ord(i))   
        
    glutSwapBuffers()



def main():
    glutInit()
    glutInitDisplayMode(GLUT_RGBA)
    glutInitWindowSize(win, win)
    glutCreateWindow("OpenGL Text Example")
    glutDisplayFunc(display)
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glutMainLoop()

main()
