#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Funcao que retorna o modulo de um double
def modulo(self, n):
    if n >= 0:
        return n
    else:
        return (n * (-1))


def imprime_w(self, l, c, tableaux, W):
    i, j, isBasic, k, x, cont = 0
    x = []
    print("\n\n")
    print("\tW\t")
    for j in range(0, c - 2):
        print("X%d\t", (j + 1))

    print("b\n\nbase\t")
    for j in range(0, c):
        print ("%.1lf\t", W[j])

    print("\n\n")
    #1.1 - imprime as outras linhas
    for i in range(1, l):
        for j in range(1, c):
            if tableaux[i][j] == 1:
                isBasic = 0
                for k in range(1, l):
                    if tableaux[k][j] != 0:
                        isBasic = isBasic + 1


                if isBasic == 1:
                    cont+=1
                    x[cont] = j
                    print("X%d\t", (j))
                    break

        for j in range(0, c):
            print("%.1lf\t", (tableaux[i][j]))

        print("\n\n")

def iteracao_w(self, tableaux, W, l, c, lPivo, cPivo):
    i, j
    aux
    aux = tableaux[lPivo][cPivo]
    for i in range(0, c):
        tableaux[lPivo][i] = (tableaux[lPivo][i] / aux)


    for i in range(0, l):
        if i != lPivo:
            for j in range(0, c):
                if j == 0:
                    aux = tableaux[i][cPivo]

                tableaux[i][j] = tableaux[i][j] - (aux * tableaux[lPivo][j])

    for j in range(0, c):
        if j == 0:
            aux = W[cPivo]

        W[j] = W[j] - (aux * tableaux[lPivo][j])



def verificar_w(self, W, c):
    i, aux = 0
    for i in range(1, c - 1):
        if W[i] < 0:
            aux = 1
            break

    if aux == 0 and W[c - 1] != 0:
        aux = 2

    return aux


def win(self, W, c):
    i, indice = 0
    menor = 0
    for i in range(1, c - 1):
        if W[i] < menor:
            menor = W[i]
            indice = i

    return indice


def primeira_fase(self, tableaux, W, l, c, tipo_restricao):
    isOtimo, _in, out, i, aux, j
    cPivo
    cPivo = win(W, c)
    isOtimo = verificar_w(W, c)
    if isOtimo == 1:
        print("\nW NAO E IGUAL A ZEROnot !not \n")
        _in = win(W, c)
        print("\nENTRA A VARIAVEL X%d\n", (_in))
        out = variable_out(tableaux, _in, l, c)
        aux = 0
        for j in range(1, c - 1):
            if tableaux[out][j] == 1:
                for i in range(1, l):
                    if tableaux[i][j] != 0:
                        aux+=1

            if aux == 1:
                aux = j
                break

            else:
                aux = 0

        print("SAI A VARIAVEL X%d\n", (aux))
        
        print("\n\nNOVA SOLUCAO:\n")
        iteracao_w(tableaux, W, l, c, out, _in)
        imprime_w(l, c, tableaux, W)
        primeira_fase(tableaux, W, l, c, tipo_restricao)

    else:
        if isOtimo == 2:
            print("\nA FUNCAO NAO TEM SOLUCAOnot !not \n")
        else:
            print("\nW E IGUAL A ZER0not !not \n")
            print("\nFIM DA PRIMEIRA FASE\n")

        
        if isOtimo == 0:
            print("\n\nINICIO DA SEGUNDA FASE:\n")
            imprime_tableaux(l, c, tableaux, tipo_restricao)
            resultado_tableaux(tableaux, l, c, tipo_restricao)

#1.1 - fun��o que imprime o tableaux
def imprime_tableaux(self, l, c, tableaux, tipo_restricao):
    i, j, isBasic, k, x, cont = 0, tam, k2
    x = [] #2.0 - vetor que guarda os �ndices dos x pra serem impressos embaixo do tableaux
    print("\n\n")
    print("\tZ\t")
    tam = c - 2
    for i in range(0, l - 1):
        tam = tam - tipo_restricao[i]
    for j in range(0, tam):
        print("X%d\t", (j + 1))
    k = 0
    for j in range(tam, c - 2):
        print("X%d\t", (j + 1))
        k+=1
        if tipo_restricao[k] == 2:
            j+=1
    print("b\n\n")
    print("base\t")
    k = 0
    for j in range(0, c):
        print("%.1lf\t", (tableaux[0][j]))   #1.1 - imprime a primeira linha do tableaux
        if j >= tam + 1 and j < c - 1:
            k+=1
            if tipo_restricao[k] == 2:
                j+=1

    print("\n\n")
    #1.1 - imprime as outras linhas
    for i in range(1, l):
        for j in range(1, c):
            if(tableaux[i][j] == 1):   #1.1 - procura por 1 na linha
                isBasic = 0
                for k in range(1, l): #1.1 - se encontrar percorre toda a coluna
                    if tableaux[k][j] != 0:
                        isBasic = isBasic + 1
                if(isBasic == 1):   #1.1 - se o 1 for o �nico elemento diferente de 0 na coluna, vari�vel � b�sica
                    cont+=1
                    x[cont] = j  #2.0 - Nesse ponto x guarda os indices dos X que est�o na base
                    print("X%d\t", (j)) #1.1 - imprima ela
                    break
        k2 = 0
        for j in range(0, c):
            print("%.1lf\t", (tableaux[i][j]))   #1.1 - imprime os elementos de cada linha do tableaux
            if j >= tam + 1 and j < c - 1:
                k2+=1
                if tipo_restricao[k2] == 2:
                    j+=1

        print("\n\n")

    k2 = 0
    for i in range(0, c - 2):   #2.0 - c-2 pois a quantidade de X � a quantidade de colunas menos a linha Z e a linha b
        k = 0  #2.0 - k indica se o x est� ou n�o na base
        print("X%d = ", i + 1)
        for j in range(0, cont):#2.0 - percorre o vetor e busca se o �ndice do x em quest�o est� na base
            if(i + 1 == x[j]):   #2.0 - se sim imprime o valor dele
                print("%.1lf ", (tableaux[j + 1][c - 1]))
                k = 1
                break

        if(k == 0):  #2.0 - se n�o imprime 0
            print("0 ")
        if i >= tam:
            k2+=1
            if tipo_restricao[k2] == 2:
                i+=1

    if tableaux[0][0] == -1 and tableaux[0][c - 1] != 0: #2.0 - Imprime o valor de Z (Max) ou -Z (Min:
        print("\n\nZ = %.1lf\n\n", tableaux[0][c - 1] * (-1))
    else:
        print("\n\nZ = %.1lf\n\n", tableaux[0][c - 1])
    


#1.1 - fun��o que imprime o problema
def imprime_problema(self, op, l, c, Z, restricoes, tipo_restricao):
    i, j, cont = 0
    #Imprime o problema
    print("O problema e:\n")
    #Dependendo da op��o op imprime Max ou Min
    if op == 1:
        print("\Z = ")
    if op == 2:
        print("\Z = ")
    #Imprime Z
    for j in range(0, c - 1):
        if(j == 0):  #Se for o primeiro elemento apenas imprime normalmente
            print("%.0lfX%d ", (Z[j], j + 1))
        else:
            print("%.0lfX%d ", (modulo(Z[j]), j + 1)) #Se for outro elemento imprime apenas o m�dulo
        if(j != c - 2):   #Aqui imprime o sinal para que fique alinhado
            if Z[j + 1] >= 0:
                print("+ ")
            else:
                print("- ")


    #Imprime as restri��es
    print("\n\nSujeito a:\n\n")
    for i in range(0, l):
        for j in range(0, c - 1):   #Vai at� o utimo X
            if j == 0:
                print("%.0lfX%d ", (restricoes[i][j], j + 1))
            else:
                print("%.0lfX%d ", (modulo(restricoes[i][j]), j + 1))
            if j != c - 2:
                if restricoes[i][j + 1] >= 0:
                    print("+ ")
                else:
                    print("- ")

            else:     #Se for o ultimo X, a igualdade e o numero depois dela
                if tipo_restricao[cont] == 1:
                    print("<= ")
                else:
                    print(">= ")
                cont+=1
                print("%.0lf ", (restricoes[i][c - 1]))

        print("\n\n")

    #Imprime as restri��es de >=0
    for j in range(0, c - 1):
        print("X%d", (j + 1))
        if j != c - 2:
            print(", ")

    print(" >= 0")
    


#1.1 - fun��o que imprime o problema na forma padr�o
def imprime_na_forma_padrao(self, l, c, Z, padrao, tipo_restricao, q_var, op):
    i, j, cont = 0
    #Imprimindo na forma padr�o
    print("\n\nForma padrao:\n")
    #1.1 - impress�o do Z modificada para uma forma mais f�cil
    if op == 1:
        print("\nZ ")
    else:
        print("\n- Z ")
    for j in range(0, q_var):
        if Z[j] >= 0:
            print("+ ")
        else:
            print("- ")
        print("%.0lfX%d ", (modulo(Z[j]), j + 1))
    for i in range(q_var + 1, count < l):
        if tipo_restricao[cont] == 1:
            print("+ 0X%d ", (i))
        else:
            print("+ 0X%d ", (i))
            i+=1
            print("+ 0X%d ", (i))

        cont+=1

    print("= 0")
    print("\n\nSujeito a:\n\n")
    for i in range(0, l):
        for j in range(0, c - 1):
            if j == 0:
                print("%.0lfX%d ", (padrao[i][j], j + 1))
            else:
                print("%.0lfX%d ", (modulo(padrao[i][j]), j + 1))
            if j != c - 2:
                if padrao[i][j + 1] >= 0:
                    print("+ ")
                else:
                    print("- ")

            else:
                print("= ")
                print("%.0lf ", (padrao[i][c - 1]))

        print("\n\n")

    for j in range(0, c - 1):
        print("X%d", (j + 1))
        if j != c - 2:
            print(", ")

    print(" >= 0")
    


#1.2 - fun��o p/ selecionar a op��o
def menu(self):
    print("\nO problema e de:\n")
    print("1. Maximizacao\n")
    print("2. Minimizacao\n")
    print("? ")
    op = int(input())
    if op != 1 and op != 2:
        print("Opcao invalidanot \n")

    while(op != 1 and op != 2):
        print("\nO problema e de:\n")
        print("1. Maximizacao\n")
        print("2. Minimizacao\n")
        print("? ")
        op = int(input())
        if op != 1 and op != 2:
            print("Opcao invalidanot \n")
    return op


#1.2 - fun��o p/ ler valores de Z e da matriz de Restri��es
def salvar_valores(Z, restricoes, l, c, tipo_restricao):
    cont = 0
    for i in range(0, c - 1):
        print("Digite o coeficiente de X%d de Z: ", (i + 1))
        Z.append(int(input()))

    for i in range(0, l):
        for j in range(0, c):
            if(j == c - 1):   #Verifica se vai ler um coeficiente de X ou a igualdade da restri��o
                print("A restricao e de:\n")
                print("1. <=\n")
                print("2. >=\n? ")
                tipo_restricao[cont] = int(input())
                if tipo_restricao[cont] != 1 and tipo_restricao[cont] != 2:
                    print("Opcao invalidanot \n")
                while(tipo_restricao[cont] != 1 and tipo_restricao[cont] != 2):
                    print("A restricao e de:\n")
                    print("1. <=\n")
                    print("2. >=\n? ")
                    tipo_restricao[cont] = int(input())
                    if tipo_restricao[cont] != 1 and tipo_restricao[cont] != 2:
                        print("Opcao invalidanot \n")                    
                cont+=1
                print("Digite o resultado da restricao %d: ", (i + 1))

            else:
                print("Digite o coeficiente de X%d da restricao %d: ", (j + 1, i + 1))
            aux = []
            aux.append(int(input()))
            restricoes.append(aux)



#1.2 Verifica se a fun��o � �tima
def verificar_otimo(tableaux, c, l, cPivo):   #1.6 - O cabe�alho da fun��o foi alterado, h� a necessidade de receber o numero de linhas do tableaux e a coluna Piv�.
    i, aux = 0
    if(cPivo != 0):   #1.8.1 - Precisei fazer isso pra corrigir um bug, 0 como valor inicial do indice de variable_in, no ultimo tableaux, n�o tem variaveis pra entrar a fun��o vai jogar um lixo em cPivo, quando tu tentar ler ela aqui o programa vai parar de funcionar, n�o existe a coluna "lixo"
        for i in range(0, l): #1.6 - para percorrer toda a coluna piv�
            if tableaux[i][cPivo] > 0:
                aux+=1 #1.6 - Se pelo algum elemento da coluna piv� for positivo, aux � incrementado, que a solu��o n�o � infinita
        if(aux == 0): #1.6 - Se nesse ponto do programa aux for igual 0, que na coluna piv� s� h� valores negativos
            return 2 #1.6 - Retorna 2 indicando que a solu��o � infinita
        aux = 0

    for i in range(1, c - 1): #1.2 - percorre somente as culunas das vari�veis Xi.
        if tableaux[0][i] < 0:
            aux = 1 #1.2 - aux recebe 1, que ainda h� vari�veis negativas, a solu��o n�o � otima.
            break

    return aux #1.2 - se aux aqui for 0, que a solu��o � �tima


#1.2 - fun��o que encontra quem deve entrar na base.
def variable_in(self, tableaux, c):
    i, indice = 0 #1.2 - indice vai indicar a coluna do tlabeux que est� a vari�vel que deve entrar na base.
    menor = 0.0 #1.2 - variavel auxiliar pra ir comparando os valores das vari�veis Xi
    for i in range(1, c - 1): #1.5 - i inicia com 1, n�o precisa comparar a coluna do Z e vai at� c-1, n�o compara a umtima coluna de resultados.
        if tableaux[0][i] < menor:
            menor = tableaux[0][i]
            indice = i #1.2 - Se por exemplo, vari�vel que for entrar na base for X1, indice vai guardar 1

    return indice


#1.2 - fun��o que encontra quem deve sair da base.
def variable_out(self, tableaux, ind, l, c):
    i, indice # 1.2- indice guarda a linha que est� a vari�vel que vai sair.
    menor = 100000.0, result #1.2 - result guarda o resultado da divis�o dos elementos de B pelos valores da coluna piv�
    for i in range(1, l): #1.2 - come�a a percorrer depois da linha do Z
        if(tableaux[i][ind] > 0):   #1.2 - S� ir� dividir se o denominador for maior que 0
            result = tableaux[i][c - 1] / tableaux[i][ind] #1.2 - divis�o da �ltima coluna do tableaux pelos elementos da linha piv�.
            if(result < menor):   # 1.2 - vai comparando se o resultado da divis�o � menor que o valor da divis�o anterior
                menor = result #1.2 - se for menor, este resultado como o novo menor
                indice = i
    return indice


#1.5 - fun��o para testar se as fun��es variable_in e variable_out est�o funcionando
def resultado_tableaux(self, tableaux, l, c, tipo_restricao):
    isOtimo, _in, out, i, aux, j
    cPivo #1.6 - vari�vel auxiliar para receber a coluna piv� do tableaux
    cPivo = variable_in(tableaux, c) #1.6 - A fun��o variable_in s� � chamada pq a fun��o abaixo(verificar_otimo) precisa saber quem � a coluna piv�
    isOtimo = verificar_otimo(tableaux, c, l, cPivo)
    #1.8 - Verifica se a solu��o � multipla
    aux = 0
    for i in range(1, c - 1): #1.8 - Percorre a linha da base guardando a quantidade de zeros em aux
        if tableaux[0][i] == 0:
            aux+=1
    for i in range(0, l - 1):
        if tipo_restricao[i] == 2:
            aux-=1
    if(aux > l - 1): #1.8 - Se houverem mais zeros do que variaveis na base a solu��o � multipla
        print("\nO PROBLEMA POSSUI MULTIPLAS SOLUCOESnot \n")
    #1.7 - Verifica se a solu��o � degenerada
    aux = 0
    for i in range(1, l):#1.7 - A linha da base n�o conta, isso come�a do 1
        if(tableaux[i][c - 1] <= 1e-10 and tableaux[i][c - 1] >= -1e-10): #1.7 - Se houver algum 0 na ultima coluna (b) incrementa aux
            aux+=1
    if aux > 0: #1.7 - Se aux for maior que 0 significa que alguma variavel b�sica � 0 (Solu��o degenerada:
        print("\nA SOLUCA0 E DEGENERADAnot \n")
    if isOtimo == 1:
        print("\nA SOLUCAO NAO E OTIMAnot !not \n")
        _in = variable_in(tableaux, c)
        print("\nENTRA A VARIAVEL X%d\n", (_in))
        out = variable_out(tableaux, _in, l, c)
        #2.0 - baseado no �ndice de out, qual X vai sair da base (quase o msm algoritmo que esta em imprimir_tableaux)
        aux = 0
        for j in range(1, c - 1):
            if tableaux[out][j] == 1:
                for i in range(1, l):
                    if tableaux[i][j] != 0:
                        aux+=1
            if aux == 1:
                aux = j
                break

            else:
                aux = 0

        print("SAI A VARIAVEL X%d\n", (aux))
        
        print("\n\nNOVA SOLUCAO:\n")
        iteracao_tableaux(tableaux, l, c, out, _in)
        imprime_tableaux(l, c, tableaux, tipo_restricao)
        resultado_tableaux(tableaux, l, c, tipo_restricao) #1.5 - como n�o � otimo chama a fun��o recursivamente.

    else:
        if isOtimo == 2:
            print("\nA FUNCAO TEM SOLUCAO INFINITAnot !not \n")
        else:
            print("\nA SOLUCAO E OTIMAnot !not \n")
        



#1.5 - fun��o que aplica os c�lculos no tableuax
def iteracao_tableaux(self, tableaux, l, c, lPivo, cPivo):
    i, j
    aux
    aux = tableaux[lPivo][cPivo]
    for i in range(0, c): #1.5 - para o c�lculo da nova linha piv�
        tableaux[lPivo][i] = tableaux[lPivo][i] / aux   #A nova linha ser� ela mesma dividida pela intersecc��o entre a linha e a coluna piv�s
    for i in range(0, l):   #1.5 - inicia o percurso pela primeira linha do tableaux
        if(i != lPivo): #1.5 - s� prossigo com os c�lculos se a linha atual n�o for a linha piv�, ela j� foi calculada antes
            for j in range(0, c):   #1.5 - caso n�o seja a LP, toda a linha
                if j == 0:
                    aux = tableaux[i][cPivo]#1.5 - aux guarda a intersec��o entre a linha atual com a coluna piv�
                tableaux[i][j] = tableaux[i][j] - (aux * tableaux[lPivo][j])
                # 1.5 - Os novos valores de cada linha, � cada valor subtraido da multiplica��o de aux com o valor correspondente na mesma coluna, s� que na linha Piv�

#1.2 - Menu Principal
def menu_principal():
    op = 0
    print("-=1-=1-=1-=1-=1SIMPLEX-=1-=1-=1-=1-=1\n")
    print("DESEJA UTILIZAR PROBLEMAS DO ARQUIVO OU INSERIR PROBLEMAS MANUALMENTE?\n")
    print("1. ARQUIVO\n")
    print("2. DIGITAR\n")
    print("3. SAIR\n\n")
    print("Opcao: ")
    op = int(input())
    while(op != 1 and op != 2 and op != 3):
        print("ola mundo")
        print("-=1-=1-=1-=1-=1SIMPLEX-=1-=1-=1-=1-=1\n")
        print("DESEJA UTILIZAR PROBLEMAS DO ARQUIVO OU INSERIR PROBLEMAS MANUALMENTE?\n")
        print("1. ARQUIVO\n")
        print("2. DIGITAR\n")
        print("3. SAIR\n\n")
        print("Opcao: ")
        op = int(input("valor"))
        print(op)
        print(type(op))
    return op

#1.2 - Menu Principal
def menu_continuar():
    print("DESEJA CONTINUAR COM OUTRO PROBLEMA?\n")
    print("1. SIM\n")
    print("2. NAO\n\n")
    print("Opcao: ")
    op = int(input())
    while(op != 1 and op != 2):
        print("DESEJA CONTINUAR COM OUTRO PROBLEMA?\n")
        print("1. SIM\n")
        print("2. NAO\n\n")
        print("Opcao: ")
        op = int(input())
    return op


# Main
def main():
    Z = []
    restricoes = []
    tipo_restricao = []
    cont = 0
    padrao = []
    W = []
    opcao = menu_principal()
    if opcao == 1:
        #arquivo = fopen("in.txt", "r")
        #if fscanf(arquivo, "%d %d", l, c) == EOF:
        #    print("NAO EXISTE MAIS PROBLEMAS NO ARQUIVOnot !not \n")
            
        #    continue

        # tamZ = c
        # c = c + 1
        # cont = 0
        # for i in range(0, c - 1):
        #     fscanf(arquivo, "%lf", Z[i])
        # for i in range(0, l):
        #     for j in range(0, c):
        #         if(j == c - 1)   #Verifica se vai ler um coeficiente de X ou a igualdade da restri��o
        #             fscanf(arquivo, "%d", tipo_restricao[cont])
        #             cont+=1

        #         fscanf(arquivo, "%lf", restricoes[i][j])

        # fscanf(arquivo, "%d", op)
        # fclose(arquivo)
        print(".")
    elif opcao == 2:
        #system("cls")
        print("-=1-=1-=1-=1-=1SIMPLEX-=1-=1-=1-=1-=1\n")
        print("\nQuantas restricoes tem o problema? ")  #A quantidade de restri��es representa a quantidade de linhas da matriz
        l = int(input())
        if l <= 0:
            print("Quantidade invalidanot \n")
        while(l <= 0):
            print("\nQuantas restricoes tem o problema? ")  #A quantidade de restri��es representa a quantidade de linhas da matriz
            l = int(input())
            if l <= 0:
                print("Quantidade invalidanot \n")
        print("\nQuantas variaveis tem o problema? ") #A quantidade de vari�veis + 1 representa a quantidade de colunas da matriz
        c = int(input())
        if c <= 0:
            print("Quantidade invalidanot \n")
        while(c <= 0):
            print("\nQuantas variaveis tem o problema? ") #A quantidade de vari�veis + 1 representa a quantidade de colunas da matriz
            c = int(input())
            if c <= 0:
                print("Quantidade invalidanot \n")
        tamZ = c
        c = c + 1
        print("\n")
        salvar_valores(Z, restricoes, l, c, tipo_restricao) # 1.2 - fun��o criada separadamente pra ler as entradas de dados
        op = menu() #1.2 - fun��o menu criada s� pra diminuir um pouco o c�digo na main
    else:
        exit(0)

    imprime_problema(op, l, c, Z, restricoes, tipo_restricao)
    #Colocando a matriz na forma padr�o
    #aux=c-1    #Guarda em aux a posi��o da matriz a partir da qual v�o se colocar as vari�veis de folga
    aux = 0
    #c=c+l  #O n�mero de colunas da matriz aumenta por causa das vari�veis de folga
    q_var = c - 1
    for i in range(0, l):
        c = c + tipo_restricao[i]

    for i in range(0, l):
        for j in range(0, c - 1):
            if(j < q_var):  #Ate o tamanho da matriz restricoes apenas copia os coeficientes de uma pra outra
                padrao[i][j] = restricoes[i][j]

            else:
                if(j == q_var):   #Copia a igualdade da matriz restri��es para o fim da matriz padrao
                    padrao[i][c - 1] = restricoes[i][j]

                padrao[i][j] = 0



    for j in range(0, c - 1):
        if j >= q_var:
            if tipo_restricao[cont] == 1:
                padrao[aux][j] = 1

            else:
                if padrao[aux][j - 1] == -1:
                    padrao[aux][j] = 1

                else:
                    padrao[aux][j] = -1
                    cont-=1
                    aux-=1


            cont+=1
            aux = aux + 1


    #1.1 - Colocando Z na forma padr�o
    if op == 1:  #1.3 - s� muda o sinal se for de maximiza��o (equivale a multiplicar todo o Z por -1:
        for j in range(0, q_var):
            Z[j] = Z[j] * (-1)


    Z[j] = 0
    #restricoes = desaloca_matriz(l, restricoes)   #Matriz restri��es n�o vai mais ser usada, ent�o desaloquei ela
    imprime_na_forma_padrao(l, c, Z, padrao, tipo_restricao, q_var, op)
    tableaux[100][100] #1.1 - tableaux � a matriz que vai guardar o tableaux
    c = c + 1 #1.1 - precisa de mais uma coluna para o Z
    l = l + 1 #1.1 - precisa de mais uma linha para a base
    #1.1. - Definindo a primeira coluna do tableaux
    if op == 1:
        tableaux[0][0] = 1
    else:
        tableaux[0][0] = -1 #1.3 - caso seja de minimiza��o multiplica-se a linha base por -1, o Z

    #Atribui��o da coluna do Z que tem 1 na primeira linha e 0 nas outras
    for i in range(1, l):
        tableaux[i][0] = 0


    #1.1 - Colocando Z no tableaux
    for j in range(1, tamZ + 1):  #1.1 - Atribuindo o vetor Z como a linha baase no tableaux
        tableaux[0][j] = Z[j - 1]
    for j in range(tamZ+1, j < c, 1):
        tableaux[0][j] = 0

    #1.1 - Colocando as restri��es no tableaux
    for i in range(1, l):
        for j in range(1, c):
            tableaux[i][j] = padrao[i - 1][j - 1]
    aux = 0
    for i in range(0, l - 1):
        if tipo_restricao[i] == 2:
            aux = 1
            break
    print("\n\nTableaux:")
    if aux == 1:
        W[0] = -1
        for i in range(0, l - 1):
            if tipo_restricao[i] == 2:
                for j in range(0, c - 1):
                    W[j + 1] = W[j + 1] + (padrao[i][j] * (-1))
                for j in range(c-1, j != 0, -1):
                    if W[j] == -1:
                        W[j] = 0
                        break
        imprime_w(l, c, tableaux, W)
        primeira_fase(tableaux, W, l, c, tipo_restricao)

    else:
        imprime_tableaux(l, c, tableaux, tipo_restricao)
        resultado_tableaux(tableaux, l, c, tipo_restricao)

    opcao = menu_continuar()

    while(opcao != 2):
        opcao = menu_principal()
        if opcao == 1:
            #arquivo = fopen("in.txt", "r")
            #if fscanf(arquivo, "%d %d", l, c) == EOF:
            #    print("NAO EXISTE MAIS PROBLEMAS NO ARQUIVOnot !not \n")
                
            #    continue

            # tamZ = c
            # c = c + 1
            # cont = 0
            # for i in range(0, c - 1):
            #     fscanf(arquivo, "%lf", Z[i])
            # for i in range(0, l):
            #     for j in range(0, c):
            #         if(j == c - 1)   #Verifica se vai ler um coeficiente de X ou a igualdade da restri��o
            #             fscanf(arquivo, "%d", tipo_restricao[cont])
            #             cont+=1

            #         fscanf(arquivo, "%lf", restricoes[i][j])

            # fscanf(arquivo, "%d", op)
            # fclose(arquivo)
            break
        elif opcao == 2:
            #system("cls")
            print("-=1-=1-=1-=1-=1SIMPLEX-=1-=1-=1-=1-=1\n")
            print("\nQuantas restricoes tem o problema? ")  #A quantidade de restri��es representa a quantidade de linhas da matriz
            l = int(input())
            if l <= 0:
                print("Quantidade invalidanot \n")
            while(l <= 0):
                print("\nQuantas restricoes tem o problema? ")  #A quantidade de restri��es representa a quantidade de linhas da matriz
                l = int(input())
                if l <= 0:
                    print("Quantidade invalidanot \n")
            print("\nQuantas variaveis tem o problema? ") #A quantidade de vari�veis + 1 representa a quantidade de colunas da matriz
            c = int(input())
            if c <= 0:
                print("Quantidade invalidanot \n")
            while(c <= 0):
                print("\nQuantas variaveis tem o problema? ") #A quantidade de vari�veis + 1 representa a quantidade de colunas da matriz
                c = int(input())
                if c <= 0:
                    print("Quantidade invalidanot \n")
            tamZ = c
            c = c + 1
            print("\n")
            salvar_valores(Z, restricoes, l, c, tipo_restricao) # 1.2 - fun��o criada separadamente pra ler as entradas de dados
            op = menu() #1.2 - fun��o menu criada s� pra diminuir um pouco o c�digo na main
            break
        else:
            exit(0)

        imprime_problema(op, l, c, Z, restricoes, tipo_restricao)
        #Colocando a matriz na forma padr�o
        #aux=c-1    #Guarda em aux a posi��o da matriz a partir da qual v�o se colocar as vari�veis de folga
        aux = 0
        #c=c+l  #O n�mero de colunas da matriz aumenta por causa das vari�veis de folga
        q_var = c - 1
        for i in range(0, l):
            c = c + tipo_restricao[i]

        for i in range(0, l):
            for j in range(0, c - 1):
                if(j < q_var):  #Ate o tamanho da matriz restricoes apenas copia os coeficientes de uma pra outra
                    padrao[i][j] = restricoes[i][j]

                else:
                    if(j == q_var):   #Copia a igualdade da matriz restri��es para o fim da matriz padrao
                        padrao[i][c - 1] = restricoes[i][j]

                    padrao[i][j] = 0



        for j in range(0, c - 1):
            if j >= q_var:
                if tipo_restricao[cont] == 1:
                    padrao[aux][j] = 1

                else:
                    if padrao[aux][j - 1] == -1:
                        padrao[aux][j] = 1

                    else:
                        padrao[aux][j] = -1
                        cont-=1
                        aux-=1


                cont+=1
                aux = aux + 1


        #1.1 - Colocando Z na forma padr�o
        if op == 1:  #1.3 - s� muda o sinal se for de maximiza��o (equivale a multiplicar todo o Z por -1:
            for j in range(0, q_var):
                Z[j] = Z[j] * (-1)


        Z[j] = 0
        #restricoes = desaloca_matriz(l, restricoes)   #Matriz restri��es n�o vai mais ser usada, ent�o desaloquei ela
        imprime_na_forma_padrao(l, c, Z, padrao, tipo_restricao, q_var, op)
        tableaux[100][100] #1.1 - tableaux � a matriz que vai guardar o tableaux
        c = c + 1 #1.1 - precisa de mais uma coluna para o Z
        l = l + 1 #1.1 - precisa de mais uma linha para a base
        #1.1. - Definindo a primeira coluna do tableaux
        if op == 1:
            tableaux[0][0] = 1
        else:
            tableaux[0][0] = -1 #1.3 - caso seja de minimiza��o multiplica-se a linha base por -1, o Z

        #Atribui��o da coluna do Z que tem 1 na primeira linha e 0 nas outras
        for i in range(1, l):
            tableaux[i][0] = 0


        #1.1 - Colocando Z no tableaux
        for j in range(1, tamZ + 1):  #1.1 - Atribuindo o vetor Z como a linha baase no tableaux
            tableaux[0][j] = Z[j - 1]
        for j in range(tamZ+1, j < c, 1):
            tableaux[0][j] = 0

        #1.1 - Colocando as restri��es no tableaux
        for i in range(1, l):
            for j in range(1, c):
                tableaux[i][j] = padrao[i - 1][j - 1]
        aux = 0
        for i in range(0, l - 1):
            if tipo_restricao[i] == 2:
                aux = 1
                break
        print("\n\nTableaux:")
        if aux == 1:
            W[0] = -1
            for i in range(0, l - 1):
                if tipo_restricao[i] == 2:
                    for j in range(0, c - 1):
                        W[j + 1] = W[j + 1] + (padrao[i][j] * (-1))
                    for j in range(c-1, j != 0, -1):
                        if W[j] == -1:
                            W[j] = 0
                            break
            imprime_w(l, c, tableaux, W)
            primeira_fase(tableaux, W, l, c, tipo_restricao)

        else:
            imprime_tableaux(l, c, tableaux, tipo_restricao)
            resultado_tableaux(tableaux, l, c, tipo_restricao)

        opcao = menu_continuar()
    return 0

main()