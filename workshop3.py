from graphics import*
from time import*
from random import*

win=GraphWin("My Program", 500, 500)

def RandomCircle100():
	x=randint(50,450)
	y=randint(50,450)
	my_point=Point(x,y)
	my_circle=Circle(my_point, 100)
	return(my_circle)

first_circle = RandomCircle100()
first_circle.setFill("red")
first_circle.draw(win)

first_circle = RandomCircle100()
first_circle.setFill("blue")
first_circle.draw(win)

win2=GraphWin("My Program 2", 500, 500)

def DrawUntilClick():
	while win2.checkMouse()==None:
		circles=RandomCircle100()
		circles.draw(win2)

DrawUntilClick()

win3=GraphWin("My Program 3", 500, 500)

def AlternateColors(circle): 
	circle.draw(win3)
	while win3.checkMouse()==None:
		circle.setFill("blue")
		sleep(1)
		circle.setFill("red")
		sleep(1)
		

my_circle2=RandomCircle100()
AlternateColors(my_circle2)

win4=GraphWin("My Program 4", 500, 500)

def ManyColoredCircles():
	y=0
	while y<400:
		new_point = win4.getMouse()
		x = new_point.getX()
		y = new_point.getY()
		my_circle3=Circle(Point(x,y), 100)
		my_circle3.draw(win4)
		if x<=250 and y<400: 
			my_circle3.setFill("blue")
		if x>250 and y<400:
			my_circle3.setFill("red")
		
ManyColoredCircles()

win5=GraphWin("My Program 5", 500, 500)

def MoveRight(circle1):
	circle1.draw(win5)
	sleep(1)	
	x=0
	while x<350:
		center_point = circle1.getCenter()
		r=circle1.getRadius()
		x1= center_point.getX()
		y1= center_point.getY()
		new_center= Point(x1+50,y1)
		circle1.undraw()
		circle1= Circle(new_center, r)
		circle1.draw(win5)
		circle1.setFill("blue")
		x=x1+50
		sleep(1)



circle2 = RandomCircle100()
circle2.setFill("blue")
MoveRight(circle2)
	
win6=GraphWin("My Program 6", 500, 500)

def MoveLeft(circle1):
	circle1.draw(win6)
	sleep(1)	
	x=100
	while x>50:
		center_point = circle1.getCenter()
		r=circle1.getRadius()
		x1= center_point.getX()
		y1= center_point.getY()
		new_center= Point(x1-50,y1)
		circle1.undraw()
		circle1= Circle(new_center, r)
		circle1.draw(win6)
		circle1.setFill("blue")
		x=x1-50
		sleep(1)


circle3 = RandomCircle100()
circle3.setFill("blue")
MoveLeft(circle3)

win7=GraphWin("My Program 7", 500, 500)

def BackAndForth():
	circle1=RandomCircle100()
	circle1.setFill("blue")
	x=70
	while x>50:
		center_point = circle1.getCenter()
		r=circle1.getRadius()
		x1= center_point.getX()
		y1= center_point.getY()
		new_center= Point(x1-50,y1)
		circle1.undraw()
		circle1= Circle(new_center, r)
		circle1.draw(win7)
		circle1.setFill("blue")
		sleep(1)
		center_point = circle1.getCenter()
		r=circle1.getRadius()
		x1= center_point.getX()
		y1= center_point.getY()
		new_center= Point(x1+50,y1)
		circle1.undraw()
		circle1= Circle(new_center, r)
		circle1.draw(win7)
		circle1.setFill("blue")
		x=70
		sleep(1)

BackAndForth()
	


input("press a key to continue")
