count = 0


def show_count():
    print(count)


def set_count(c):
    count = c

# this show count returns 0
show_count()

# we expect this to set count to 5
set_count(5)

# however, this still returns 0.  
# this is due to python seeing a locally scopped "count" and using that, rather than using the "global" version
show_count()