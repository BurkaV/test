#def do_twice(f):
#	f()
#	f()
#def print_spam():
#	print("spammm")
#do_twice(print_spam)


def do_twice(f):# ця функції мала бути буз прінта, але так вона не робила
    print (f)
    print (f)
do_twice("5")

def print_twice(g):
	print(g)
	print(g)
print_twice("spam")
#do_twice(print_spam) #нерозумію чому не включається
def print_twise(g):
	print_twice(g)
	print_twice(g)
print_twise ("cool")

def do_four(f):
    do_twice(f)
    do_twice(f)
do_four("56")
