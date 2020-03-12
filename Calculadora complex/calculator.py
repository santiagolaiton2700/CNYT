from sys import stdin
import math

def suma(a,b):
    reala=a[0]
    realb=b[0]
    imaa=a[1]
    imab=b[1]
    sumar = reala+realb
    sumai= imaa+imab
    fin=(sumar,sumai)
    return fin

def resta (a,b):
    reala=a[0]
    realb=b[0]
    imaa=a[1]
    imab=b[1]
    restarr = reala-realb
    restari= imaa-imab
    fin=(restarr,restari)
    return fin

def multi(a,b):
    reala=a[0]
    realb=b[0]
    imaa=a[1]
    imab=b[1]
    parte1a  = reala*realb 
    parte2a  = imaa*imab
    parte3b  = reala*imab
    parte4b  = realb*imaa
    fin=(parte1a-parte2a,parte3b+parte4b)
    return fin

def division(a,b):
    reala=a[0]
    realb=b[0]
    imaa=a[1]
    imab=b[1]
    fin=((reala*realb+imaa*imab)/(realb**2+imab**2),(realb*imaa-reala*imab)/(realb**2+imab**2))
    return fin

def conjugado(a):
    x,y=a[0],a[1]
    fin=(float(x),float(y*-1))
    return fin

def modulo(a):
    b=int(a[0])
    c=int(a[1])
    fin=(b**2+c**2)**0.5
    return round(fin,2)
def moduloVectorial(vector):
    answer=0
    for i in vector:
        answer+=modulo(i)
    return round(answer,2)

def polar_a_cartesiano(a):
    hipotenusa=a[0]
    teta=a[1]*(math.pi/180)
    return (hipotenusa*math.cos(teta),hipotenusa*math.sin(teta))

def cartesiano_a_polar(a):
    teta=math.atan2(a[1],a[0])
    return((a[0]**2+a[1]**2)**5,teta*(180/math.pi))

def fase(a):
    return math.atan2(a[1],a[0])

def adicionVectorial(a,b):
    if len(a) != len(b):
        raise 'La suma entre estos 2 vectores no esta definida'
    answer = []
    for i in range(len(a)):
        answer.append(suma(a[i],b[i]))
    return answer

def inversa_vector(a):
    for x in range(len(a)):
        a[x] = (a[x][0]*-1,a[x][1]*-1)
    return a

def multiplicaionVectorEscalar(vector,escalar):
    temp=[]
    for i in range(len(vector)):
        temp.append(multi(vector[i],(escalar,0)))
    return temp

def suma_matrices_complejos(matriz1,matriz2):
    if len(matriz1)!=len(matriz2) or len(matriz1[0])!=len(matriz2):
        raise "La suma no se puede realizar por que las matrices debe ser de la misma dimension"
    else:
        final=[]
        for i in range (len(matriz1)):
            tempo=[]
            for j in range (len(matriz2)):
                sumado=suma(matriz1[i][j],matriz2[i][j])
                tempo.append(sumado)
            final.append(tempo)
        return final
def matriz_inversa(matriz):
    final=[]
    for i in range (len(matriz)):
        tempo=[]
        inverso=inversa_vector(matriz[i])
        final.append(inverso)
    return final


def multiplicacion_matriz_Escalar(matriz,escalar):
    final=[]
    for i in range (len(matriz)):
        inversa=multiplicaionVectorEscalar(matriz[i],escalar)
        final.append(inversa)
    return final
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
                    multi=multiplicacion_vectores(a[x][z],c[z][y])
                    nu=nueva[x][y]
                    nueva[x][y]=(multi[0]+nu[0],multi[1]+nu[1])
        return nueva
    else:
        return false

def matriz_conjugada(matriz):
    final=[]
    for i in range(len(matriz)):
        tempo=[]
        for j in range(len(matriz[0])):
            respuesta=conjugado(matriz[i][j])
            tempo.append(respuesta)
        final.append(tempo)
    return final
def vector_conjugado(vector):
    final=[]
    for k in vector:
        answer=conjugado(k)
        final.append(answer)
    return final
def matriz_transpuesta(matriz):
    transpuesta=[None]*len(matriz[0])
    for i in range(len(matriz)):
        transpuesta[i]=[None]*len(matriz)
        for j in range(len(matriz[i])):    
            transpuesta[i][j]=matriz[j][i]
    return transpuesta
def vector_transpuesto(vector):
    return vector
def matriz_adjunta(matriz):
    a=matriz_conjugada(matriz)
    b=matriz_transpuesta(a)
    return b
def vector_adjunto(vector):
    a=vector_conjugado(vector)
    b=vector_transpuesto(a)
    return b
def multiplicacion_matrices(m1,m2):
    final=[]
    if len(m1)==len(m2):
        for a in range(len(m1)):
            answer=[]
            for b in range(len(m2[0])):
                enviar=(0,0)
                for c in range(len(m2)):
                    enviar=suma(enviar,multi(m1[a][c],m2[c][b]))
                answer.append(enviar)
            final.append(answer)
        return final
    else:
         raise 'La longitud de las dos matrices no son iguales'
def multiplicacion_vectores(vect1,vect2):
    respuesta=[]
    if len(vect1)==len(vect2):
        final=(0,0)
        for i in range(len(vect1)):
            final=suma(final,multi(vect1[i],vect2[i]))
        return final
    else:
        raise 'La longitud de los dos vectores no son iguales'
def producto_interno_vectores(vector1,vector2):
    a=vector_conjugado(vector1)
    b=multiplicacion_vectores(a,vector2)
    return b
def matriz_normal(matriz):
    real=0
    ima=0
    for i in range(len(matriz)):
        caso1=matriz[i][0]
        real +=math.pow(caso1[0],2)
        ima +=math.pow(caso1[1],2)
    return ((math.sqrt(real)),(math.sqrt(ima)))
def matriz_hermitian(matriz):
    if len(matriz) != len(matriz[0]):  raise 'La matriz no es cuadrada'
    else:
        return matriz == matriz_adjunta(matriz)    
def tensorVector(vector1,vector2):
    fin=[]
    for x in range(len(vector1)):
        tempo=[]
        for y in range(len(vector2)):
            tempo.append(multi(vector1[x],vector2[y]))
        fin.append(tempo)
    return fin
def distancia_vectorial(vector1,vector2):
    real=(vector1[0]-vector2[0])**2
    imaginaria=(vector1[1]-vector2[1])**2
    respuesta=(real+imaginaria)**0.5
    return respuesta
def unitaria(matriz1):
    adjunta=matriz_adjunta(matriz1)
    multiplicada=multiplicacion_matrices(matriz1,adjunta)
    for i in range(len(matriz1)):
        for k in range(len(matriz1)):
            estado=multiplicada[i][k]
            if i==k and (estado[0]!=1 or posicion[1]!=0):
                return False
            elif(i!=k and (estado[0]!=0 or estado[1]!=0)):
                return False
    return True

def tensorMatrices(mat1,mat2):
    fin=[]
    for i in range(len(mat1)):
        for j in range(len(mat2)):
             fin.append(tensorVector(mat1[i],mat2[j]))
    return fin

###########Ejercicio lineal#############################
def probabilidad(h,vector):
    modul=modulo(vector[h])
    moduloVec=moduloVectorial(vector)
    proba=(modul/moduloVec)*100
    return round(proba,0)
def transicion(vector1,vector2):
    conju=vector_adjunto(vector2)
    answer=multiplicacion_vectores(conju,vector1)
    return answer
