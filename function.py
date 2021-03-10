import math

# change the function here.
# fn is the function that we are optimizing.


def fn(items) -> int:
    '''
    items is a list of integers which define the coordinates
    returns an integer value.
    '''
    x = items[0]
    y = items[1]

    return ((x*x+y*y)**(0.25))*math.sin(30*((y*y+(x+0.5)**2)**0.1)*(math.pi/180))+abs(x)+abs(y)

# -((x-4)**3)*(-1+math.e**(-x))+y**2
