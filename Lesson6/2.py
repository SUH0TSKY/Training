"""Код Морзе для представления цифр и букв использует тире и точки. Напишите
функцию для кодирования текстового сообщения в соответствии с кодом Морзе.
(словари в помощь)"""
def foo(morze, text):
    result = ""

    text = text.upper()

    for symbol in text:
        result += morze[symbol]

    print(result)


morze = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    " ": "      ",
}


foo(morze, "Hello world")