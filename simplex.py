#!/usr/bin/env python
# -*- coding: utf-8 -*-
def pivoting(tableaux,_colPivot, _linePivot):
    i = 0
    newTableaux = []
    pivotLine = []
    mult = 1
    for line in tableaux: #seek and store pivot line
        aux = []
        j = 0
        for col in line:
            if j == 0:
                j+=1
                continue
            if i == _linePivot: #index pivot line
                if j == _colPivot: #index column pivot
                    if col != 1: 
                        div = float(col)
                        k = 0
                        for col2 in line:
                            if k == 0:
                                pivotLine.append(col2)
                            else:
                                pivotLine.append(float(col2)/div)
                            k+=1 
                    else:
                        k = 0
                        for col2 in line:
                            pivotLine.append(col2)
                            k+=1               
                    break
            j+=1 
        i+=1
    print("pivotLine")
    print(pivotLine)               
    i = 0                    
    for line in tableaux:
        aux = []
        j = 0
        for col in line:
            if j == 0:
                j+=1
                continue
            if i == _linePivot:
                newTableaux.append(pivotLine)
                j+=1
                break    
            elif j == _colPivot: # itsnot pivot line, but is over pivot column
                if col == 0: #line already is normalized
                    for col2 in line:
                        aux.append(col2)
                else:   
                    mult = 0
                    l = 0 
                    for col2 in line:
                        if l == _colPivot:
                            mult = col2
                            break
                        l+=1    
                    k = 0        
                    for col2 in line:
                        if k == 0:
                            aux.append(col2)
                        else:    
                            aux.append((col2 - pivotLine[k]*mult))
                        k+=1    
                break        
            j+=1
        if aux:
            newTableaux.append(aux)    
        i+=1
    for line in newTableaux:
        print(line)
    return newTableaux    

def seachOut(tableaux, minOrMax, p): #seach index var from base that'll come out
    piv = 0
    i = 0
    if minOrMax == 1:#max
        maxI = 0
        for line in tableaux:
            j = 0 
            if i < len(tableaux):
                for col in line:
                    if j == p:
                        if col != 0: # SPLIT TEST
                            if (line[-1]/col) >= maxI: #last column (result) div for value pivot column
                                maxI = (line[-1]/col)
                                piv = i
                    j += 1
            else:
                break        
            i += 1
    elif minOrMax == 2: #min
        minI = 0
        for line in tableaux:
            j = 0 
            if i < len(tableaux):
                for col in line:
                    if j == p:
                        if col != 0: #SPLIT TEST
                            if (line[-1]/col) <= minI:
                                minI = (line[-1]/col)
                                piv = i
                    j += 1
            else:
                break    
            i += 1
    return piv  

def seachIn(Z, minOrMax): # seach the value that'll come to base (index column)
    piv = 0
    i = 0
    if minOrMax == 1:
        maxI = 0
        for res in Z:
            if i == 0:
                i += 1       
                continue     
            if i == len(Z)-1:
                break
            if res > maxI:
                maxI = res
                piv = i    
            i+=1  
    elif minOrMax == 2:
        minI = 0
        for res in Z:
            if i == 0:
                i += 1
                continue
            if i == len(Z)-1:
                break
            if res < minI:
                minI = res
                piv = i
            i+=1                    
    return piv    

def conditions(Z, minOrMax): # break condition
    i = 0
    if minOrMax == 1:
        for res in Z:
            if i == 0:
                i += 1
                continue
            if i == len(Z)-1: # Z value
                return False
            if res > 0: 
                return True
            i+=1        
    elif minOrMax == 2:
        for res in Z:
            if i == 0:
                i += 1
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
        _colPivot = seachIn(tableaux[-1], minOrMax) # index column that enter in the base
        _linePivot = seachOut(tableaux, minOrMax, _colPivot) # index base that out from the base
        #pivoting
        print("_linePivot")
        print(_linePivot)
        print("_colPivot")        
        print(_colPivot)        
        tableaux = pivoting(tableaux, _colPivot, _linePivot)
        i+=1

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
                aux.append(Z[j-1])
            else:
                aux.append(restrict[i][r])
                r+=1
        tableaux_1.append(aux)   
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
                for var in restrict:
                    for var2 in var:
                        var2 = var2 * (-1)
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