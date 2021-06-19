import sys, random

print("Welcome to the Psych 'sidekick Name Picker.'\n")
print("A name just like Sean would pick for Gus:\n\n")

first = ('Baby oil', 'Bad News', 'Big Burps', "Bill 'Beenie-Weenie;", "Bob 'Stinkbug'", 'Bowel Noises', 'Boxelder', "Bud 'Lite'", 'Butterbean', 'Buttermilk', 'Buttocks', 'Chad', 'Chesterfield')
last = ('Appleyard', 'Bigmeat', 'Bloominshine', 'Boogerbottom', 'Breedslovetrout', 'Butterbaugh', 'Clovenhoof', 'Clutterbuck', 'Endicott', 'Fewhais', 'Goodberdapple', 'Goodensmith')

while True:
    firstName = random.choice(first)
    lastName = random.choice(last)
    print("{0} {1}".format(firstName, lastName), file=sys.stderr)
    print()
    try_agin = input("\nTry again? (Press Enter else n to quit): ")
    print()
    if try_agin.lower() == "n":
        break

input("\nPress Enter to exit.")