# def greet(name,time):
#     print(f"good {time} {name}, hope you are well")
# name = input('enter your name:')
# time = input('enter the time of day:')
# greet(name,time)
# to calculate the area of a circle
def area(radius):
    return 3.142*radius**2
def volume(area,length):
    print(area*length)
radius = int(input('enter the radius'))
length = int(input('enter a length'))

volume(area(radius),length)
 
