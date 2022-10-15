import Utils

while True:
    x = input("Zadej číslo:")
    if Utils.kontrolaCisla(x):
        print("Tvoje číslo je:", x)
        break
    else:
        print("Zadal jsi:",x)
        print("Musis zadat číslo")


