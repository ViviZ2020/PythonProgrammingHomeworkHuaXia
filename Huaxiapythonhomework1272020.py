import turtle
sc = turtle.Screen()
sc.bgcolor('LightBlue')

x = turtle.Turtle()
x.speed(50)


for i in range (26):
    x.circle(100)
    x.right(10)

print(i)

for y in range (6):
    x.forward(100)
    x.left(60)

print(y)
