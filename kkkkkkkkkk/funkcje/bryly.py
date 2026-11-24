from math import pi
def pp_szescianu(a:float)->float:
    return 6*a**2

def pp_prostopadloscianu(a:float,b:float,c:float)->float:
    return 2*a*b+2*a*c+2*b*c

def pp_graniastoslipa(Pp:float,Pb:float)->float:
    return 2*Pp+Pb

def pp_ostroslupa(Pp:float,Pb:float)->float:
    return Pp+Pb

def pp_walca(r:float,h:float)->float:
    return 2*pi*r**2+2*pi*h

def pp_stozka(r:float,i:float)->float:
    return pi*r**2+pi*r*i

def pp_kuli(r:float)->float:
    return 4*pi*r**2  

def legenda_pp()->None:
    print("a---pp_szescianu")
    print("b----pp_prostopadloscianu")
    print("c---pp_graniastoslipa")
    print("d---pp_ostroslupa")
    print("e--- pp_walca")
    print("f---pp_stozka")
    print("g---pp_kuli")

def jakie_pp()->None:
    while True:
        legenda_pp()
        inp = input().lower().strip()
        if inp == "q":
            print("Exsit")
            break
        elif inp == "a":
            a=float(input("a="))
            print(f"dla{a} pp_szescianu={pp_szescianu(a)} ")
        elif inp=="b":
            a=float(input("a="))
            b=float(input("b="))
            c=float(input("c="))
            print(f"dla{a} {b} {c} pp_prostopadloscianu={pp_prostopadloscianu(a,b,c)}")
        elif inp=="c":
            Pp=float(input("Pp="))
            Pb=float(input("Pb="))
            print(f"dla {Pp} {Pb} pp_graniastoslipa={pp_graniastoslipa(Pp,Pb)}")
        elif inp=="d":
            Pp=float(input("Pp="))
            Pb=float(input("Pb="))
            print(f"dla {Pp} {Pb} pp_ostroslupa={pp_ostroslupa(Pp,Pb)}")
        elif inp=="e":
            r=float(input("r="))
            h=float(input("h="))
            print(f"dla {h} {r} pp_walca={pp_walca(h,r)}")
        elif inp=="f":
            r=float(input("r="))
            i=float(input("i="))
            print(f"dla {h} {i} pp_stozka={pp_stozka(i,r)}")
        elif inp=="g":
            r=float(input("r="))
            print(f"dla {r} pp_kuli={pp_kuli(r)}")
# ---------------------------------------------------------------




# --------------------------------------------------------------
def bryly()->None:
    while True:
        print("a -- pp bryl")
        print("b -- obw bryl")
        print("q -- Exsit ")
        inp = input().lower().strip()
        if inp == "a":
            jakie_pp()
        elif inp == "b":
            pass
        elif inp == "q":
            print("Exsit")
            break


