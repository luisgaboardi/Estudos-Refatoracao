# SIMPLICIDADE

# Código original
def calcular_media_original(lista_notas):
    soma = 0
    for nota in lista_notas:
        soma += nota
    media = soma / len(lista_notas)
    return media

# Código Após a Refatoração:
def calcular_media_refatorada(lista_notas):
    return sum(lista_notas) / len(lista_notas)

# Dados de entrada
notas = [8, 7, 9, 10, 8.5]

# Execução e impressão dos resultados
print("Resultado do Código Original:")
media_original = calcular_media_original(notas)
print(f"Média Original: {media_original}")

print("\nResultado do Código Refatorado:")
media_refatorada = calcular_media_refatorada(notas)
print(f"Média Refatorada: {media_refatorada}")