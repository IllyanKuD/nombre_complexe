from math import * 

a=float (input("valeur de a"))
b=float(input("valeur de b"))
pi=3,14159
def affichage_nc(a,b):
    print(str(a)+"+"+str(b)+"i")

def module(a,b):
    return sqrt((a**2)+(b**2))

def argu(a,b):
    result=atan2(b,a)
    print(result)
    print(type(result))
    a=result/3.14159265358979323846264338327950288419716939937510
    return a

def forme_trigo(a,b):
    mod=module(a,b)
    trig=argu(a,b)
    final=("Z="+str(mod)+"("+"cos"+"("+str(trig)+")"+"i("+"sin("+str(trig)+"))")
    print(final)


def test():
    affichage_nc(a,b)
    forme_trigo(a,b)
    
test()

