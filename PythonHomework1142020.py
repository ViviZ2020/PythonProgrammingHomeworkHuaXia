Height = input('Height of area:')
Width = input('Width of area:')
Length = input('Length of area:')
Windows =('Windows in area:')
Doors = input('Doors in area:')
Height = int(Height)
Width = int(Width)
Length = int(Length)
Windows = int(Windows)
Doors = int(Doors)
WallArea = 2 * Length * Height + 2 * Width * Height
NoPaintArea = Doors + Windows
PaintArea = WallArea - NoPaintArea
print('Total surface area:')
print(PaintArea)
print('Gallons of paint needed:')
Gallons = WallArea/350
print(Gallons)
