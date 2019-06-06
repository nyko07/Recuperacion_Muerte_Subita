from functools import reduce

#Ejercicio 1
lista = [[29,15,12],[4,5,6],[7,8,9]]
mapear = map(lambda x: [x[0],x[-1]],lista)
print(mapear)


#Ejercicio 2
lisNum2 = [13,24,36,4,5,6,7,8,9]
def suPares(num):
    estado = True
    textNum = str(num)
    for d in textNum:
        if int(d) % 2 != 0:
            estado = estado and False
    return estado

mapear2 = filter(lambda x:suPares(x),lisNum2)
print(mapear2)


#Ejercicio 3
maxMap = map(lambda x: max(x),lista)
print(maxMap)


#Ejercicio 4
def minSuperpar(lista):
    aux = []
    for ele in lista:
        if suPares(ele):
            aux.append(ele)
    return min(aux)
lisNum3 = [[2,4,778,895,22,44],[21,4,7784,895,22,448],[1,33,45,82,88,25]]
mapeo4 = map(lambda x: minSuperpar(x),lisNum3)
print(mapeo4)


#Ejercicio 5
lisNum3 = [2,2,3,4,5555,6,7,8,9]
filtro = filter(lambda x: x < lisNum3[0]**5,lisNum3)
print(filtro)


#Ejercicio 6
lisTuplas = [[6,3],[10,4],[2,78],[98,34]]
def numTrangular (num):
    trian = 0
    for i in range(0,num+1):
        trian = trian + i
    return trian

filtroTri = filter(lambda x: x[0] == numTrangular(x[1]),lisTuplas)
mapTri = reduce(lambda x,y: x[0]+y[0],filtroTri)
print(mapTri)