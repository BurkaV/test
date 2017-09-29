def print_twice(b):
	print(b)
	print(b)
print_twice("Hello")

def do_twice(a, w):
	a(w)
	a(w)
do_twice(print_twice, "spam")

def do_four(e, r):
	e(r)
	e(r)
do_four(print_twice, "four")