import math

def add(a1: int, a2: int):
    return a1 + a2

def sub(a1: int, a2: int):
    return a1 - a2

def mul(a1: int, a2: int):
    return a1 * a2

def div(a1: int, a2: int):
    if (a2 != 0):
        return a1/a2
    else:
        print("Error")