with open('data/calificaciones.txt', 'r') as f_in:
    with open('data/promedios.txt', 'w') as f_out:
        for linea in f_in:
            palabras = linea.strip().split()
            nombre = palabras[0]
            apellido = palabras[1]
            calificaciones = [int(calificacion) for calificacion in palabras[2:]]
            promedio = sum(calificaciones) / len(calificaciones)
            resultado = f'{apellido.upper()}, {nombre}: {promedio:.1f}\n'
            f_out.write(resultado)

