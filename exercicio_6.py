# 6.Escrever a função que recebe por parâmetro uma string e um número. A função deve retornar os primeiros caracteres
# da string de acordo com o número passado por parâmetro.

def primeiras_letras(string, num):
    nome = ''
    if num > len(string):
        num = len(string)
    for i in range(num):
        nome = nome + string[i]
    return nome


nome = input("Digite um nome qualquer: ")
primeiros = int(input("Digite o número das primeiras letra a retornar: "))

print(primeiras_letras(nome, primeiros))