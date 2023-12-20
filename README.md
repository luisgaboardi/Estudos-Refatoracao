# Trabalho Prático 2 - TPPE

UnB/FGA - 2023.2

Luís Guilherme Gaboardi Lins - 180022962

## Descrição
As características de um bom projeto de software apresentadas estão, de certo modo, associadas aos maus-cheiros de código apresentados por Martin Fowler em seu catálogo de refatorações e relacionados às operações que tratam tais maus-cheiros. De acordo com a definição do próprio Martin Fowler, refatoração é uma maneira de aperfeiçoar o projeto de código existente sem alterar o seu comportamento externamente observável.

Para esse trabalho o grupo deverá escolher 5 características dentre as 9 características de um bom projeto de software apresentadas acima e, para cada uma delas, apresentar:

- Uma descrição da característica, mostrando claramente quais são os seus efeitos no código (em termo de estrutura, claridade, coesão, acoplamento dentre outros efeitos aplicáveis);
- Uma relação da característica com os maus-cheiros de código definidos por Fowler. Uma descrição dos maus cheiros está disponível nos slides sobre o conteúdo de refatoração;
- Pelo menos uma operação de refatoração capaz de levar o projeto de código a ter a característica em análise.

## Documentação

### 1. Simplicidade:

#### Descrição:
A simplicidade no código se refere à ideia de manter as soluções o mais simples possível, evitando complexidade desnecessária. Código simples é mais fácil de entender, manter e menos propenso a erros.

#### Efeitos no Código:

- Estrutura mais clara e direta.
- Facilita a compreensão e manutenção.
- Reduz a probabilidade de bugs.
- Melhora a legibilidade do código.

#### Relação com Maus-Cheiros de Código:

- Complexidade Excessiva: Códigos complexos frequentemente carecem de simplicidade.
- Métodos Longos: Funções extensas muitas vezes indicam falta de simplicidade.
- Lógica Aninhada Profundamente: A simplicidade é comprometida quando há muitos níveis de aninhamento.

#### Operação de Refatoração:

- Simplificar Expressões Condicionais: Refatoração para simplificar e tornar mais legíveis as expressões condicionais complexas.

### 2. Moduaridade (Baixo Acoplamento e Alta Coesão):

#### Descrição:
Modularidade refere-se à divisão do sistema em módulos independentes que realizam tarefas específicas. Baixo acoplamento significa que os módulos são independentes, e alta coesão significa que os elementos dentro do módulo estão fortemente relacionados.

#### Efeitos no Código:

- Facilita a manutenção e evolução do sistema.
- Permite a reutilização de módulos.
- Melhora a legibilidade e compreensão do código.

#### Relação com Maus-Cheiros de Código:

- Acoplamento Forte: Indica falta de modularidade.
- Classes God: Classes que fazem tudo podem indicar baixa coesão.
- Métodos com muitos parâmetros: Podem indicar falta de coesão.

#### Operação de Refatoração:
- Extrair Método: Separação de funcionalidades específicas em métodos distintos, promovendo a coesão e reduzindo o acoplamento.

### 3. Boas Interfaces:

#### Descrição:
Boas interfaces referem-se à exposição clara e consistente dos métodos e propriedades de uma classe, facilitando o uso por outros módulos ou classes.

#### Efeitos no Código:

- Melhora a comunicação entre módulos.
- Facilita a integração de novos componentes.
- Reduz a probabilidade de erros de uso.

#### Relação com Maus-Cheiros de Código:

- Métodos com muitos parâmetros: Uma interface bem definida pode evitar a necessidade de muitos parâmetros.
- Métodos longos: Interfaces claras muitas vezes implicam em métodos mais curtos e especializados.

#### Operação de Refatoração:
- Extrair Interface: Criação de interfaces claras e específicas para melhorar a comunicação entre diferentes partes do sistema.

### 4. Ausência de Duplicidades:

#### Descrição:
A ausência de duplicidades refere-se à eliminação de código redundante e repetitivo, promovendo a reutilização e facilitando a manutenção.

#### Efeitos no Código:

- Reduz a probabilidade de inconsistências.
- Facilita a atualização e manutenção.
- Melhora a legibilidade.

#### Relação com Maus-Cheiros de Código:

- Duplicação de Código: Indica a presença de duplicidades.
- Métodos Longos: Podem incluir trechos de código duplicados.

#### Operação de Refatoração:
- Extrair Método ou Classe: Identificação e isolamento de código duplicado em métodos ou classes separadas.

### 5. Boa Documentação:

#### Descrição:
A boa documentação envolve fornecer informações claras e úteis sobre o código, explicando seu propósito, funcionamento e como utilizá-lo.

#### Efeitos no Código:

- Facilita a compreensão do código.
- Acelera a integração de novos desenvolvedores.
- Reduz a probabilidade de erros de uso.

#### Relação com Maus-Cheiros de Código:

- Código Comentado em Excesso: Indica possível falta de clareza no código.
- Nomes de Variáveis e Métodos Não Explicativos: Pode indicar necessidade de documentação adicional.

#### Operação de Refatoração:
- Extrair Comentário: Transforma comentários em documentação formal e clara, quando necessário.

## Prática

### Pré-requisitos

- Python versão 3.x

### Execução

```
python caracteristica_[numero].py
```

Sendo o [número] a identificação da característica, de 1 a 5. 
