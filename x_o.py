tabla = [
    ['X', 'O', None],
    [None, 'X', 'O'],
    ['O', None, 'X']
]
# for i in range(0, len(tabla)):
#     for j in range(0, len(tabla[i])):
#         print(tabla[i][j], end = " ")
#     print("\n")

# _ karakterre való csere none ról
for i in range(0, len(tabla)):
    for j in range(len(tabla[i])):
        if tabla[i][j] == None:
            tabla[i][j] = "_"
# jobb felső cseréje:
tabla[0][2] = "O"



# maga a print metódus
for i in range(0, len(tabla)):
    for j in range(0, len(tabla[i])):
        print(tabla[i][j], end = " ")
    print()
