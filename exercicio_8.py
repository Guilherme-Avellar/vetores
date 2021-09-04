# 8.Implemente uma função que, dado um valor, retorne se esse valor pertence ou não a um vetor de inteiros.

def analisar_inteiros(num, vetor):
    resultado = 'não está contido no vetor'
    if num in vetor:
        resultado = 'está contido no vetor'
    return resultado

vetor1 = [9, 30, 4, 15, 100]
valor1 = int(input("Teste do número: "))
print(analisar_inteiros(valor1, vetor1))

# def verificar_valor(vetor, valor):
#
#     achou = False
#     for i in range(len(vetor)):
#         if vetor[i] == valor:
#             achou = True
#     return achou
#
#
# def verificar_valor_2(vetor, valor):
#     return valor in vetor
#
#
# vetor = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# print(verificar_valor(vetor, 5))