print("*********JOGO DO PAR OU IMPAR*********")
option = str(input("escolha se é PAR ou IMPAR: "))
if option != "IMPAR" and option!="PAR":
    print("RESPOSTA INVALIDA")
else:
    num = int(input("escolha um numero de 1 á 5: "))
    import random
    from random import randint
    Bot = random.randint(1,5)
    erro = "O Bot escolheu {} Voce errou".format(Bot)
    acerto = "O Bot escolheu {}, Voce acertou".format(Bot)
    r = Bot + num
    if (r % 2 !=1 and option == "PAR" ):
        print(acerto)
    elif(r % 2 ==1 and option == "IMPAR" ):
        print(acerto)
    elif(r % 2 != 1 and option == "IMPAR"):
        print(erro)
    elif(r % 2 == 1 and option == "PAR"):
        print(erro)