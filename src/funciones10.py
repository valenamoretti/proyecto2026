def procesar_ronda(ronda, tabla_final):
    esta_ronda = {}
    scores = ronda['scores']


    for cocinero, puntajes in scores.items():
        total = sum(puntajes.values())
        esta_ronda[cocinero] = total


        if cocinero not in tabla_final:
            tabla_final[cocinero] = {
                'total': 0,
                'rondas_ganadas': 0,
                'mejor_ronda': 0,
                'rounds': 0
            }


        tabla_final[cocinero]['total'] += total
        tabla_final[cocinero]['rounds'] += 1


        if total > tabla_final[cocinero]['mejor_ronda']:
            tabla_final[cocinero]['mejor_ronda'] = total


    return esta_ronda




def obtener_ganador(esta_ronda):
    max_puntaje = -1


    for nombre, puntaje in esta_ronda.items():
        if puntaje > max_puntaje:
            max_puntaje = puntaje
            ganador = nombre


    return ganador






def imprimir_tabla(posiciones):
    for nombre, data in posiciones:
        print(f"    {nombre}: {data['total']} pts")