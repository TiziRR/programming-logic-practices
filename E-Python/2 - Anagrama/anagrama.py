# /*
#  * Escribe una función que reciba dos palabras (String) y retorne
#  * verdadero o falso (Bool) según sean o no anagramas.
#  * - Un Anagrama consiste en formar una palabra reordenando TODAS
#  *   las letras de otra palabra inicial.
#  * - NO hace falta comprobar que ambas palabras existan.
#  * - Dos palabras exactamente iguales no son anagrama.
#  */

def is_anagrama(first_word: str, second_word: str):
    """
    This function return True if the words are anagrams and False if not.
    """
    if list(first_word).sort() == list(second_word).sort():
        return True
    return False

print(is_anagrama('roma', 'amor'))