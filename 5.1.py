import math

def chack_fermat ():
	
	a = int(input(" а = \n"))
	b = int(input("b =\n"))
	n = int(input("n =\n"))
	c = int(input("c = \n"))
	
	left_side = pow(a, n) + pow (b, n)
	right_side = pow(c, n)
    

	if (n > 2) and (left_side == right_side):
		print("Неможливо, Ферма помилився")
	else:
		print("Ні, це не підходить")

chack_fermat()