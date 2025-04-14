matriz = [] # Lista que vai receber as linhas
def matrizDiagonal():
    tamanho = int(input("Digite o tamanho da matriz (linhas x colunas): "))

    # Inicializando a matriz com zeros
    matriz = [[0 for _ in range(tamanho)] for _ in range(tamanho)]

    # Preenchendo a diagonal
    for i in range(tamanho):
        valor = int(input(f"Digite o valor para a posição {i + 1} (na diagonal): "))
        matriz[i][i] = valor  # Preenchendo a diagonal (onde linha == coluna)

    # Exibindo a matriz com uma formatação mais bonita
    print(f"\nMatriz {tamanho}x{tamanho}: ")

    # Calculando o maior número para alinhar
    maior_valor = max(max(linha) for linha in matriz)
    tamanho_espaco = len(str(maior_valor))  # Quantidade de espaços a ser usada para formatação

    for linha in matriz:
        # Imprime cada linha, formatando os números com alinhamento à direita
        print(" ".join(f"{num:>{tamanho_espaco}}" for num in linha))


def matrizIdentica():
    tamanho = int(input("Digite o tamanho da matriz (linhas x colunas): "))

    # Inicializando a matriz com zeros
    matriz = [[0 for _ in range(tamanho)] for _ in range(tamanho)]

    # Preenchendo a diagonal
    for i in range(tamanho):
        matriz[i][i] = 1  # Preenchendo a diagonal (onde linha == coluna)

    # Exibindo a matriz com uma formatação mais bonita
    print(f"\nMatriz {tamanho}x{tamanho}: ")

    # Calculando o maior número para alinhar
    maior_valor = max(max(linha) for linha in matriz)
    tamanho_espaco = len(str(maior_valor))  # Quantidade de espaços a ser usada para formatação

    for linha in matriz:
        # Imprime cada linha, formatando os números com alinhamento à direita
        print(" ".join(f"{num:>{tamanho_espaco}}" for num in linha))

def matrizSimetrica():
    tamanho = int(input("Digite o tamanho da matriz (linhas x colunas): "))

    # Inicializando a matriz com zeros
    matriz = [[0 for _ in range(tamanho)] for _ in range(tamanho)]

    # Preenchendo a diagonal
    for i in range(tamanho):
        valor = int(input(f"Digite o valor para a posição {i + 1} (na diagonal): "))
        matriz[i][i] = valor  # Preenchendo a diagonal (onde linha == coluna)

    # Preenchendo a parte superior da matriz e automaticamente a parte inferior
    for i in range(tamanho):
        for j in range(i + 1, tamanho):  # Preenche apenas a parte superior da matriz
            valor = int(input(f"Digite o valor para a posição ({i + 1}, {j + 1}): "))
            matriz[i][j] = valor  # Preenche a posição (i, j)
            matriz[j][i] = valor  # Preenche a posição simétrica (j, i)

    # Exibindo a matriz com uma formatação mais bonita
    print(f"\nMatriz Simétrica {tamanho}x{tamanho}: ")

    # Calculando o maior número para alinhar
    maior_valor = max(max(linha) for linha in matriz)
    tamanho_espaco = len(str(maior_valor))  # Quantidade de espaços a ser usada para formatação

    for linha in matriz:
        # Imprime cada linha, formatando os números com alinhamento à direita
        print(" ".join(f"{num:>{tamanho_espaco}}" for num in linha))

def matrizTransposta():
    linhas = int(input("Digite o tamanho das linhas: "))
    colunas = int(input("Digite o tamanho das colunas: "))

    for i in range(linhas):
        linha_atual = [] # Nova linha vazia
        for j in range(colunas):
            valor = int(input(f"Digite o valor da posição [{i+1}][{j+1}]: "))
            linha_atual.append(valor) # Preenche a linha
        matriz.append(linha_atual) # Adiciona a linha na matriz

    print("\nMatriz Comum: ")
    for linha in matriz:
        print(" ".join(str(valor) for valor in linha))

    transposta = []
    for j in range(colunas): # Agora percorre as colunas da original
        nova_linha = []
        for i in range(linhas): # Vai buscando o elemento [i][j]
            nova_linha.append(matriz[i][j])
        transposta.append(nova_linha)

    print("\nMatriz Transposta: ")
    for linha in transposta:
        print(" ".join(str(valor) for valor in linha))


while True:
    print("\n1 - Matriz Diagonal")
    print("2 - Matriz Identidade")
    print("3 - Matriz Simétrica")
    print("4 - Matriz Transposta")
    print("\n0 - Sair do Programa")

    escolha = int(input("\nEscolha uma Matriz: "))

    match escolha:
        case 1:
            matrizDiagonal()
        case 2:
            matrizIdentica()
        case 3:
            matrizSimetrica()
        case 4:
            matrizTransposta()
        case 0:
            print("Saindo do programa...")
            break
        case _:
            print("Opção inválida. Tente novamente.")