#Løs disse tre opgaver i den fil:
#Opgave 1: Print tallene fra 1 til 10 (begge inklusiv).
for i in range(1, 11):
    print(i)
#Opgave 2: Print alle tal fra 1 til 20, men kun de lige tal.
for i in range(1, 21):
    if i % 2 == 0:
        print(i)
#(Hint: et tal er lige hvis tal % 2 == 0)
#Opgave 3: Beregn og print summen af alle tal fra 1 til 100.
#(Hint: du skal bruge en variabel til at akkumulere summen)
total = 0
for i in range(1,101):
    
    total += i

print(total)

#Reglerne:

#Der er et hemmeligt tal: secret = 42
#Brugeren gætter et tal med input()
#Hvis gættet er forkert, siger programmet "For lavt" eller "For højt"
#Når brugeren gætter rigtigt, siger programmet "Korrekt!" og stopper

#Husk: input() returnerer en string — du skal konvertere til int med int(input(...)).
#Prøv dig frem. Vil du have et hint, eller kaster du dig ud i det?



while True:
    userInput = int(input("Guess a number: "))
    if userInput < 42:
        print("For lavt")
    elif userInput > 42:
        print("For højt")
    else:
        print("Korrekt!")
        break
    


