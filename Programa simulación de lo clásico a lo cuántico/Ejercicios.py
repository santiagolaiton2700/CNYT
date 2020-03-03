#from numpy import linalg
"----------------Ejercicio1---------------------------------------"
def multiplicacion(vector1,vector2):
    real1=vector1[0]
    real2=vector2[0]
    ima1=vector1[0]
    ima2=vector2[0]
    real=(real1*real2)-(ima1*ima2)
    ima=(ima1*real1)+(ima2*real1)
    respuesta=(real,ima)
    return respuesta

def tensorMatrices(matriz1,matriz2):
    row1=len(matriz1)
    columnas1=len(matriz1[0])
    row2=len(matriz2)
    columns2=len(matriz2[0])
    for x in range (row2):
        for y in range(columns2):
            nueva=[]
            for z in range(row2):
                for j in range(columns2):
                    nueva.append(multiplicacion(matriz1[x][y],matriz2[x][y]))
                matriz1[x][y]=nueva
    return matriz1
def vectorMatriz(a,c):
    rowC=len(c)
    columnsL=len(a[0])
    if rowC==columnsL:
        rows=len(a)
        columns=len(b[0])
        nueva=[[(0, 0)] * columns for x in range(rows)]
        for x in range(rows):
            for y in range(columns):
                for z in range(len(c)):
                    multi=multiplicacion(a[x][z],c[z][y])
                    nu=nueva[x][y]
                    nueva[x][y]=(multi[0]+nu[0],multi[1]+nu[1])
        return nueva
    else:
        return false
def multiplicacionMatriz(matriz1,matriz2):
    rows2=len(matriz2)
    columns1=len(matriz1[0])
    if rows2==columns1:
        rows=len(matriz1)
        columns=len(matriz2[0])
        nueva=[[(0, 0)] * columns for x in range(rows)]
        for x in range(rows):
            for y in range(columns):
                for z in range(len(matriz2)):
                    multi=multiplicacion(matriz1[x][z],matriz2[z][y])
                    nu=matriz[x][y]
                    nueva[x][y]=(multi[0]+nu[0],multi[1]+nu[1])                    
        return nueva 
    else:
        raise "La dimension de las matrices son incorrectas"    
def modulo(a):
    b=int(a[0])
    c=int(a[1])
    fin=(b**2+c**2)**0.5
    return fin
def multi(tupla1,tupla2):
    a1,b1,a2,b2 = tupla1[0],tupla1[1],tupla2[0],tupla2[1]
    return (float((a1*a2)-(b1*b2)),float((a1*b2)+(a2*b1)))
def multiplicacion_matrices(A,B):
    rowB = len(B)
    columnA = len(A[0])
    if rowB == columnA:
        rows = len(A)
        columns = len(B[0])
        matriz = [[(0, 0)] * columns for x in range(rows)]
        for i in range(0, rows):
            for j in range(0, columns):
                for k in range(0, len(B)):
                    multi = multiplicacion(A[i][k], B[k][j])
                    nu = matriz[i][j]
                    matriz[i][j] = (multi[0]+nu[0], multi[1]+nu[1])
        return matriz
    else:        
        raise 'La longitud de las matriz son diferentes'
    
def accion_matriz_vector(matriz, vector):    
    if len(matriz[0]) != len(matriz) != len(vector):
        raise 'Operacion no definida'
    else:
        accion = []
        for fila in matriz:
            accion.append(producto_punto(fila, vector))
        return accion
    
def matriz_transpuesta(matriz):
    rows = len(matriz)
    columns = len(matriz[0])
    return [[matriz[j][i] for j in range(rows)] for i in range(columns)]
            
def canicas(a,b,c):
    n=a
    while b!=0:
        f=multiplicacion_matrices(n,a)
        n=f
        b=b-1
    return multiplicacion_matrices(n,matriz_transpuesta(c))

def balas(a,b,c):
    n=a
    while b!=0:
        f=multiplicacion_matrices(n,a)
        n=f
        b=b-1
    return multiplicacion_matrices(n,matriz_transpuesta(c))

def dinamica(sistema,inicial,clicks):
    for x in range(clicks):
        inicial=accion_matriz_vector(sistema,inicial)
    return inicial

def dobleRendija(a,clicks):
    "Doble rendija"
    for x in range(len(a)):
        for y in range(len(a[0])):
            for k in range(clicks):
                a[x][y] = multi(a[x][y],a[x][y])
            a[x][y] = modulo(a[x][y])
    return a

def flash(a,b):
    n=a
    while b!=0:
        respuesta=multiplicacion_matrices(n,a)
        n=respuesta
        b=b-1
    f=a
    for x in range(len(a)):
        for y in range(len(a[0])):
            mu=((a[x][y][0]**2)+(a[x][y][1]**2))**0.5
            f[x][y]=mu
    return f
def multiples_rendijas(rendijas, blancos_pared, vector_probabilidad):
    paredes = rendijas + 1
    nodos = 2 * rendijas + paredes * blancos_pared + 1
    blancos_rendija = len(vector_probabilidad)
    sistema = [[(0, 0) for j in range(nodos)]for i in range(nodos)]
    posicion = 0
    for i in range(1, rendijas + 1):
        sistema[i][0][0] = 1/(rendijas**(1/2))
        posicion = i
    for i in range(1, num_rendijas + 1):
        for j in range(posicion, posicion + blancos_rendija + 1):
            sistema[j][i] = vector_probabilidad[i-1]                
    return sistema
"---------------------------------Ejercicio2------------------------------"
def egval(expresion):
    a=complex(expresion[0],expresion[1])
    return a
def prube(expresion):
    a=expresion[0]-0.1
    b=expresion[1]
    if b>0:
        b=b-0.1
    return (a,b)

def vectorComplex(vector):
    tempo=0
    for i in range(len(vector)):
        tempo=tempo+(vector[i][0]**2+vector[i][1]**2)

    return round((tempo**0.5),3)
def conjugado(a):
    rows=len(a)
    columns=len(a[0])
    for x in range(rows):
        for y in range(columns):
            b=a[i][j]
            c=b[0]
            d=b[1]*-1
            e=(c,d)
            a[x][y]=e
    return A
def simplificacion(a, b):
    R = [[(0, 0)] * len(a) for x in range(len(a))]
    for i in range(len(a)):
        for j in range(len(b)):
            R[i][j] = (a[i][j][0] - b[i][j][0], a[i][j][1] - b[i][j][1])
    return R

def hermitian(matriz):
    rows=len(a)
    columns=len(a[0])
    if rows==columns:
        transpuesta=matriz_transpuesta(matriz)
        conju=conjugado(transpuesta)
        if transpuesta==matriz:
            return True
        else:
            return False
    else:
        return False

def particle(vector):
    j = 1
    normal= vectorComplex(vector)
    proba = (j/(normal**2))
    return round(proba, 6)


def normalize(vector):
    j = 1
    norm = vectorComplex(vector)
    nueva = [[]]
    for i in range(len(vector)):
        operacion1 = (1/norm) * vector[j][0]
        operacion2 = (1/norm) * vector[j][1]
        nueva[0].append((round(operacion1, 5), round(operacion2, 5)))
    return nueva


def spin(vector):
    norm = vectorComplex(vector)**2
    arriba = vector[0][0]**2 + vector[0][1]**2
    abajo = vector[1][0]**2 + vector[1][1]**2
    operacion1 = round((arriba/norm), 2)
    operacion2 = round((abajo/norm), 2)
    respuesta = (operacion1, operacion2)
    return respuesta


def ident(c, Matriz):
    Respuesta = [[(0, 0)] * len(Matriz) for x in range(len(Matriz))]
    for x in range(len(Matriz)):
        for y in range(len(Matriz)):
            if x == y:
                Respuesta[x][y] = (c, 0)
    return Respuesta

"--------------Ejercicio3-------------------------------------------"

def inner_product(vector1, vector2):
    if len(vector1) == len(vector2):
        cont = (0, 0)
        for i in range(len(vector1)):
            multi = multiplicacion(vector1[i], vector2[i])
            nu= (cont[0]+multi[0], cont[1]+multi[1])
            cont = nu
        return cont
    else:
        return False
def amplitudeKet(nu1, nu2, k1, k2):
    k3 = k2
    r1 = inner_product(nu1, k1)
    r2 = inner_product(nu2, k2)
    return inner_product(r1, r2)

def proba(h, ket):
    r = vectorComplex(ket)
    x = ket[h]
    y = x
    sum_1 = multiplicacion(x, y)
    sum_2 = abs(sum_1[0] + sum_1[1])
    pro = sum_2/(r ** 2)
    return pro
def variance(M, v):
    if len(M) == len(v[0]):
        H = multiplicacion_matrices(M, matriz_transpuesta(v))
        w = [[]]
        for j in H:
            w[0].append(j[0])
        x = multiplicacion_matrices(matriz_transpuesta(w), v)
        E = x[0][0][0] + x[1][0][1]
        m1 = ident(E, M)
        N = simplificacion(M, m1)
        Delta = multiplicacion_matrices(N, N)
        r = v
        for i in range(len(v)):
            for j in range(len(v[0])):
                x = v[i][j]
                c = x[0] ** 2
                t = x[1] ** 2
                r[i][j] = (c, t)
        Rf = multiplicacion_matrices(r, Delta)
        x = prube(Rf[0][0])
        return round(x[0], 2)
    else:
        return False
##def eigenstates(ob, v):
##    ob1 = []
##    for i in range(len(ob)):
##        ob1.append([])
##        for j in range(len(ob[0])):
##            ob1[i].append(ob[i][j])
##    for i in range(len(ob1)):
##        for j in range(len(ob1[0])):
##            ob1[i][j] = egval(ob1[i][j])
##    N = list(linalg.eig(ob1)[0])
##    y = variance(ob, v)
##    return N, y
