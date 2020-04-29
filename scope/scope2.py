count = 0


def show_count():
    print(count)


def set_count(c):
    global count
    count = c

# this show count returns 0
show_count()

# we expect this to set count to 5
set_count(5)

# now this works as expected, by using the global keyword, we tell python to use the globally scopped "count"
show_count()