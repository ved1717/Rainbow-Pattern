import os, sys, time
x=1
def move():
    global x
    x = x + 1
def refresh():
    os.system('clear')
    #print x
    for i in range(0, x):
        sys.stdout.write(' ')
    sys.stdout.write('X')
    sys.stdout.flush()

while 1:
    refresh()
    time.sleep(1)
    move()