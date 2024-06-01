def substituir_numeros(lista: list[int]):  # O(n^2)
    for i in range(len(lista)):  # O(n)
        elemento_original = lista[i]
        maior_a_direita = elemento_original
        for j in range(len(lista)):  # O(n)
            novo_elemento = lista[j]
            if j > i and novo_elemento > maior_a_direita:
                maior_a_direita = novo_elemento
        lista[i] = maior_a_direita

# Exemplo de uso
lista = [2, 1, 2, 3, 0, 5, 1, 2, 3]
substituir_numeros(lista)
print(lista)  # Saída esperada: [5, 5, 5, 5, 5, 5, 3, 3, 3]
