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
    print("")               
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
    piv = 0
    if minOrMax == 1:#max
        i = 0
        maxI = 0
        for line in tableaux:
            j = 0 
            if i < len(tableaux)-1:
                for col in line:
                    if j == _colPivot:
                        if col != 0: # SPLIT TEST
                            if (line[-1]/col) >= maxI: #last column (z_valueult) div for value pivot column
                                maxI = (line[-1]/col)
                                piv = i
                    j += 1
            else:
                break        
            i += 1
    elif minOrMax == 2: #min
        i = 0
        minI = 9999
        print("len(tableaux)")
        print(len(tableaux))
        for line in tableaux:
            j = 0 
            if i != _linePivot:
                if i < len(tableaux)-1:
                    print("valor de i")
                    print(i)
                    for col in line:
                        if j == _colPivot:
                            if col > 0: #SPLIT TEST
                                if (line[-1]/col) <= minI:
                                    minI = (line[-1]/col)
                                    piv = i
                                    break
                        j += 1    
                else:
                    break    
            i += 1    
    return piv

def seachOut(tableaux, minOrMax, _colPivot): #seach index var from base that'll come out
    piv = 0
    i = 0
    if minOrMax == 1:#max
        maxI = 0
        for line in tableaux:
            j = 0 
            if i < len(tableaux)-1:
                for col in line:
                    if j == _colPivot:
                        if col != 0: # SPLIT TEST
                            if (line[-1]/col) >= maxI: #last column (z_valueult) div for value pivot column
                                maxI = (line[-1]/col)
                                piv = i
                    j += 1
            else:
                break        
            i += 1
    elif minOrMax == 2: #min
        minI = 9999
        print("len(tableaux)")
        print(len(tableaux))
        for line in tableaux:
            j = 0 
            if i < len(tableaux)-1:
                for col in line:
                    if j == _colPivot:
                        if col > 0: #SPLIT TEST
                            if (line[-1]/col) <= minI:
                                minI = (line[-1]/col)
                                piv = i
                                break
                    j += 1
                i += 1    
            else:
                break    
    return piv  

def indexColumnPivot(Z, minOrMax, tableaux, _colPivot): # seach the value that'll come to base (index column)
    piv = 0
    if minOrMax == 1:
        maxI = abs(Z[1])
        piv = 0
        j = 0
        for line in tableaux:
            i = 0   
            if j < len(tableaux):
                for z_value in Z:
                    if i < len(Z)-1:
                        if i > 0:
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
                                if flag:
                                    maxI = z_value
                                    piv = i
                    i+=1
            j += 1 
    elif minOrMax == 2:
        minI = 9999
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
                                if abs(z_value) < minI:
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

def seachIn(Z, minOrMax, tableaux): # seach the value that'll come to base (index column)
    piv = 0
    if minOrMax == 1:
        maxI = abs(Z[1])
        piv = 0
        j = 0
        for line in tableaux:
            i = 0   
            if j < len(tableaux):
                for z_value in Z:
                    if i < len(Z)-1:
                        if i > 0:
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
                                if flag:
                                    maxI = z_value
                                    piv = i
                    i+=1
            j += 1 
    elif minOrMax == 2:
        minI = abs(Z[1])
        piv = 1
        j = 0
        for line in tableaux:
            i = 0   
            if j < len(tableaux):
                for z_value in Z:
                    if i < len(Z)-1:
                        if i > 0:
                            if i == line[0]:
                                break
                            if abs(z_value) < minI:
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

def conditions(Z, minOrMax, tableaux): # break condition
    i = 0
    if minOrMax == 1:
       for z_value in Z:
            if i == 0:
                i += 1
                continue
            if i == len(Z)-1: # Z value
                k = 1
                for line in tableaux:
                    if k < len(tableaux):
                        if line[0] != k:
                            return True     
                    k+=1            
                return False
            if z_value > 0:
                return True
            i+=1                                
    elif minOrMax == 2:
        for z_value in Z:
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
                return False
            if z_value < 0:
                return True
            i+=1                                    

def iterations(tableaux, minOrMax):
    i = 0
    tam = len(tableaux[-1])# [-1] -> last line(element) from matrix
    if conditions(tableaux[-1], minOrMax, tableaux):
        print("iteration "+str(i+1))
        _colPivot = seachIn(tableaux[-1], minOrMax, tableaux) # index column that enter in the base
        _linePivot = seachOut(tableaux, minOrMax, _colPivot) # index base that out from the base
        #pivoting
        tableaux[_linePivot][0] = _colPivot
        print("_linePivot")
        print(_linePivot)
        print("_colPivot")        
        print(_colPivot)        
        tableaux = pivoting(tableaux, _colPivot, _linePivot)
        i+=1
        while conditions(tableaux[-1], minOrMax, tableaux): # while Z values are less than 0
            print("iteration "+str(i+1))
            _colPivot = indexColumnPivot(tableaux[-1], minOrMax, tableaux, _colPivot) # index column that enter in the base
            _linePivot = indexLinePivot(tableaux, minOrMax, _colPivot, _linePivot) # index base that out from the base
            #pivoting
            tableaux[_linePivot][0] = _colPivot
            print("_linePivot")
            print(_linePivot)
            print("_colPivot")        
            print(_colPivot)        
            tableaux = pivoting(tableaux, _colPivot, _linePivot)
            i+=1

def make_tableaux(Z,type_z_valuetrict, z_valuetrict, base, z_valueult, row, col):
    #base var_z_valuetriction z_valueult
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
                aux.append(z_valueult[i]) # z_valueult lines
            elif i == len(base):
                aux.append(Z[j-1])
            else:
                aux.append(z_valuetrict[i][r])
                r+=1
        tableaux_1.append(aux)   
    for x in tableaux_1:
        print(x)
    return tableaux_1

def pattern_F(Z, type_z_valuetrict, z_valuetrict, z_valueult, row, col):
    i = 0
    base = []
    sv_count = 0
    tam = len(z_valuetrict[0])
    for type_R in type_z_valuetrict:
        if type_R == 1: #add new spear var. If type == 1 then its equals to "<="
            col += 1 # att number of columns
            for j in xrange(0,row): # create a triangular of news vars matrix
                if j == i:
                    z_valuetrict[j].append(1)
                else:
                    z_valuetrict[j].append(0)
                Z.append(0)    
            if z_valueult[i] < 0: # negative z_valueults -> multiply all var by (-1)
                for var in z_valuetrict:
                    for var2 in var:
                        var2 = var2 * (-1)
            base.append(tam+1)
            tam += 1
        i+=1        
        type_R = "="
    return Z, z_valuetrict, z_valueult, base, col

def show(Z, type_z_valuetrict, z_valuetrict, z_valueult, row, col):
    print("Z = ")
    aux = 1
    for x in Z:
        print(str(x)+"X"+str(aux))
        aux += 1
    print("z_valuetrição")
    for i in xrange(0,row):
        for j in xrange(0,col):
            if j == col-1:
                print(str(z_valuetrict[i][j])+"X"+str(j+1))
                if type_z_valuetrict[i] == 1:
                    print(" <= "+str(z_valueult[i]))
                else:
                    print(" >= "+str(z_valueult[i]))   
            else:    
                print(str(z_valuetrict[i][j])+"X"+str(j+1))

def z_valuetrict_op(row, col):
    var_z = []
    z_valuetrictr = []
    z_valueult = []
    type_z_valuetrict = []
    for i in xrange(0, col):
        var_z.append(int(input("Z: informe o valor da variavel X"+str(i+1)+": ")))
    
    for i in xrange(0,row):
        aux = []
        for j in xrange(0,col):
            aux.append(int(input("Digite o coeficiente de X"+str(j+1)+" da z_valuetrição "+str(i+1)+": ")))
            if(j == col-1):   #Verifica se vai ler um coeficiente de X ou a igualdade da z_valuetrictrição
                print("A z_valuetrição e de:\n")
                print("1. <=")
                print("2. >= ? \n")
                type_z_valuetrict.append(int(input()))
                if type_z_valuetrict[i] != 1 and type_z_valuetrict[i] != 2:
                    print("Opcao invalida")
                while(type_z_valuetrict[i] != 1 and type_z_valuetrict[i] != 2):
                    print("A z_valuetrição e de:\n")
                    print("1. <=")
                    print("2. >= ? \n")
                    del type_z_valuetrict[i]
                    type_z_valuetrict[i].append(int(input()))
                    if type_z_valuetrict[i] != 1 and type_z_valuetrict[i] != 2:
                        print("Opcao invalida")       
                z_valueult.append(int(input("Digite o z_valueultado da z_valuetrição "+str(i+1)+": ")))
        z_valuetrictr.append(aux)
    return var_z, type_z_valuetrict, z_valuetrictr, z_valueult        

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
    _Z_z_valueult = 0
    print("SIMPLEX")
    row = int(input("Quantas z_valuetrições tem o problema"))
    col = int(input("Quantas variaveis tem o problema"))
    _type_minMax = minOrMax()
    _Z,_type_z_valuetrict, _z_valuetrict, _z_valueult = z_valuetrict_op(row, col)
    show(_Z,_type_z_valuetrict, _z_valuetrict, _z_valueult, row, col)
    #pattern form
    _Z, _z_valuetrict, _z_valueult, _base, col = pattern_F(_Z, _type_z_valuetrict, _z_valuetrict, _z_valueult, row, col)
    #construct tableaux matrix
    _tableaux = make_tableaux(_Z, _type_z_valuetrict, _z_valuetrict, _base, _z_valueult, row, col)
    _Z_z_valueult = iterations(_tableaux, _type_minMax)

main()