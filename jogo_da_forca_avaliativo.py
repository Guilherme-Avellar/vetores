import random

def sortear_palavra():
    arquivo = open("br-sem-acentos.txt")
    linhas = arquivo.readlines()
    palavra = ''
    while len(palavra) < 5 or len(palavra) > 10:
        sorteio = random.randint(0, len(linhas)) + 1
        palavra = linhas[sorteio]
    palavra = palavra.upper()
    arquivo.close()
    return palavra


palavra = sortear_palavra()

nova_palavra = ""
for i in range(len(palavra) - 1):
    nova_palavra = nova_palavra + palavra[i]
print(nova_palavra)



erros = 0
acertos = 0
tentativas = []
resultado2 = ""
def fazer_linha(nova_palavra, tentativa):
    resultado = ""
    if tentativa == "":
        for i in range(len(nova_palavra)):
            resultado = resultado + "_"
    else:
        for j in range(len(nova_palavra)):
            if tentativa == nova_palavra[j]:
                resultado = resultado + tentativa
            else:
                resultado = resultado + "_"

    return resultado
print(fazer_linha(nova_palavra, ""))


while erros < 6 or acertos != len(nova_palavra):
    tentativa = input("Digite uma letra: ").upper()
    tentativas.append(tentativa)
    if tentativa not in palavra:
        erros = erros + 1
    else:
        resultado2 = (fazer_linha(nova_palavra, tentativa))
        print(fazer_linha(nova_palavra, tentativa))
