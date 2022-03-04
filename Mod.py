#Módulo Formas Turtle
import turtle
import math

"""
Este módulo es útil para crear formas usando el módulo de turtle
"""
__name__ = "Modulo Formas en Turtle"

#Función Cuadrado
def cuadrado(tortuga, color, dim):
    tortuga.begin_fill()
    for i in range(4):
        tortuga.forward(dim)
        tortuga.right(90)
    tortuga.color(color)
    tortuga.end_fill()

#Función Rectángulo
def rectangulo(tortuga, color, base, alt):
    tortuga.begin_fill()
    for i in range(2):
        tortuga.forward(base)
        tortuga.right(90)
        tortuga.forward(alt)
        tortuga.right(90)
    tortuga.color(color)
    tortuga.end_fill()

#Función Rombo donde "angle1" es el ángulo más estrecho
def rombo(tortuga, color, dim, angle1):
    angle2 = (360-2*(angle1))/2
    tortuga.begin_fill()
    tortuga.left(angle2/2)
    tortuga.forward(dim)
    tortuga.right(180-angle1)
    tortuga.forward(dim)
    tortuga.right(180-angle2)
    tortuga.forward(dim)
    tortuga.right(180-angle1)
    tortuga.forward(dim)

    tortuga.color(color)
    tortuga.end_fill()

#Función Hexágono
def hexagono(tortuga, color, dim):
    tortuga.begin_fill()
    for i in range(6):
        tortuga.forward(dim)
        tortuga.left(60)
    tortuga.color(color)
    tortuga.end_fill()

#Función Triángulo
def triangulo(tortuga, color, dim1, dim2, dim3):
    angl1, angl3 = degrees(dim1,dim2, dim3)
    
    tortuga.begin_fill()
    tortuga.forward(dim1)
    tortuga.left(180-angl3)
    tortuga.forward(dim2)
    tortuga.left(180-angl1)
    tortuga.forward(dim3)
    tortuga.color(color)
    tortuga.end_fill()

"""
Se utilizó al función de ángulos para otras formas en caso de ser necesitadas,
en base a ley de cosenos.
"""
#Función para cálculo de angulos (cosenos)
def degrees(A,B,C):
    D1 = math.degrees(math.acos((A**2-B**2-C**2)/(-2*B*C)))
    D2 = math.degrees(math.acos((B**2-A**2-C**2)/(-2*A*C)))
    D3 = 180-D1-D2
    return D1, D3

#Función paralelogramo
def paralelogramo(tortuga, color, dim1, dim2, angl1):
    tortuga.begin_fill()
    angl2 = (360-2*(angl1))/2

    tortuga.forward(dim1)
    tortuga.left(180-angl2)
    tortuga.forward(dim2)
    tortuga.left(180-angl1)
    tortuga.forward(dim1)
    tortuga.left(180-angl2)
    tortuga.forward(dim2)
    tortuga.color(color)
    tortuga.end_fill()

""" Este trapecio es de únicamente 3 lados iguales y la base"""
#Función trapecio 
def trapecio(tortuga, color, b, dim1):
    tortuga.begin_fill()
    i = (b-dim1)/2
    angle1 = angSeno(i, dim1)+90
    angle2 = (360 -2*angle1)/2

    tortuga.forward(b)
    tortuga.left(180-angle2)
    tortuga.forward(dim1)
    tortuga.left(180-angle1)
    tortuga.forward(dim1)
    tortuga.left(180- angle1)
    tortuga.forward(dim1)
    tortuga.color(color)
    tortuga.end_fill()

"""
Función  para calcular angulos con base a la ley de senos
"""
#Función cálculo de senos
def angSeno(A, B):
    angle = math.degrees(math.asin(A/B))
    return angle

#Función circulo
def circulo(tortuga, color, radio):
    tortuga.begin_fill()
    tortuga.circle(radio)
    tortuga.color(color)
    tortuga.end_fill()
