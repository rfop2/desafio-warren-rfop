k = 2
tempoChegada = [0, -1, 2, 1]
for x in tempoChegada:
    if x <= 0:
        k -= 1
if k <= 0:
    print("Aula normal")
else:
    print("Aula Cancelada")