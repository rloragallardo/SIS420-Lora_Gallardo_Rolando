#  DATASET x = tamaño del terreno en metros cuadrados (m2) y = precio del terreno en miles de dólares (mil)

dataset = [
    (50, 68),
    (60, 71),
    (70, 76),
    (80, 78),
    (90, 84),
    (100, 86),
    (110, 91),
    (120, 94),
    (130, 97),
    (140, 101),
    (150, 104),
    (160, 108),
    (170, 111),
    (180, 114),
    (190, 119),
    (200, 121),
    (210, 126),
    (220, 128),
    (230, 133),
    (240, 135),
    (250, 139),
    (260, 143),
    (270, 145),
    (280, 150),
    (290, 153),
    (300, 156),
    (310, 160),
    (320, 163),
    (330, 167),
    (340, 170),
    (350, 174),
    (360, 177),
    (370, 181),
    (380, 184),
    (390, 188),
    (400, 191),
    (410, 195),
    (420, 198),
    (430, 202),
    (440, 205),
    (450, 209),
    (460, 212),
    (470, 216),
    (480, 219),
    (490, 223),
    (500, 226),
    (510, 230),
    (520, 233),
    (530, 237),
    (540, 240)
]

# Formula de la recta: y = mx + b


mejor_b = 0
mejor_m = 0
menor_error = float("inf")





for b in range(0, 101):

    for m_entero in range(0, 101):

        m = m_entero / 10

        error_total = 0


        for x, y in dataset:

            
            y_predicho = m * x + b

            
            error = y - y_predicho

            
            error_cuadratico = error * error

            
            error_total = error_total + error_cuadratico


        if error_total < menor_error:

            menor_error = error_total
            mejor_b = b
            mejor_m = m





print("RESULTADOS")


print("Mejor valor de b:", mejor_b)
print("Mejor valor de m:", mejor_m)
print("Error total:", menor_error)

print()
print("Ecuacion de la recta:")
print("y =", mejor_m, "* x", "+", mejor_b)



#INFERENCIAS

nuevos_x = [
    550,
    560,
    570,
    580,
    590,
    600,
    610,
    620,
    630,
    640
]

print()
print("INFERENCIAS")

for x in nuevos_x:

    y_inferido = mejor_m * x + mejor_b

    print("Terreno:",x,"m_cuadrados -> Precio estimado:",y_inferido,"mil dolares")