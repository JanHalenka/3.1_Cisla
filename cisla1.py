while True:
    n = (int)(input("Zadej prirozene cislo: "))
    if n > 0:
        break

print('Zadane cislo je ' + (str)(n))

soucet = 0
for i in range(n+1):
    soucet += i
print("Soucet prvnich n prirozenych cisel je: " + (str)(soucet))

