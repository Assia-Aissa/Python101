import math
## Exercidce 1 avec math library
#log2(n)=x alors : 2^x=n
def Logarithme_binaire_with_lib(n):
    if n > 0 :
        return round(math.log2(n))
    else :
        return 


def logarithme_binaire_withourt_lib(n):
    cpt=0
    while n >1:
        n=n//2
        cpt +=1
    return cpt 

r=logarithme_binaire_withourt_lib(10)
print(r)
b=Logarithme_binaire_with_lib(10)
print(b)
######################################################################
#Exerice 2 
#Une Suite de Syracuse connue sous le nom de *conjecture de collatz* *suite de hailstone*
def Syracuse(n,N):
    if N==1:
        print(f"U({n})={N}")
        return N
    else:
        print(f"U({n})={N}")
        if N % 2==0:
            return Syracuse(n+1,N//2)
        else:
            return Syracuse(n+1,3*N+1)
        
Syracuse(3,6)

##########################################################################
#exercice 3 factoriel
def Factoriel(N):
    if N==1 or N==0:
        return 1
    else:
        return N*Factoriel(N-1)
b=3  
a = Factoriel(3)
print(f"factoriel of {b} is {a}")

##########################################################################
#exercice 4 nombre Premier

def est_Premier(a):
    if a==0 or a==1:
        return False
    if a % 2==0:
        return False
    for i in range(3,int(a**0.5)+1,2):
        if a % i==0:
            return False
        
    return True

n= est_Premier(6)
print(f" nombre est premier ? {n}")

###################################################
# exercice 5
def est_parfait(a):
    dev=0
    for i in range(1,a):
        if a% i ==0:
            dev +=i
    if dev== a:
        return True
    else:
        return False

print(f"le nombre parfait est :{est_parfait(6)}")

####################################33333333333333333333333333333333
#exercice 6
# caree parfait : means that : x^2 =y and also x*x=y
def est_carre_parfait(a):
    if a**2 ==a*a :
        return True 
    else :
        return False

print(f"{est_carre_parfait(4)}")
###################################################3
# exercice 7  suite recurrente
def Suite_recurrente(n):
    if n==0:
         return 1
    elif n==2:
         return 2
    M0=1
    M1=2
    for i in range(2,n+1):
        Mn=M1+6*M0
        M0 , M1= M1,Mn
    return Mn
####################################################
#exercice 8:
def calcule(n,p):
    return n**p

#############################################3
#exercice 9
def Input_Output():
    N=input("enter number: ")
    return N

##########################3333
#exercice 10:
# la methode de dichotomie de f(x)=0 avec TVI 
def f(x):
    return x**3-2*x+1
def dichtomie(f,a,b,n):
    if f(a)*f(b) >=0:
        return None
    while (b-a)/2 >n :
        c=(a+b) / 2
        if f(c)==0:
            return c
        elif (c) * f(a) <0:
             b=c
        else :
             a=c
    return (a+b)/2

a=1
b=2
tol=1e-6
racine = dichtomie(f,a,b,tol)
if racine is not None:
    print(f"--------> {racine}")

#############################################################
#exercice11
#development limite de fonction f(x)=exp(x)
def factoriel(n):
    if n==0 or n==1:
        return 1
    else :
        return n*factoriel(n-1)
def exp(x,n):
    ex=0
    for i in range(0,n+1):
        ex += x**i /factoriel(i)
    return ex
x=2
n=10
print(f"exp({x} with order of {n} is :{round(exp(x,n))}")




##################################3
#exercice 12 : integrale :
# define the function f(x)
def function(x):
    return math.exp(-x**2)

#method of trapezoidal rule  I = (b-a/n) *(f(a)+2 sigma(i=1 -> n-1)f(x(i)+ f(b))
def trapezoidal(a,b,n):
    h= b-a/n
    I = 0.5 * (function(a) +function(b))
    for i in range (1, n):
        x = a + i *h
        I += function(x)
    I *= h
    return I

e=0
d=1
m=1000
approximation= trapezoidal(e,d,m)

print(f"pproximate integer of exp  from a et b :{approximation}")



##########################33333333333
# number 13
def somme (n):
    s=0
    for i in range(0,n+1):
        s += (2*i +1)**3
    return s

###################################
#exercice 14
def DIVESEUR(n):
    for i in range(n-1,1,-1):
        if n % i ==0:
            return i
    return -1
print(f"------->{DIVESEUR(100)}")
#####################################33
#exercice 15
def est_premier(p):
    if p<2:
        return False
    for i in range (2, int(p**0.5)+1):
        if p % i ==0:
            return False
    return True
def PlusGrandDivPrem(n):
    if n==1:
        return 1
    for i in range(n,1,-1):
        if n % i == 0 and est_premier(i):
            return i
    return 1
print(f"--> {PlusGrandDivPrem(100)}")


############################3333
def Factoriser(n):
    List_premier=[]
    for i in range (1,n):
        if est_premier(i) and  n %i ==0:
            List_premier.append(i)
            n//=i
    return List_premier
#still the problem of i can't se the same n;umber more than one 
def afficher(n):
    a=Factoriser(n)  
    print(f"{n} =" ,end="")
    for i in a :
        print(f"{i}*", end="")
    print()
z=30
afficher(z)

def est_mechant(n):
    if n <= 0:
        return "c'est pas un nombre mechant :)"
    for i in [2,3,5]:
        while n% i==0:
            n//=i
    if n==1: 
        return "yes nombre mechant "
    else :
        return "c'est pas un nombre mechant :)"
n=int (input ("enter a number : "))
print(est_mechant(n))
