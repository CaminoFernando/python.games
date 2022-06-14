import turtle
import time
import random

# Creamos la ventana del juego
ventana = turtle.Screen()
ventana.title('Juego de la serpiente')
ventana.bgcolor("black")
ventana.setup(width = 620, height = 700) # ancho , alto
ventana.tracer(0)

# Velocidad inicial
velocidad = 0.1

# Marcador
score = 0
high_score = 0

# Nivel de juego
nivel = 1

# Texto
textoPuntuacion = turtle.Turtle()
textoPuntuacion.speed(0)
textoPuntuacion.color("white")
textoPuntuacion.penup()
textoPuntuacion.hideturtle()
textoPuntuacion.goto(-270,260)
textoPuntuacion.write("Puntuación: {}".format(score), font=("Arial", 16, "normal"))

textoPuntuacionMax = turtle.Turtle()
textoPuntuacionMax.speed(0)
textoPuntuacionMax.color("white")
textoPuntuacionMax.penup()
textoPuntuacionMax.hideturtle()
textoPuntuacionMax.goto(50,260)
textoPuntuacionMax.write("Puntuación máxima: {}".format(high_score), font=("Arial", 16, "normal"))

textoNivel = turtle.Turtle()
textoNivel.speed(0)
textoNivel.color("yellow")
textoNivel.penup()
textoNivel.hideturtle()
textoNivel.goto(0,300)
textoNivel.write("NIVEL {}".format(nivel), align = "center", font=("Arial", 22, "normal"))

# Funciones
def crearElemento(forma, color):
    elemento = turtle.Turtle()
    elemento.speed(0)
    elemento.shape(forma)
    elemento.color(color)
    elemento.penup() # no deja rastro
    # elemento.goto(0,0)
    elemento.direccion = "quieto"
    return elemento

def movimiento():
    if cabeza.direccion == "arriba":
        y = cabeza.ycor()
        cabeza.sety(y + 20)

    if cabeza.direccion == "abajo":
        y = cabeza.ycor()
        cabeza.sety(y - 20)

    if cabeza.direccion == "izquierda":
        x = cabeza.xcor()
        cabeza.setx(x - 20)

    if cabeza.direccion == "derecha":
        x = cabeza.xcor()
        cabeza.setx(x + 20)

def arriba():
    if cabeza.direccion != "abajo":
        cabeza.direccion = "arriba"
def abajo():
    if cabeza.direccion != "arriba":
        cabeza.direccion = "abajo"
def izquierda():
    if cabeza.direccion != "derecha":
        cabeza.direccion = "izquierda"
def derecha():
    if cabeza.direccion != "izquierda":
        cabeza.direccion = "derecha"

def mostrarScore(score, high_score):
    textoPuntuacion.clear()
    textoPuntuacionMax.clear()
    textoPuntuacion.write("Puntuación: {}".format(score), font=("Arial", 16, "normal"))
    textoPuntuacionMax.write("Puntuación máxima: {}".format(high_score), font=("Arial", 16, "normal"))

def mostrarNivel(nivel):
    textoNivel.clear()
    textoNivel.write("NIVEL {}".format(nivel), align = "center", font=("Arial", 22, "normal"))

def reiniciarPartida(cabeza, cuerpo, score, high_score, nivel):
    time.sleep(1)
    cabeza.goto(0,0)
    cabeza.direccion = "quieto"
    nivel = 1    
    
    # Reiniciar cuerpo
    [a.hideturtle() for a in cuerpo]
    cuerpo.clear()

    # Reiniciar score y nivel
    mostrarScore(score, high_score)
    mostrarNivel(nivel)

def subirNivel(nivel):
    time.sleep(1)
    cabeza.goto(0,0)
    cabeza.direccion = "quieto"

    # Reiniciar cuerpo
    [a.hideturtle() for a in cuerpo]
    cuerpo.clear()
    
    nivel = nivel +1
    mostrarNivel(nivel)

def aumentarVelocidad(velocidadActual):
    nuevaVelocidad = velocidadActual / 2
    return nuevaVelocidad

def crearCuadrilatero(forma, color):
    borde = turtle.Turtle()
    borde.shape(forma)
    borde.color(color)
    borde.penup()
    borde.goto(-280,240)
    borde.pendown()
    borde.pensize(20)
    for i in range(4):
        borde.forward(560)
        borde.right(90)
    borde.hideturtle()

def ubicarComida(elemento):
    x = random.randint(-13,13)
    y = random.randint(-15,11)
    elemento.goto(x*20,y*20)

# Teclado
ventana.listen()
ventana.onkeypress(arriba, "Up")
ventana.onkeypress(abajo, "Down")
ventana.onkeypress(izquierda, "Left")
ventana.onkeypress(derecha, "Right")

# Cabeza serpiente
cabeza = crearElemento("square", "dark green")

# Comida
comida = crearElemento("circle", "red")
ubicarComida(comida)

# Cuerpo de la serpiente
cuerpo = []