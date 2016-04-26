import turtle

def square(length,radius):
	t = turtle.Turtle()
	for i in range(4):
		t.fd(length)
		t.lt(radius)
	turtle.mainloop()

square(100,90)
