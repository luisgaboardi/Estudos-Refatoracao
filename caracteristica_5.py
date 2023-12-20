# BOA DOCUMENTAÇÃO

# Código original
# Função para ordenar uma lista de números usando o algoritmo
# de ordenação bolha.
def ordenar_lista_original(lista):
    # Implementação do algoritmo de ordenação bolha.
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista

# Código Após a Refatoração:
def ordenar_lista_refatorada(lista):
    """
    Ordena uma lista de números em ordem crescente.

    Parâmetros:
    - lista: A lista a ser ordenada.

    Retorno:
    A lista ordenada.
    """
    # Implementação do algoritmo de ordenação bolha.
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista

# Dados de entrada
lista_numeros = [64, 25, 12, 22, 11]

# Execução e impressão dos resultados
print("Resultado do Código Original:")
lista_original = ordenar_lista_original(lista_numeros.copy())
print(f"Lista Ordenada Original: {lista_original}")

print("\nResultado do Código Refatorado:")
lista_refatorada = ordenar_lista_refatorada(lista_numeros.copy())
print(f"Lista Ordenada Refatorada: {lista_refatorada}")
