import random

summa = 0

while summa < 21:
    kast = random.randint(1, 6)
    summa = summa + kast

    print("Du slog", kast)
    print("Nuvarande totalsumma:", summa)

    if summa > 21:
        print("Du förlorade!")
        break

    if summa == 21:
        print("Du vann!")
        break

    svar = input("Vill du kasta igen? (ja/nej): ")

    if svar == "nej":
        print("Du slutade på", summa)

        if summa >= 18:
            print("Du vann!")
        else:
            print("Du förlorade!")

        break