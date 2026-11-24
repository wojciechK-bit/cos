
from math import pi

def pp_kwadratu(a:float)->float:
    return a**2

def pp_porstokata(a:float, b:float)->float:
    return a*b

def pp_rownolegloboku(a:float, h:float)->float:
    return a*h

def pptrapezu(a:float, b:float,h:float)->float:
    return (a+b)/h

def pp_trojkata(a:float,h:float)->float:
    return (a*h)/2

def pp_romba(a:float,h:float):
    return a*h
def pp_kola(r:float)->float:
    return pi*r**2

def legenda_pp()->None:
    print("a -- pp_kwadratu")
    print("b -- pp_porstokata")
    print("c---- pp_rownolegloboku ")
    print("d--- pptrapezu")
    print("e---pp_trojkata ")
    print("h--- pp_romba")
    print("f-- pp_kola")
    print("q -- Exsit")


def jakie_pp()->None:
    while True:
        legenda_pp()
        inp = input().lower().strip()
        if inp == "q":
            print("Exsit")
            break
        elif inp == "a":
            a = float(input("a = "))
            print(f"dla {a} pp_kwadratu = {pp_kwadratu(a)}")
        elif inp == "b": 
            a = float(input("a = "))
            b = float(input("b = "))
            print(f"dla {a} {b} pp_porstokata = {pp_porstokata(a,b)}")
        elif inp== "c":
            a=float(input("a="))
            h=float(input("h="))
            print(f"dla {a} {h} pp_rownolegloboku = {pp_rownolegloboku(a,h)}")
        elif inp=="d":
            a=float(input("a="))
            b=float(input("b="))
            h=float(input("h="))
            print(f"dla {a} {b}{h} pptrapezu = {pptrapezu(a,b,h)}")
        elif inp == "e":
            a=float(input("a="))
            h=float(input("h="))
            print(f"dla {a} {h} pp_trojkata={pp_trojkata(a,h)}")
        elif inp =="h":
            a=float(input("a="))
            h=float(input("h="))
            print(f"dla {a} {h} pp_romba={pp_romba(a,h)}")
        elif inp=="f":
            r=float(input("r="))
            print(f"dla {r} pp_kola={pp_kola(r)}")
            


            

# ------------------------------------------------------------------------------
def obw_kwadaru(a:float)->float:
    return 4*a

def obw_prostokata(a:float, b:float)->float:
    return 2*a+2*b

def obw_rownologloboku(a:float,b:float)->float:
    return 2*a+2*b

def obw_trapezu(a:float,b:float,c:float,d:float)->float:
    return a+b+c+d

def obw_trojkota(a:float,b:float,c:float)->float:
    return a+b+c

def obw_trojkata_rownobocznego(a:float)->float:
    return 3*a

def obw_rombu(a:float)->float:
    return 4*a

def obw_kola(r:float)->float:
    return 2*pi*r


def legenda_obw()->None:
    print("a -- obw_kwadaru")
    print("b -- obw_prostokata")
    print("c--- obw_rownologloboku ")
    print("d --- obw_trapezu")
    print("e--- obw_trojkota")
    print("f--- obw_trojkata_rownobocznego")
    print("g--- obw_rombu")
    print("h--- obw_kola")
    print("q -- zkoncz program")

def jakie_obw()->None:
    while True:
        legenda_obw()
        inp = input().lower().strip()
        if inp == "q":
            print("Exsit")
            break
        elif inp == "a":
            a=float(input("a="))
            print(f"dla {a} obw_kwadaru ={obw_kwadaru(a)}")
        elif inp=="b":
            a=float(input("a="))
            b=float(input("b="))
            print(f"dla {a} {b} obw_prostokata={obw_prostokata(a,b)}")
        elif inp=="c":
            a=float(input("a="))
            b=float(input("b="))
            print(f"dla {a} {b} obw_rownologloboku={obw_rownologloboku(a,b)}")
        elif inp=="d":
            a=float(input("a="))
            b=float(input("b="))
            c=float(input("c="))
            d=float(input("d="))
            print(f"dla {a} {b} {c} {d} obw_rownologloboku={obw_trapezu(a,b,c,d)}")
        elif inp=="e":
            a=float(input("a="))
            b=float(input("b="))
            c=float(input("c="))
            print(f"dla {a} {b} {c} obw_prostokata={obw_prostokata(a,b,c)}")
        elif inp == "f":
            a=float(input("a="))
            print(f"dla {a} obw_trojkata_rownobocznego ={obw_trojkata_rownobocznego(a)}")
        elif inp == "g":
            a=float(input("a="))
            print(f"dla {a} obw_rombu ={obw_rombu(a)}")
        elif inp == "h":
            r=float(input("r="))
            print(f"dla {r} obw_kola ={obw_kola(r)}")
        


# ------------------------------------------------------------------------------

def plaskie()->None:
    while True:
        print("a -- pp fig plaskich")
        print("b -- obw fig plaskich")
        print("q -- Exsit ")
        inp = input().lower().strip()
        if inp == "a":
            jakie_pp()
        elif inp == "b":
            jakie_obw()
        elif inp == "q":
            print("Exsit")
            break


