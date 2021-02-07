from turtle import*

speed(1)
bgcolor("black")
penup()
goto(0,-225)
pendown()
color("white")
begin_fill()
circle(225)
end_fill()
penup()
goto(0,0)
pendown()
color("black")
begin_fill()
for i in range(3):
    right(120)
    for i in range(3):
        forward(200)
        right(120)
end_fill()
hideturtle()
