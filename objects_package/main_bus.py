from Bus import *
num=int(input("enter num of seats: "))
bus=Bus(num)
while num!=0:
    num=int(input("enter 1 to add name 2 to remove 0 to stop: "))
    if num==1:
        name=input("enter a name to add:")
        bus.geton(name)
    elif num==2:
        name = input("enter a name to remove:")
        bus.getoff(name)
print(bus)
