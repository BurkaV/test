def print_twice(b):
	print(b)
	print(b)
print_twice("Hello")

def do_twice(a, w):
	a(w)
	a(w)
do_twice(print_twice, "spam")

def do_four(e, r):
	e(print, r)
	e(print, r)
do_four(do_twice, "four") #"seven", "three")