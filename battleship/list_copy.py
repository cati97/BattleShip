import copy

row0 = [1, 2, 3]
row1 = [4, 5, 6]
row2 = [7, 8, 9]

lista = [row0, row1, row2]

kopia = [row[:] for row in lista]  # deep copy!

print("Lista")
print(lista)
print("Kopia")
print(kopia)

kopia[0][0] = 56

print("Zmiana")
print("Lista")
print(lista)
print("Kopia")
print(kopia)
