# AUSÊNCIA DE DUPLICIDADES

# Código original
def calcular_area_retangulo_original(base, altura):
    area = base * altura
    return area

def calcular_volume_cubo_original(lado):
    volume = lado ** 3
    return volume

# Código Após a Refatoração:
def calcular_area_retangulo_refatorado(base, altura):
    return base * altura

def calcular_volume_cubo_refatorado(lado):
    return lado ** 3

# Dados de entrada
base_retangulo = 5
altura_retangulo = 10
lado_cubo = 3

# Execução e impressão dos resultados
print("Resultado do Código Original:")
area_retangulo_original = calcular_area_retangulo_original(base_retangulo, altura_retangulo)
volume_cubo_original = calcular_volume_cubo_original(lado_cubo)
print(f"Área do Retângulo Original: {area_retangulo_original}")
print(f"Volume do Cubo Original: {volume_cubo_original}")

print("\nResultado do Código Refatorado:")
area_retangulo_refatorado = calcular_area_retangulo_refatorado(base_retangulo, altura_retangulo)
volume_cubo_refatorado = calcular_volume_cubo_refatorado(lado_cubo)
print(f"Área do Retângulo Refatorado: {area_retangulo_refatorado}")
print(f"Volume do Cubo Refatorado: {volume_cubo_refatorado}")
