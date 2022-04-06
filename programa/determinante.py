def matriz_2x2(matriz):
    termo1 = matriz[0][0] * matriz[1][1]
    termo2 = matriz[0][1] * matriz[1][0]
    determinante = termo1 - termo2
    return determinante

def matriz_3x3(matriz):
    sub1 = [
            [matriz[1][1], matriz[1][2]],
            [matriz[2][1], matriz[2][2]]
            ]
    sub2 = [
            [matriz[1][0], matriz[1][2]],
            [matriz[2][0], matriz[2][2]]
            ]
    sub3 = [
            [matriz[1][0], matriz[1][1]],
            [matriz[2][0], matriz[2][1]]
            ]
    a, b, c = matriz[0][0], matriz[0][1], matriz[0][2]
    determinante = a * matriz_2x2(sub1) - b * matriz_2x2(sub2) + c * matriz_2x2(sub3)
    return determinante
