# 10.Escrever uma função que substitui por zero todos os números negativos do vetor passado por parâmetro,

def subistituir_negativos(vetor, num):
    for i in range(len(vetor)):
        if vetor[i] < 0:
            vetor[i] = num
    return vetor

vetor1 = []
for i in range(5):
    numero = int(input("Digite um dos números para o vetor: "))
    vetor1.append(numero)
parametro = int(input("Digite o número que irá substituir os negativos: "))

print(subistituir_negativos(vetor1, parametro))