# Trabalho avaliativo da forca. Feito sozinho: GUILHERME CARNEIRO AVELLAR.

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

def contar_letras(nova_palavra, tentativa):
    contador = 0
    for i in range(len(nova_palavra)):
        if nova_palavra[i] == tentativa:
            contador = contador + 1
    return contador

def fazer_linha(tentativas, palavra_vetor, tentativa):





    return

# Não estou conseguindo, professor, fazer o código substituir o "_" por uma letra e armazenar pra fazer de novo...tentei
# fazer como fizemos em um exercício de números, mas deu errado, dá erro.

palavra = sortear_palavra()

nova_palavra = ""
palavra_vetor = []
for i in range(len(palavra) - 1):
    nova_palavra = nova_palavra + palavra[i]
    palavra_vetor.append(palavra[i])


print(nova_palavra)
print("JOGO DA FORCA")
print(f"A palavra tem {len(nova_palavra)} letras")
print(fazer_linha("", palavra_vetor,"",))

erros = 0
acertos = 0
tentativa = input(f"Digite sua primeira tentativa: ").upper()
tentativas = []



while erros < 6 or acertos != len(nova_palavra):
    if tentativa in tentativas:
        print("Você já digitou essa letra")
        tentativa = input(f"Digite outra tentativa: ").upper()
    else:
        tentativas.append(tentativa)
        if tentativa in nova_palavra:
            acertos = acertos + contar_letras(tentativas, palavra_vetor)
            print(f"Você acertou! Por enquanto {acertos} acertos de {len(nova_palavra)}")
            print(fazer_linha(tentativas, palavra_vetor, tentativa))
        else:
            erros = erros + 1
            print(f"Você tem {erros} erro(s)")
        tentativa = input(f"Digite outra tentativa: ").upper()
# A flag não tá funcionando Marco. Estou perdendo a sanidade. Vou por um break
        if len(nova_palavra) == acertos or erros == 5:
            break

if acertos == len(nova_palavra):
    print(f"Você acertou tudo. A palavra era {nova_palavra}")
else:
    print(f"Você errou tudo que podia. A palavra era {nova_palavra}")
