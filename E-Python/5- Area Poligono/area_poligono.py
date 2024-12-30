# Crea una única función (importante que sólo sea una) que sea capaz
# de calcular y retornar el área de un polígono.
# - La función recibirá por parámetro sólo UN polígono a la vez.
# - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
# - Imprime el cálculo del área de un polígono de cada tipo.

def area_poligono(poligono: str):
    if poligono.lower() == 'triangulo':
        base = float(input('Ingrese la base del triángulo: '))
        altura = float(input('Ingrese la altura del triángulo: '))
        area = (base * altura) / 2
        print(f'El área del triángulo es: {area}')
    elif poligono.lower() == 'cuadrado':
        lado = float(input('Ingrese el lado del cuadrado: '))
        area = lado ** 2
        print(f'El área del cuadrado es: {area}')
    elif poligono.lower() == 'rectangulo':
        base = float(input('Ingrese la base del rectángulo: '))
        altura = float(input('Ingrese la altura del rectángulo: '))
        area = base * altura
        print(f'El área del rectángulo es: {area}')
    else:
        print('Polígono no soportado')

area_poligono('triangulo')