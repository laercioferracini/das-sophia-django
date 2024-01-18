from turtle import *

color('blue', 'orange')
co = float(200)
ca = float(200)

hipotenusa = (ca ** 2 + co ** 2) ** (1/2)

begin_fill()
while True:
    forward(200)
    left(90)
    if abs(pos()) < 1:
        right(90)
        forward(200)
        right(90)
        forward(200)
        right(90)
        forward(200)
        right(90)
        forward(200)
        left(135)
        forward(hipotenusa)
        left(135)
        forward(200)
        left(135)
        forward(hipotenusa)
        break

end_fill()
done()
