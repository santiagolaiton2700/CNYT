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


