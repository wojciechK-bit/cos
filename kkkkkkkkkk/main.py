import funkcje.plaskie as pl  funkcje.bryly as pl




def main():
    print("q - zakoncz program")
    print("a - plaskie")
    print("b - bryly")
    print("c - warunki")
    while True:
        inp = input().lower().strip()
        if inp == "q":
            print("Program zkonczyl dzialanie")
            break
        elif inp == "a":
            pl.plaskie()
        elif inp == "b":
            pl.bryly()
        elif inp == "c":
            pass

# --------------------------------------------------

main()













