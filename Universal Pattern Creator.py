import turtle
import random 


screen = turtle.Screen()
bob = turtle.Turtle()
screen.bgcolor("black")
bob.pencolor("cyan")
bob.speed(10000)
def crazy(var1):
	for i in range(360):
		bob.forward(i)
		bob.left(var1)
crazy(555)		

    
# Range = 360
# Crazy = 34
# Crazy = 50

#speed = 100
#crazy = 34

#crazy = 90,167,124,78,137,656,988,555
