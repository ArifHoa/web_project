import turtle
turtle.color('red','yellow')
turtle.begin_fill()
while True:
    turtle.forward(100)	
    turtle.forward(70)	
    if abs (turtle.position())<5:
        break
turtle.end_fill()
turtle.done()
			