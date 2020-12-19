import turtle # nested loops

x=turtle.Turtle()
x.shape('turtle')
x.color('lightBlue')
x.shapesize(1,0.5)

for i in range(36): 
    for j in range(3):
        x.forward(50)
        x.left(120)
        x.right(10) 

