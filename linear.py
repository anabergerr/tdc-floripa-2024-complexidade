def substituir_numeros(lista: list[int]):
    ultima_posicao = len(lista) - 1
    maior_a_direita = lista[ultima_posicao]

    for i in range(ultima_posicao, -1, -1):
        if maior_a_direita > lista[i]:
            lista[i] = maior_a_direita
        else:
            maior_a_direita = lista[i]

# Exemplo de uso
lista = [2, 1, 2, 3, 0, 5, 1, 2, 3]
substituir_numeros(lista)
print(lista)  # Saída esperada: [5, 5, 5, 5, 5, 3, 3, 3, 3]
