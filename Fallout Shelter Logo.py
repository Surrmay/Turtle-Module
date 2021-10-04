from turtle import *

#Dimention of Object
speed(0)
penup()
color("gold")
goto(0,-223)
pendown()
color("black")
begin_fill()
circle(235)
end_fill()
penup()
goto(0,0)
pendown()
color("gold")
begin_fill()

#Base for pen to create object
for i in range(3):
	right(120)
	for i in range(3):
		forward(200)
		right(120)

end_fill()
hideturtle()
