# 2.Implemente uma função que retorne o maior elemento de um vetor de inteiros.
# 3.Implemente uma função que retorne o menor elemento de um vetor de inteiros.
def menor_valor(n):
    menor = n[0]
    for i in range(len(n)):
        if n[i] < menor:
            menor = n[i]
    return menor

def maior_valor(n):
    maior = n[0]
    for i in range(len(n)):
        if n[i] > maior:
            maior = n[i]
    return maior

inteiros = []
quantidade = int(input("Digite quantos valores você quer testar: "))
if quantidade < 0:
    print("inválido")
else:
    for i in range(quantidade):
        inteiro = int(input("Digite um valor: "))
        inteiros.append(inteiro)
    print(f"O maior valor é: {maior_valor(inteiros)}")
    print(f"O menor valor é: {menor_valor(inteiros)}")