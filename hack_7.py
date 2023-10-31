"""
loop: while [] output => [5,4,3,2,1,0]
"""

def fn_hack_7():
    result = []
    contador = 6
    while contador != 0:
        contador-=1
        result.append(contador)
    return result  