# banco-de-dados-ii

# Equipe:
- Breno Pedrosa
- Gustavo Lima
- Luis Gustavo
- Renata Bezerra
# Sistema de Banco de Dados para Restaurante

## Linguagem
- O projeto deve ser desenvolvido utilizando uma linguagem de programação à escolha do grupo e SQL.
- **Atenção**: O não cumprimento deste critério implicará em nota zero para o projeto, independentemente da etapa.

## Implementação
- Todos os requisitos descritos a seguir devem ser implementados com queries SQL e enviadas ao banco de dados utilizando a função da biblioteca escolhida.

## Contexto
Este projeto é um sistema de banco de dados para um restaurante. Ele deve ser criado de acordo com o seguinte modelo:

## Requisitos do Sistema

### Funcionalidades
- O sistema deve ter uma opção para **criar** e **destruir** completamente o banco de dados.
- O sistema deve iniciar com **10 registros pré-cadastrados** em cada tabela.
- Deve permitir o **cadastro** de novos itens em todas as tabelas.

### Triggers
Implemente os seguintes **triggers**:
1. O cliente ganha 1 ponto para cada 10 reais gastos. Implemente um trigger que automatize este cálculo.
2. Quando um ingrediente tiver sua data de validade expirada, o prato que utiliza esse ingrediente deve ser marcado como indisponível.
3. Se o cliente tentar comprar um prato que está indisponível, a compra não deve ser realizada.
4. Em uma venda, sempre que um produto for vendido, a quantidade disponível no banco de dados deve ser reduzida em 1.

### Usuários
O sistema deve ter três tipos de **usuários**, com permissões específicas:
- **Administrador**: Possui todas as permissões.
- **Gerente**: Pode realizar buscas, apagar registros e editar os registros já existentes.
- **Funcionário**: Pode adicionar novos registros e consultar os registros de vendas.

### Views
Implemente **3 views** usando `JOINs` e `GROUP BY`. As definições dessas views ficam a cargo do grupo.

### Procedimentos
Implemente os seguintes **procedimentos**:
1. **Reajuste**: Receba um percentual e aumente o valor de todos os pratos em proporção a este reajuste.
2. **Sorteio**: Selecione aleatoriamente um cliente para receber uma premiação de 100 pontos.
3. **Estatísticas**: Exiba as seguintes estatísticas a partir da tabela de vendas:
   - Produto mais vendido
   - Vendedor associado ao produto mais vendido
   - Produto menos vendido
   - Valor gerado pelo produto mais vendido
   - Mês de maior e menor venda do produto mais vendido
   - Valor gerado pelo produto menos vendido
   - Mês de maior e menor venda do produto menos vendido
4. **Gastar Pontos**: Permita que o cliente use seus pontos para comprar um prato. A proporção será de 1 ponto para cada 1 real. Caso o valor do prato contenha centavos, use 1 ponto extra para cobrir. Se a quantidade de pontos for maior que o valor do prato, o saldo restante de pontos deve ser mantido.

### Funções
Implemente a seguinte **função**:
- **Cálculo**: Receba um valor de compra e retorne a quantidade de pontos referentes à compra. Para cada 10 reais gastos, o cliente ganha 1 ponto. Valores que não completam 10 reais não geram pontos.

## Estrutura do Banco de Dados

### Tabelas
- **Cliente**: `cliente(id, nome, sexo, idade, nascimento, pontos)`
- **Prato**: `prato(id, nome, descricao, valor, disponibilidade)`
- **Fornecedor**: `fornecedor(id, nome, estado_origem)`
- **Ingrediente**: `ingredientes(id, nome, data_fabricacao, data_validade, quantidade, observacao)`
- **Usos**: `usos(id_prato(FK), id_ingrediente(FK))`
- **Venda**: `venda(id, id_cliente(FK), id_prato(FK), quantidade, dia, hora, valor)`

### Constraints
- O campo `sexo` deve conter os valores: `'m'`, `'f'`, ou `'o'`.
- O campo `estado_origem` deve ser um dos estados brasileiros.
- O campo `disponibilidade` deve ser booleano, onde `true` indica que o prato está disponível e `false` indica que está indisponível.
