# BOAS INTERFACES

# Código original
class ProcessadorDadosOriginal:
    def realizar_operacao1(self, dados):
        print('Realizando Operação 1 no Processador de Dados Original')

    def executar_tarefa(self, parametros):
        print('Executando Tarefa no Processador de Dados Original')

# Código Após a Refatoração:
class Operacao1Refatorada:
    def executar(self, dados):
        print('Realizando Operação 1 na Operação 1 Refatorada')

class TarefaRefatorada:
    def executar(self, parametros):
        print('Executando Tarefa na Tarefa Refatorada')

# Dados de entrada
dados = {'info': 'alguma informação'}
parametros = {'param': 'algum parâmetro'}

# Execução e impressão dos resultados
print("Resultado do Código Original:")
processador_original = ProcessadorDadosOriginal()
processador_original.realizar_operacao1(dados)
processador_original.executar_tarefa(parametros)

print("\nResultado do Código Refatorado:")
operacao_refatorada = Operacao1Refatorada()
operacao_refatorada.executar(dados)

tarefa_refatorada = TarefaRefatorada()
tarefa_refatorada.executar(parametros)
