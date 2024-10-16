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

n= est_Premier(5)
print(f"{n}")


    




