# Exercício 8 (Semana 1): salário anual com 13º
# Copiado do notebook para rodar no terminal, onde o input() funciona direto.
# Para rodar:  .venv\Scripts\python.exe fase-1-python\exercicio_08.py

nome = input("Digite seu nome: ")
print("Quanto você ganha (R$)")
salario = int(input())
decimo = (salario * 13)


print(f"Olá, {nome}! Seu salário com 13º é R$ {decimo:.2f}")
