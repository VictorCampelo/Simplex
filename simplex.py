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

def indexLinePivot(tableaux, minOrMax, _colPivot, _linePivot): #seach index var from base that'll come out
    piv = -1
    if minOrMax == 1:#max
        print("new column pivot: "+str(_colPivot))
        print("debug 3")
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
                        if j == _colPivot and col > 0 and (float(line[-1])/float(col)) <= minI:
                                minI = (float(line[-1])/float(col))
                                piv = i
                        j += 1     
            i += 1    
    return piv

def indexColumnPivot(Z, minOrMax, tableaux, _colPivot): # seach the value that'll come to base (index column)
    piv = 0
    if minOrMax == 1:
        maxI = 9999
        piv = 0
        j = 0
        for line in tableaux:
            i = 0   
            if j < len(tableaux):
                for z_value in Z:
                    if i < len(Z)-1: # dont take result column
                        if i > 0: # dont take base column
                            if i != _colPivot: # 
                                if i == line[0]:
                                    break
                                if abs(z_value) < maxI:
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
                                        maxI = z_value
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
                                if z_value > minI:
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
    return piv  

def seachFirstLN(tableaux, minOrMax, _colPivot): #seach index var from base that'll come out
    piv = 0
    if minOrMax == 1: #max
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
    elif minOrMax == 2: #min
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
    return piv      

def seachFirstCL(Z, minOrMax, tableaux): # seach the value that'll come to base (index column)
    piv = 0
    if minOrMax == 1:
        maxI = 9999
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
                            if abs(z_value) < maxI:
                                #check if this index already is in base
                                k = 1
                                flag = True
                                for line in tableaux:
                                    if k < len(tableaux):
                                        if line[0] == i:
                                            flag = False
                                            break                                             
                                if flag:
                                    maxI = z_value
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
                            if z_value > minI:
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
    return piv    

def conditions(Z, minOrMax, tableaux, lenBase): # break condition
    i = 0
    countZero = 0
    for z_value in Z:
        if z_value == 0:
            countZero += 1
        if countZero >= lenBase:
            print("Infinitas soluções")
            return False
        if i == 0:
            i += 1
            continue
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
            print(Z)                    
            print("Solucação Otima encontrada!")                  
            return False
        if minOrMax == 1:
            if z_value < 0:
                return True
        else:    
            if z_value > 0:
                return True
        i+=1                                    

def iterations(tableaux, minOrMax, lenBase):
    y = 0
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
        print("_linePivot")
        print(_linePivot)
        print("_colPivot")        
        print(_colPivot)        
        tableaux = pivoting(tableaux, _colPivot, _linePivot)
        i+=1
        while conditions(tableaux[-1], minOrMax, tableaux, lenBase): # while Z values are less than 0
            print("iteration "+str(i+1))
            _colPivot = indexColumnPivot(tableaux[-1], minOrMax, tableaux, _colPivot) # index column that enter in the base
            _linePivot = indexLinePivot(tableaux, minOrMax, _colPivot, _linePivot) # index base that out from the base
            #pivoting
            if _linePivot == -1: #unlimited solution
                print("solucão ilimitada")
                break
            tableaux[_linePivot][0] = _colPivot
            print("_linePivot")
            print(_linePivot)
            print("_colPivot")        
            print(_colPivot)        
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

def make_tableaux(Z,type_restrict, restrict, base, result, row, col):
    #base var_z_valuetriction result
    #...        ...        ...
    #...        ...        ...
    #xxx        xz1...      Z
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

def z_valuetrict_op(row, col):
    var_z = []
    z_valuetrictr = []
    result = []
    type_restrict = []
    for i in range(0, col):
        var_z.append(int(input("Z: informe o valor da variavel X"+str(i+1)+": ")))
    
    for i in range(0,row):
        aux = []
        for j in range(0,col):
            aux.append(int(input("Digite o coeficiente de X"+str(j+1)+" da restrição "+str(i+1)+": ")))
            if(j == col-1):   #Verifica se vai ler um coeficiente de X ou a igualdade da z_valuetrictrição
                print("A restrição e de: ")
                print("1. <=")
                #print("2. >= ? : ")
                #type_restrict.append(int(input()))
                type_restrict.append(1)
                # if type_restrict[i] != 1 and type_restrict[i] != 2:
                #     print("Opcao invalida")
                # while(type_restrict[i] != 1 and type_restrict[i] != 2):
                #     print("A restrição e de:")
                #     print("1. <=")
                #     print("2. >= ? :  ")
                #     del type_restrict[i]
                #     type_restrict.append(int(input()))
                #     if type_restrict[i] != 1 and type_restrict[i] != 2:
                #         print("Opcao invalida")       
                result.append(int(input("Digite o resultado da restrição "+str(i+1)+": ")))
        z_valuetrictr.append(aux)
    return var_z, type_restrict, z_valuetrictr, result        

def minOrMax():
    print("O problema e de:")
    print("1. Maximizacao")
    print("2. Minimizacao")
    print("? ")
    op = int(input())
    if op != 1 and op != 2:
        print("Opcao invalida \n")

    while(op != 1 and op != 2):
        print("O problema e de:")
        print("1. Maximizacao")
        print("2. Minimizacao")
        print("? ")
        op = int(input())
        if op != 1 and op != 2:
            print("Opcao invalida")
    return op

def main():
    while True:
        _Z_Result = 0
        print("SIMPLEX")
        row = int(input("Quantas restrições tem o problema: "))
        col = int(input("Quantas variaveis tem o problema: "))
        _type_minMax = minOrMax()
        _Z,_type_restrict, _restrict, _result = z_valuetrict_op(row, col)
        show(_Z,_type_restrict, _restrict, _result, row, col)
        #pattern form
        _Z, _restrict, _result, _base, col = pattern_F(_Z, _type_restrict, _restrict, _result, row, col)
        #construct tableaux matrix
        _tableaux = make_tableaux(_Z, _type_restrict, _restrict, _base, _result, row, col)
        _Z_Result, _base, _notBase, _result = iterations(_tableaux, _type_minMax, len(_base))
        print("Base: ")
        i = 0
        for b in _base:
            print("X"+str(b)+" = "+str(_result[i]))
            i+=1
        print("Não basica: ")
        for nb in _notBase:
            print("X"+str(nb)+" = 0")
        print("Valor de Z: "+str(_Z_Result))    
        "Deseja Sair(1-sim, 2-não): "
        if (int(input("Deseja continuar (1-sim, outro valor - não): ")) != 1):
            break

main()