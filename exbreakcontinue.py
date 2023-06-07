#Ex 1#
print("############## ADIVINHE O Nº DE 1 A 10 ##############")
print("Voce tem 3 tentativas")

import random
from random import randint
x = random.randint(1,2)

for t in range(1,4):
    guess= int(input("Qual é o numero?"))
    while guess != x:
        print("Errouuu!!")
        if t>=0:
            print("Voce ja gastou {} tentativas".format(t))
            if t==3:
                print("Voce nao tem mais tentativas, LOOOSERR")
        break
    else:
        print("Voce acertou o numero era {}".format(x))
        
#EX 2#
print("LOOP 1-30")
Start = str(input("Press ENTER to >START LOOP<"))
for c in range(1,31):
    if c == 4 or c==19 or c==23:
        continue
    print(c)