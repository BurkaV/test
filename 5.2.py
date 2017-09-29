def is_triangle ():
	a = int(input("a = \n"))
	b = int(input("b = \n"))
	c = int(input("c = \n"))
	if a + b < c:
		print("not")
	elif a + c < b:
		print("not")
	elif b + c < a:
		print ("not")
	else:
		print("yes")
is_triangle() 