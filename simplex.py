#!/usr/bin/env python
# -*- coding: utf-8 -*-

def pivoting(tableaux,_colPivot, _linePivot):
    """
    [function to make a pivonting from tableaux matrix]
    
    Arguments:
        tableaux {[matrix]} -- [description]
        _colPivot {[int]} -- [index of column pivot]
        _linePivot {[int]} -- [index of line pivot]
    
    Returns:
        [matrix] -- [tableaux pivoted]
    """
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
    for x in range(0, len(tableaux[0])):
        if x == 0:
            print("Bs ", end='')
        elif x == len(tableaux[0])-1:
            print("b")
        else:             
            print("X"+str(x)+"  ", end='')
    i = 0        
    for line in newTableaux:
        j = 0
        for col in line:
            if j == 0:
                print("X%d" % (col), end='')
            else:
                if col < 0:    
                    print("%.1f" % (col), end='')
                else:
                    print(" %.1f" % (col), end='')    
            j+=1    
        print("")    
    return newTableaux    

def indexLinePivot(tableaux, minOrMax, _colPivot, _linePivot): #seach index var from base that'll come out
    """
    [seach the index of the variable that is come out]
    
    Arguments:
        tableaux {[matrix]} -- [matrix with all elements]
        minOrMax {[int]} -- [<= or >=]
        _colPivot {[int]} -- [index of actual column pivot]
        _linePivot {[int]} -- [index of the last line pivot]
    
    Returns:
        [int] -- [index of actual pivot line]
    """
    piv = -1
    if minOrMax == 1:#max
        print("new column pivot: "+str(_colPivot))
        i = 0
        maxI = 9999
        for line in tableaux:
            j = 0 
            if i != _linePivot and i < len(tableaux)-1:
                for col in line:
                    if j == _colPivot and col > 0 and (float(line[-1])/float(col)) < maxI: #SPLIT TEST
                            maxI = (float(line[-1])/float(col))
                            piv = i
                    j += 1   
            i += 1 
    elif minOrMax == 2: #min
        i = 0
        minI = 9999
        for line in tableaux:
            j = 0 
            if i != _linePivot:
                if i < len(tableaux)-1:
                    for col in line:
                        if j == _colPivot and col > 0 and (float(line[-1])/float(col)) <= minI: #SPLIT TEST
                                minI = (float(line[-1])/float(col))
                                piv = i
                        j += 1     
            i += 1    
    print("Variavel que sai: X"+str(tableaux[piv][0])) 
    return piv

def indexColumnPivot(Z, minOrMax, tableaux, _colPivot): # seach the value that'll come to base (index column)
    """
    [seach the index of pivot column. That is a value that'll come to base]
    
    Arguments:
        Z {[list]} -- [list from Z line]
        minOrMax {[int]} -- [description]
        tableaux {[matrix]} -- [description]
        _colPivot {[int]} -- [last index of pivot column]
    
    Returns:
        [int] -- [index of actual pivot column]
    """
    piv = 0
    if minOrMax == 1:
        maxI = -9999
        piv = 0
        j = 0
        for line in tableaux:
            i = 0   
            if j < len(tableaux):
                for z_value in Z:
                    if i < len(Z)-1 and z_value < 0: # dont take result column
                        if i > 0: # dont take base column
                            if i != _colPivot: # 
                                if i == line[0]:
                                    break
                                if abs(z_value) > maxI:
                                    #verific if this index already is in base
                                    k = 1
                                    flag = True
                                    for line in tableaux:
                                        if k < len(tableaux):
                                            if line[0] == i:
                                                flag = False
                                                break 
                                        k+=1                                                    
                                    if flag:
                                        maxI = abs(z_value)
                                        piv = i
                    i+=1
            j += 1 
    elif minOrMax == 2:
        minI = -9999
        piv = 0
        j = 0
        for line in tableaux:
            i = 0   
            if j < len(tableaux):
                for z_value in Z:
                    if i < len(Z)-1 and z_value < 0: # dont take result column
                        if i > 0: # dont take base column
                            if i != _colPivot: # 
                                if i == line[0]:
                                    break
                                if abs(z_value) > minI:
                                    #verific if this index already is in base
                                    k = 1
                                    flag = True
                                    for line in tableaux:
                                        if k < len(tableaux):
                                            if line[0] == i:
                                                flag = False
                                                break 
                                        k+=1                                                    
                                    if flag:
                                        minI = z_value
                                        piv = i
                    i+=1
            j += 1
    print("Variavel que entra: X"+str(piv))                                 
    return piv  

def seachFirstLN(tableaux, minOrMax, _colPivot): #seach index var from base that'll come out
    """
    [seach the first index of the variable that is come out]
    
    Arguments:
        tableaux {[matrix]} -- [matrix with all elements]
        minOrMax {[int]} -- [<= or >=]
        _colPivot {[int]} -- [index of actual column pivot]
    
    Returns:
        [int] -- [index of actual pivot line]
    """
    piv = 0
    if minOrMax == 1: #max case
        i = 0
        maxI = 9999
        for line in tableaux:
            if i < len(tableaux)-1:
                j = 0
                for col in line:
                    if j == _colPivot:
                        if col > 0: #SPLIT TEST
                            if (float(line[-1])/float(col)) <= maxI:
                                maxI = (float(line[-1])/float(col))
                                piv = i
                    j += 1  
            i += 1 
    elif minOrMax == 2: #min case
        i = 0
        minI = 9999
        for line in tableaux:
            j = 0 
            if i < len(tableaux)-1:
                for col in line:
                    if j == _colPivot:
                        if col > 0: #SPLIT TEST
                            if (float(line[-1])/float(col)) <= minI:
                                minI = (float(line[-1])/float(col))
                                piv = i
                    j += 1    
            i += 1
    print("Variavel que sai: X"+str(tableaux[piv][0]))
    return piv

def seachFirstCL(Z, minOrMax, tableaux): # seach the value that'll come to base (index column)
    """
    [seach the first index of pivot column. That is a value that'll come to base]
    
    Arguments:
        Z {[list]} -- [list from Z line]
        minOrMax {[int]} -- [description]
        tableaux {[matrix]} -- [description]
    
    Returns:
        [int] -- [index of actual pivot column]
    """
    piv = 0
    if minOrMax == 1:
        maxI = -9999
        piv = 1
        j = 0
        for line in tableaux: # MAX: take the less absolute value from all negatives values in Z
            i = 0   
            if j < len(tableaux):
                for z_value in Z:
                    if i < len(Z)-1 and z_value < 0:
                        if i > 0:
                            if i == line[0]:
                                break
                            if abs(z_value) > maxI:
                                #check if this index already is in base
                                k = 1
                                flag = True
                                for line in tableaux:
                                    if k < len(tableaux):
                                        if line[0] == i:
                                            flag = False
                                            break                                             
                                if flag:
                                    maxI = abs(z_value)
                                    piv = i
                    i+=1
            j += 1
    elif minOrMax == 2:
        minI = -9999
        piv = 1
        j = 0
        for line in tableaux:
            i = 0   
            if j < len(tableaux):
                for z_value in Z:
                    if i < len(Z)-1 and z_value > 0:
                        if i > 0:
                            if i == line[0]:
                                break
                            if abs(z_value) > minI:
                                #verific if this index already is in base
                                k = 1
                                flag = True
                                for line in tableaux:
                                    if k < len(tableaux):
                                        if line[0] == i:
                                            flag = False
                                            break                                             
                                if flag:
                                    minI = z_value
                                    piv = i
                    i+=1
            j += 1
    print("Variavel que entra: X"+str(piv))                            
    return piv    

#verify if found the great solution or not
def conditions(Z, minOrMax, tableaux, lenBase): # break condition
    """
    [verify if already find the great solution or anothers case]
    
    Arguments:
        Z {[list]} -- [line Z]
        minOrMax {[int]} -- [<= or >=]
        tableaux {[matrix]} -- [tableau matrix]
        lenBase {[int]} -- [lenght of base]
    
    Returns:
        bool -- [it is optimal or not]
    """
    i = 0
    countZero = 0
    for z_value in Z:
        if i == 0:
            i += 1
            continue
        if z_value == 0:
            countZero += 1
        if countZero > lenBase:
            print("Infinitas soluções")
            return False
        if i == len(Z)-1: # Z value
            count = 0
            l = 0
            for var in Z:
                if var == 0 and l < len(Z)-1 and l > 0:
                    count += 1
                l+=1    
            if count > len(tableaux)-1:
                k = 1
                for line in tableaux:
                    if k < len(tableaux):
                        if line[0] != k:
                            return True     
                    k+=1  
            #print(Z)                    
            print("Solucação Otima encontrada!")                  
            return False
        if minOrMax == 1:
            if z_value < 0:
                return True
        else:    
            if z_value < 0:
                return True
        i+=1                                    

def iterations(tableaux, minOrMax, lenBase):
    """
    [execute all interarions until find the optmial solution]
    
    Arguments:
        tableaux {[matrix]} -- [matrix with all values from the all lists]
        minOrMax {[int]} -- [<= or >=]
        lenBase {[int]} -- [lenght of base]
    
    Returns:
        [float, list, list, list] -- [value resulting from Z, list of all variables in base, list of all variables in notBase,
        list from column result]
    """
    if minOrMax == 1:
        y = 0
        #multiply the Z line by -1
        for col in tableaux[-1]:
            tableaux[-1][y] = col*-1
            y+=1
    i = 0
    tam = len(tableaux[-1])# [-1] -> last line(element) from matrix
    if conditions(tableaux[-1], minOrMax, tableaux, lenBase):
        print("iteration "+str(i+1))
        _colPivot = seachFirstCL(tableaux[-1], minOrMax, tableaux) # index column that enter in the base
        _linePivot = seachFirstLN(tableaux, minOrMax, _colPivot) # index base that out from the base
        #pivoting
        tableaux[_linePivot][0] = _colPivot
        # print("_linePivot")
        # print(_linePivot)list of all variables in
        # print("_colPivot")        
        # print(_colPivot)        
        tableaux = pivoting(tableaux, _colPivot, _linePivot)
        i+=1
        while conditions(tableaux[-1], minOrMax, tableaux, lenBase): # while Z values are less than 0
            print("Iteration "+str(i+1))
            _colPivot = indexColumnPivot(tableaux[-1], minOrMax, tableaux, _colPivot) # index column that enter in the base
            _linePivot = indexLinePivot(tableaux, minOrMax, _colPivot, _linePivot) # index base that out from the base
            #pivoting
            if _linePivot == -1: #unlimited solution
                print("solucão ilimitada")
                break
            tableaux[_linePivot][0] = _colPivot
            # print("_linePivot")
            # print(_linePivot)
            # print("_colPivot")        
            # print(_colPivot)        
            tableaux = pivoting(tableaux, _colPivot, _linePivot)
            i+=1
    base = []
    result = []
    notBase = []
    i = 0
    for line in tableaux:
        if i < len(tableaux)-1:
            base.append(line[0])
            result.append(line[-1])
        i+=1

    for x in range(1,len(tableaux[0])-1):
        flag = 1
        for b in base:
            if x == b:
                flag = 0
                break
        if flag:
            notBase.append(x)

    return tableaux[-1][-1], base, notBase, result

    #base var_z_valuetriction result
    #...        ...        ...
    #...        ...        ...
    #xxx        xz1...      Z
def make_tableaux(Z,type_restrict, restrict, base, result, row, col):
    """    
    [make a tableaux matrix]
    
    Arguments:
        Z {[list]} -- [list Z values]
        type_restrict {[int]} -- [<= or >=]
        restrict {[list]} -- [list of all restrictions]
        result {[list]} -- [list of results from each restrition]
        row {[int]} -- [number of line]
        col {[int]} -- [number of coumn]
        base {[list]} -- [list of index from all variables that stay in base column]

    
    Returns:
        [type] -- [description]
    """
    tableaux_1 = []    
    z = 0
    for i in range(0,len(base)+1):
        aux = []
        r = 0
        for j in range(0,col+2):
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

#put the problem in standard form
def pattern_F(Z, type_restrict, restrict, result, row, col):
    """[summary]
    
    [addting variables to leave in pattern form]
    
    Arguments:
        Z {[list]} -- [list Z values]
        type_restrict {[int]} -- [<= or >=]
        restrict {[list]} -- [list of all restrictions]
        result {[list]} -- [list of results from each restrition]
        row {[int]} -- [number of line]
        col {[int]} -- [number of coumn]
    
    Returns:
        [lists] -- [every lists to need to make a first tableaux]
    """
    i = 0
    base = []
    sv_count = 0
    tam = len(restrict[0])
    for type_R in type_restrict:
        if type_R == 1: #add new spear var. If type == 1 then its equals to "<="
            col += 1 # att number of columns
            for j in range(0,row): # create a triangular of news vars matrix
                if j == i:
                    restrict[j].append(1)
                else:
                    restrict[j].append(0)
                Z.append(0)    
            if result[i] < 0: # negative z_valueults -> multiply all var by (-1)
                for var in restrict:
                    for var2 in var:
                        var2 = var2 * (-1)
            base.append(tam+1)
            tam += 1
        i+=1        
        type_R = "="
    return Z, restrict, result, base, col

#OBS: end='' param in print() function only work in python 3
def show(Z, type_restrict, restrict, result, row, col):
    """    
    [construct and show the functions]
    
    Arguments:
        Z {[list]} -- [list Z values]
        type_restrict {[int]} -- [<= or >=]
        restrict {[list]} -- [list of all restrictions]
        result {[list]} -- [list of results from each restrition]
        row {[int]} -- [number of line]
        col {[int]} -- [number of coumn]
    """
    print("Z = ", end='')
    aux = 1
    for x in Z:
        if aux == len(Z):
            st = str(x)+"X"+str(aux)
        else:
            st = str(x)+"X"+str(aux)+" + "
        print(st, end='')
        aux += 1    
    print("\n\nRestrições: \n")
    for i in range(0,row):
        for j in range(0,col):
            if j == col-1:
                print(str(restrict[i][j])+"X"+str(j+1), end='')
                if type_restrict[i] == 1:
                    print(" <= "+str(result[i])+"\n")
                else:
                    print(" >= "+str(result[i])+"\n")   
            else:    
                print(str(restrict[i][j])+"X"+str(j+1)+" + ", end='')

def restrict_op(row, col):
    """
    [function that capture all restriction of problem]
    
    Arguments:
        row {[int]} -- [number of lines]
        col {[int]} -- [number of columns]
    
    Returns:
        [list, int, matrix, list] -- [list of values from Z, <= or >=, matrix with all restrict values, 
        list with all results from all restricts]
    """
    var_z = []
    restricts = []
    result = []
    type_restrict = []
    for i in range(0, col):
        var_z.append(float(input("Z: informe o valor da variavel X"+str(i+1)+": ")))
    
    for i in range(0,row):
        aux = []
        for j in range(0,col):
            aux.append(float(input("Digite o coeficiente de X"+str(j+1)+" da restrição "+str(i+1)+": ")))
            if(j == col-1): 
                print("A restrição e de <=")
                type_restrict.append(1)
                result.append(float(input("Digite o resultado da restrição "+str(i+1)+": ")))
        restricts.append(aux)
    return var_z, type_restrict, restricts, result        

def minOrMax():
    """
    [which type of proble is it]
    
    Returns:
        [int] -- [1 - <=, 2 - >=]
    """
    op = 0
    while(op != 1 and op != 2):
        print("O PROBLEMA É DE:")
        print("1. Maximizacao")
        print("2. Minimizacao")
        op = int(input())
        if op != 1 and op != 2:
            print("Opcao invalida")
    return op

def main():
    """    
    [main function that is contais a loop]
    """
    while True:
        _Z_Result = 0
        print("SIMPLEX")
        row = int(input("Quantas restrições tem o problema: "))
        col = int(input("Quantas variaveis tem o problema: "))
        _type_minMax = minOrMax()
        _Z,_type_restrict, _restrict, _result = restrict_op(row, col)
        show(_Z,_type_restrict, _restrict, _result, row, col)
        #pattern form
        _Z, _restrict, _result, _base, col = pattern_F(_Z, _type_restrict, _restrict, _result, row, col)
        #construct tableaux matrix
        _tableaux = make_tableaux(_Z, _type_restrict, _restrict, _base, _result, row, col)
        _Z_Result, _base, _notBase, _result = iterations(_tableaux, _type_minMax, len(_base))
        print("Base: ")
        i = 0
        for b in _base:
            if _result[i] == 0:
                print("X"+str(b)+" = "+str(_result[i])+" ==> Solucação Degenerada!")
            else: 
                print("X"+str(b)+" = "+str(_result[i]))    
            i+=1
        print("Não basica: ")
        for nb in _notBase:
            print("X"+str(nb)+" = 0")
        print("Valor de Z: "+str(_Z_Result))
        if (int(input("Deseja continuar (1-sim, outro valor - não): ")) != 1):
            break

main()