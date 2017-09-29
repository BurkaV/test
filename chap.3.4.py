#def do_twice(f):
	#f()
	#f()
def print_spam():
	print("spam")

def print_twice(g):
	print(g)
	print(g)
print_twice("spam")


def do_twice(f, r):# ця функції мала бути буз прінта, але так вона не робила
    f(r)
    f(r)
do_twice(print_twice, "spam")




 #нерозумію чому не включається




#def print_twise(g):
	#print_twice(g)
	#print_twice(g)
#print_twise ("cool")

def do_four(g,t):
    g(print,t)
    g(print,t)
do_four(do_twice, "hello")
