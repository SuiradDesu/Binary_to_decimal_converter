
binario = input("digite um binario de até 8 digitos: ")
binario.split()
binarios = []
base = []
id = []
expoente = 2


def Bin2Dec():
    for i in binario:
        convertI = int(i)
        if(convertI != 1 and convertI != 0):
            print("Valor inválido, insira somente [0] ou [1]")
        else:
            binarios.append(convertI)

    # reverte a ordem dos binários (a ordem dos fatores nao altera o produto)
    binarios.reverse()

    # itera sobre os index do array (no caso a potencia)
    for index in range(len(binarios)):
        id.append(index)

    # execulta a potenciação
    for i in id:
        base.append(expoente ** i)

    # Multiplica a base com a sequência de binário inserido
    multiplicacaoIdBinario = [B*D for B, D in zip(binarios, base)]

    # Soma os elementos do array acima [no caso o resultado da conversão]
    resultado = 0
    for i in multiplicacaoIdBinario:
        resultado += i
    return resultado


# Valida se o valor inserido é realmente binário.
if('2' in binario):
    print("Digite somente binários [1] ou [0]")
else:
    print(Bin2Dec())
