# Escrever uma função que receba um vetor com 10 valores e retorne quantos destes valores são negativos.

def contar_negativos(vetor_valores):
    qtde_negativos = 0
    for i in range(len(vetor_valores)):
        if valores[i] < 0:
            qtde_negativos = qtde_negativos + 1
    return qtde_negativos


valores = []
for i in range(10):
    valor = int(input("Digite um valor: "))
    valores.append(valor)

print(f"O número de valores negativos é {contar_negativos(valores)}")

# def contar_negativos(n):
#     soma = 0
#     for i in range(len(n)):
#         if n[i] < 0:
#             soma = soma + 1
#     return soma
#
# valores = []
#
# for i in range(5):
#     valor = int(input("Digite um valor: "))
#     valores.append(valor)
#
# print(contar_negativos(valores))