# /*
#  * Escribe un programa que se encargue de comprobar si un número es o no primo.
#  * Hecho esto, imprime los números primos entre 1 y 100.
#  */

def isprimo(num) -> bool:
    for n in range(2,num):
        if num % n == 0:   
            return False
        return True

for h in range(1,10):
    print(f"{h} es primo: {isprimo(h)}")
