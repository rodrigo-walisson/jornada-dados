# Semana 2, Exercício 8: simulador de desconto
#
# O programa deve:
#   1. perguntar o valor da compra
#   2. perguntar se a pessoa é cliente fidelidade (s ou n)
#   3. aplicar as regras:
#        - cliente fidelidade         -> 10% de desconto
#        - compra acima de R$ 500     -> mais 5% (acumula com o anterior)
#   4. mostrar o desconto total em % e o valor final
#
# Exemplo:
#   Valor da compra: 600
#   Cliente fidelidade? (s/n): s
#   Desconto: 15% | Valor final: R$ 510.00
#
# Para rodar (no terminal do VS Code, na pasta do projeto):
#   .venv\Scripts\python.exe fase-1-python\semana02_desconto.py
#
# Dicas:
#   - input() sempre devolve texto: o valor da compra precisa virar número
#   - comece com desconto = 0 e vá somando conforme as regras
#   - teste os 4 casos: fidelidade s/n  x  compra acima/abaixo de 500

# Escreva seu programa abaixo
print("Qual o valor da compra?")
valor_compra = float(input())
print("Cliente fidelidade? (s/n)")
fidelizado = (input())


if fidelizado == "n":
    desconto = 0
    valor_desconto = valor_compra - (valor_compra * 0.0)
if fidelizado == "n" and valor_compra > 500:
    desconto = 5
    valor_desconto = valor_compra - (valor_compra * 0.05)
if fidelizado == "s":
    desconto = 10
    valor_desconto = valor_compra - (valor_compra * 0.1)
if fidelizado == "s" and valor_compra > 500:
    desconto = 15
    valor_desconto = valor_compra - (valor_compra * 0.15)


print(f"desconto: {desconto} % |  Valor final: {valor_desconto}")
