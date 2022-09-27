import sys
<<<<<< HEAD
======= 
>>>>>>> jupiter

def hello():
	if sys.argv[1] == "Mars":
		hellomars()
	elif sys.argv[1] == "Jupiter":
		hellojupiter()
	else:
		helloworld()

def hellomars():
	print("Hello world")

def helloworld():
	print("Hello world")

def hellojupiter():
	print("Hello jupiter")

