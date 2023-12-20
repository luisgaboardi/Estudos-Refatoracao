# MODULARIDADE (Baixo Acoplamento e Alta Coesão)

# Código original
class SistemaFinanceiroOriginal:
    def calcular_imposto(self, salario, descontos, beneficios):
        imposto = salario * 0.2 - descontos + beneficios
        print(f'Calculando o imposto no Sistema Financeiro Original: {imposto}')

    def gerar_relatorio(self, dados):
        print('Gerando o relatório no Sistema Financeiro Original')
        for chave, valor in dados.items():
            print(f"{chave}: {valor}")

# Código Após a Refatoração:
class CalculadoraImpostoRefatorada:
    def calcular_imposto(self, salario, descontos, beneficios):
        imposto = salario * 0.2 - descontos + beneficios
        print(f'Calculando o imposto na Calculadora de Imposto Refatorada: {imposto}')

class GeradorRelatorioRefatorado:
    def gerar_relatorio(self, dados):
        print('Gerando o relatório no Gerador de Relatório Refatorado')
        for chave, valor in dados.items():
            print(f"{chave}: {valor}")

# Dados de entrada
dados = {'info': 'alguma informação', 'resultado': 'algum resultado'}

# Execução e impressão dos resultados
print("Resultado do Código Original:")
sistema_original = SistemaFinanceiroOriginal()
sistema_original.calcular_imposto(50000, 2000, 1000)
sistema_original.gerar_relatorio(dados)

print("\nResultado do Código Refatorado:")
calculadora_refatorada = CalculadoraImpostoRefatorada()
calculadora_refatorada.calcular_imposto(50000, 2000, 1000)

gerador_refatorado = GeradorRelatorioRefatorado()
gerador_refatorado.gerar_relatorio(dados)