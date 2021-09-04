# 9.Implemente uma função que retorne a média dos valores armazenados em um vetor de inteiros.


def media_vetor(vetor):
    soma = 0
    for i in range(len(vetor)):
        soma = soma + vetor[i]
    return soma / len(vetor)

vetor1 = []

for i in range(5):
    num = int(input("Digite um número para o vetor: "))
    vetor1.append(num)

print(media_vetor(vetor1))