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
    return fin

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

def matriz_conjugada(matriz):
    final=[]
    for i in range(len(matriz)):
        tempo=[]
        for j in range(len(matriz[0])):
            respuesta=conjugado(matriz[i][j])
            tempo.append(respuesta)
        final.append(tempo)
    return final
def matriz_transpuesta(matriz):
    transpuesta=[None]*len(matriz[0])
    for i in range(len(matriz)):
        transpuesta[i]=[None]*len(matriz)
        for j in range(len(matriz[i])):    
            transpuesta[i][j]=matriz[j][i]
    return transpuesta
                         
def matriz_adjunta(matriz):
    a=matriz_conjugada(matriz)
    b=matriz_transpuesta(a)
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

def tensorMatrices(mat1,mat2):
    fin=[]
    for i in range(len(mat1)):
        for j in range(len(mat2)):
             fin.append(tensorVector(mat1[i],mat2[j]))
    for k in fin:
        print(k)

escalar=1/2**(1/2)
matriz=[[(1,0),(1,0)],[(1,0),(-1,0)]]
x=[[(0,0),(1,0)],[(1,0),(0,0)]]
H=multiplicacion_matriz_Escalar(matriz,escalar)
print("HH producto tensor")
M2=tensorMatrices(H,H)










