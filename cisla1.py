# Nacita cislo od uzivatele, predpoklada nacteni int, zatim neosetreno
while True:
    n = (int)(input("Zadej prirozene cislo: "))
    if n > 0:
        break

# Vypise zadane cislo
print("Zadane cislo je " + (str)(n))

# Secte prirozena cisla od 1 do n (zapocitava i realnou 0, coz zde ovsem nevadi)
soucet = 0
for i in range(n+1):
    soucet += i
print("Soucet prvnich n prirozenych cisel je: " + (str)(soucet))

