#!/usr/bin/env python
# -*- coding: utf-8 -*-
def pivoting(tableaux,_in, _out):
    i = 0
    j = 0
    newTableaux = []
    pivotLine = 0
    div = 1
    pivot = 0
    mult = 1
    for line in tableaux:
        aux = []
        for col in line:
            if j == 0:
                j+=1
                continue
            if i == _out: #pivot line
                if j == _in:
                    if col != 1:
                        div = col
                        pivot = col
                aux.append(col/div)
                pivotLine = i
                j+=1
            elif j == _in: # itsnot pivot line
                if col == 0:
                    break
                else:
                    if col > 0:
                        mult = pivot *(-col)
                        k = 0
                        for col2 in line:
                            if k == 0:
                                continue
                            else:        
                                aux.append((col2 + mult))
                    else:
                        mult = pivot *(col)
                        k = 0
                        for col2 in line:
                            if k == 0:
                                continue
                            else:        
                                aux.append((col2 + mult))
                            k+=1        
                j+=1                    
        newTableaux.append(aux)    
        i+=1
    print("aquii")    
    for line in newTableaux:
        print(line)
    return newTableaux    

def seachOut(tableaux, minOrMax, p):
    piv = 0
    i = 0
    j = 0
    if minOrMax == 1:#max
        maxI = 0
        for line in tableaux:
            for col in line:
                if i == len(tableaux)-1: # Z line
                    continue
                if j == p:
                    if col != 0:
                        if (line[-1]/col) > maxI:
                            maxI = (line[-1]/col)
                            piv = j
                j += 1
            i += 1
    elif minOrMax == 2: #min
        minI = 0
        for line in tableaux:
            for col in line:
                if i == len(tableaux)-1: # Z line
                    continue
                if j == p:
                    if col != 0:
                        if (line[-1]/col) < minI:
                            minI = (line[-1]/col)
                            piv = j
                j += 1
            i += 1
    return piv  

def seachIn(Z, minOrMax):
    piv = 0
    i = 0
    if minOrMax == 1:
        max = 0
        for res in Z:
            if i == 0:
                continue            
            if i == len(Z)-1:
                break
            if res > max:
                max = res
                piv = i    
            i+=1  
    elif minOrMax == 2:
        min = 0
        for res in Z:
            if i == 0:
                continue
            if i == len(Z)-1:
                break
            if res < min:
                min = res
                piv = i
            i+=1                    
    return piv    

def conditions(Z, minOrMax): # break condition
    i = 0
    if minOrMax == 1:
        for res in Z:
            if i == 0:
                continue
            if i == len(Z)-1: # Z value
                return False
            if res > 0:
                return True
            i+=1        
    elif minOrMax == 2:
        for res in Z:
            if i == 0:
                continue
            if i == len(Z)-1: # Z value
                return False
            if res < 0:
                return True
            i+=1                                    

def iterations(tableaux, minOrMax):
    i = 0
    tam = len(tableaux[-1])# [-1] -> last line(element) from matrix
    while conditions(tableaux[-1], minOrMax): # while Z values are less than 0
        print("iteration "+str(i+1))
        _in = seachIn(tableaux[-1], minOrMax) # ind column that enter in the base
        _out = seachOut(tableaux, minOrMax, _in) # ind base that out from the base
        #pivoting
        tableaux = pivoting(tableaux, _in, _out)

def make_tableaux(Z,type_restrict, restrict, base, result, row, col):
    #base var_restriction result
    #...        ...        ...
    #...        ...        ...
    #xxx        xz1...      Z
    tableaux_1 = []    
    z = 0
    for i in xrange(0,len(base)+1):
        aux = []
        r = 0
        for j in xrange(0,col+2):
            if   i == len(base) and j == 0:
                aux.append(0) # left lower diagonal
            elif j == 0:
                aux.append(base[i])# base lines
            elif i == len(base) and j == col+1:
                aux.append(0) # initial Z value
            elif j == col+1:
                aux.append(result[i]) # result lines
            elif i == len(base):
                print("j")
                print(j)
                aux.append(Z[j-1])
            else:
                aux.append(restrict[i][r])
                r+=1
        tableaux_1.append(aux)

    print("era pra entrar aqui")    
    for x in tableaux_1:
        print(x)
    return tableaux_1

def pattern_F(Z, type_restrict, restrict, result, row, col):
    i = 0
    base = []
    sv_count = 0
    for type_R in type_restrict:
        if type_R == 1: #add new spear var. If type == 1 then its equals to "<="
            col += 1 # att number of columns
            for j in xrange(0,row): # create a triangular of news vars matrix
                if j == i:
                    restrict[j].append(1)
                else:
                    restrict[j].append(0)
                Z.append(0)    
            if result[i] < 0: # negative results -> multiply all var by (-1)
                base.append(-1)
                for var in restrict:
                    for var2 in var:
                        var2 = var2 * (-1)
            else:
                base.append(i+1)
        i+=1        
        type_R = "="
    return Z, restrict, result, base, col

def show(Z, type_restrict, restrict, result, row, col):
    print("Z = ")
    aux = 1
    for x in Z:
        print(str(x)+"X"+str(aux))
        aux += 1
    print("restrição")
    for i in xrange(0,row):
        for j in xrange(0,col):
            if j == col-1:
                print(str(restrict[i][j])+"X"+str(j+1))
                if type_restrict[i] == 1:
                    print(" <= "+str(result[i]))
                else:
                    print(" >= "+str(result[i]))   
            else:    
                print(str(restrict[i][j])+"X"+str(j+1))

def restrict_op(row, col):
    var_z = []
    restrictr = []
    result = []
    type_restrict = []
    for i in xrange(0, col):
        var_z.append(int(input("Z: informe o valor da variavel X"+str(i+1)+": ")))
    
    for i in xrange(0,row):
        aux = []
        for j in xrange(0,col):
            aux.append(int(input("Digite o coeficiente de X"+str(j+1)+" da restrição "+str(i+1)+": ")))
            if(j == col-1):   #Verifica se vai ler um coeficiente de X ou a igualdade da restrictrição
                print("A restrição e de:\n")
                print("1. <=")
                print("2. >= ? \n")
                type_restrict.append(int(input()))
                if type_restrict[i] != 1 and type_restrict[i] != 2:
                    print("Opcao invalida")
                while(type_restrict[i] != 1 and type_restrict[i] != 2):
                    print("A restrição e de:\n")
                    print("1. <=")
                    print("2. >= ? \n")
                    del type_restrict[i]
                    type_restrict[i].append(int(input()))
                    if type_restrict[i] != 1 and type_restrict[i] != 2:
                        print("Opcao invalida")       
                result.append(int(input("Digite o resultado da restrição "+str(i+1)+": ")))
        restrictr.append(aux)
    return var_z, type_restrict, restrictr, result        

def minOrMax():
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

def main():
    _Z_Result = 0
    print("SIMPLEX")
    row = int(input("Quantas restrições tem o problema"))
    col = int(input("Quantas variaveis tem o problema"))
    _type_minMax = minOrMax()
    _Z,_type_restrict, _restrict, _result = restrict_op(row, col)
    show(_Z,_type_restrict, _restrict, _result, row, col)
    #pattern form
    _Z, _restrict, _result, _base, col = pattern_F(_Z, _type_restrict, _restrict, _result, row, col)
    #construct tableaux matrix
    _tableaux = make_tableaux(_Z, _type_restrict, _restrict, _base, _result, row, col)
    _Z_result = iterations(_tableaux, _type_minMax)

main()