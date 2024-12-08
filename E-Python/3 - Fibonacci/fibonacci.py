# /*
#  * Escribe un programa que imprima los 50 primeros números de la sucesión
#  * de Fibonacci empezando en 0.
#  * - La serie Fibonacci se compone por una sucesión de números en
#  *   la que el siguiente siempre es la suma de los dos anteriores.
#  *   0, 1, 1, 2, 3, 5, 8, 13...
#  */

def fibonacci():
    """
        Return the Fibonacci count
    """
    num = 1
    anterior = 0
    aux = num
    for n in range(50):
        if n == 0:
            print(0)
        print(aux)
        aux = anterior + num
        anterior = num
        num = aux

fibonacci()