def show_stars(n):
    for i in range(0, n):
        for j in range(0, i + 1):
           print("* ", end="")
        print()

n=int(input("enter the number"))
show_stars(n)