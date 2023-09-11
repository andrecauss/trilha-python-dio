carros = ["gol", "celta", "palio"]

# corre a lista normal trazendo cada elemento
for carro in carros:
    print(carro)

# corre a lista trazendo dois elementos, o índice e o elemento carro
for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")
