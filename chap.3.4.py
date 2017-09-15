def do_twice(f):
    f()
    f()
do_twice(45)

def do_four(f):
    do_twice(f)
    do_twice(f)
do_four(56)
