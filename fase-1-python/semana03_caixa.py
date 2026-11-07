# Semana 3, Exercício 9: caixa registradora
#
# O programa deve:
#   1. pedir o preço de um produto, repetindo ATÉ a pessoa digitar 0
#   2. ir somando os preços e contando quantos itens foram registrados
#   3. no final, mostrar a quantidade de itens e o total
#   4. BÔNUS: se o total passar de R$ 200, aplicar 10% de desconto
#
# Exemplo:
#   Preço do produto (0 para encerrar): 50
#   Preço do produto (0 para encerrar): 120.50
#   Preço do produto (0 para encerrar): 45
#   Preço do produto (0 para encerrar): 0
#   Itens: 3 | Total: R$ 215.50
#   Desconto de 10%: R$ 21.55 | A pagar: R$ 193.95
#
# Para rodar (no terminal do VS Code, na pasta do projeto):
#   .venv\Scripts\python.exe fase-1-python\semana03_caixa.py
#
# ----------------------------------------------------------------------
# PASSO A PASSO (rode no terminal depois de CADA passo)
#
# Passo 1: crie as variáveis total = 0 e itens = 0.
#          Peça o primeiro preço com input() e converta com float().
#          Dê um print no preço digitado. Rode.
#
# Passo 2: crie um while que repete ENQUANTO o preço for diferente de 0.
#          Dentro dele: some o preço ao total, some 1 aos itens,
#          e peça o PRÓXIMO preço (senão vira laço infinito!).
#          Rode e digite alguns preços, depois 0.
#          Se travar num laço infinito: Ctrl + C no terminal para parar.
#
# Passo 3: depois do while (sem recuo), mostre itens e total com f-string.
#
# Passo 4 (bônus): use um if para aplicar o desconto de 10% acima de R$ 200.
#
# Teste também: digitar 0 logo no primeiro preço. O que aparece?
# ----------------------------------------------------------------------

# Escreva seu programa abaixo
