# 5Escrever uma função que recebe por parâmetro um vetor de inteiros e o seu tamanho e retorna a soma de seus elementos

def somar_vetor (vetor, tamanho):
    soma = 0
    for i in range(tamanho):
        soma = soma + vetor[i]
    return soma

vetor1 = []
quantidade = int(input('Digite o tanto de números que quer por: '))
for i in range(quantidade):
    numero = int(input('Digite um número: '))
    vetor1.append(numero)

print(somar_vetor(vetor1, len(vetor1)))



# def retornar_soma(vetor, tamanho):
#     soma = 0
#     for i in range(tamanho):
#         soma = soma + vetor[i]
#
#     return soma
#
# vetor = [80, 10, 20, 4, 50, 2, 0, -1, 90, 3, 2]
#
# print(retornar_soma(vetor, len(vetor)))