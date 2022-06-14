import diseño
import time

while True:
    diseño.ventana.update()

    diseño.crearCuadrilatero("square", "grey")

    # Mover cuerpo serpiente
    totalCuerpo = len(diseño.cuerpo)
    for index in range(totalCuerpo -1, 0, -1):
        x = diseño.cuerpo[index-1].xcor()
        y = diseño.cuerpo[index-1].ycor()
        diseño.cuerpo[index].goto(x,y)
    
    if totalCuerpo > 0:
        x = diseño.cabeza.xcor()
        y = diseño.cabeza.ycor()
        diseño.cuerpo[0].goto(x,y)

    # Colisiones comida
    if diseño.cabeza.distance(diseño.comida) < 20:
        diseño.ubicarComida(diseño.comida)

        # Agregar cuerpo
        nuevo_cuerpo = diseño.crearElemento("square", "green")
        diseño.cuerpo.append(nuevo_cuerpo)

        # Aumentar puntuación
        diseño.score += 10

        # Actualizar puntuación máxima
        if diseño.score > diseño.high_score:
            diseño.high_score = diseño.score

        diseño.mostrarScore(diseño.score, diseño.high_score)

        # Aumentar velocidad
        if diseño.score == 30:
            diseño.velocidad = diseño.aumentarVelocidad(diseño.velocidad)
        if diseño.score == 50:
            diseño.subirNivel(diseño.nivel)
        if diseño.score == 80:
            diseño.velocidad = diseño.aumentarVelocidad(diseño.velocidad)

    diseño.movimiento()

    # Colisiones bordes
    if diseño.cabeza.xcor() > 260 or diseño.cabeza.xcor() < -260 or diseño.cabeza.ycor() > 220 or diseño.cabeza.ycor() < -300:
        diseño.score = 0
        diseño.reiniciarPartida(diseño.cabeza, diseño.cuerpo, diseño.score, diseño.high_score, diseño.nivel)
        diseño.velocidad = 0.1
        
    # Colisiones con propio cuerpo
    for unidad in diseño.cuerpo:
        if unidad.distance(diseño.cabeza) < 15:
            diseño.score = 0
            diseño.reiniciarPartida(diseño.cabeza, diseño.cuerpo, diseño.score, diseño.high_score, diseño.nivel)
            diseño.velocidad = 0.1

    time.sleep(diseño.velocidad)