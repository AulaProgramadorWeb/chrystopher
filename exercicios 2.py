#exercicio 1#

n1 = float(input("Insira o Dividendo: "))
n2 = float(input("Insira o Divisor: "))

r = n1 / n2

if (r!=0):
    print("O resultado da divisão é: {} ".format(r))
else:
    print("O numero é inválido")

#exercicio 2#

sal = float(input("Insira o salario do funcionario: "))
desc = float(input("Insira quanto de desconto:"))

desc = desc / 100
vdesc = sal * desc

if (vdesc >= 318.20):
    print("O valor do desconto é R$ 318,20")
else:
    print("O valor do desconto é: R$ {} ".format(vdesc))

#exercicio 3#
c = str(input("Deseja iniciar o programa?\nS/N\n"))
while c == "S":
    print("####Calculadora de Conversão####")
    euro = float(input("Insira o valor atual do EURO:\n "))
    dolar = float(input("Insira o valor atual do DOLAR:\n "))
    real = 1
    print("Qual opção de conversão voce deseja?")
    choice = int(input("Euro para Dolar[1], Euro para Real[2], Dolar para Euro[3], Dolar para real[4], Real para euro[5], Real para dolar[6]\n"))
    valor = float(input("Qual o valor para converter?\n"))
    if choice == 1:
        valor = valor * euro
        valor = valor/dolar
    elif choice == 2:
        valor = valor * euro
        valor = valor/real
    elif choice == 3:
        valor = valor * dolar
        valor = valor/euro
    elif choice == 4:
        valor = valor * dolar
        valor = valor/real
    elif choice == 5:
        valor = valor * real
        valor = valor/euro
    elif choice == 6:
        valor = valor * real
        valor = valor/dolar
    print("O resultado da conversão é: {} ".format(valor))
    c = str(input("Deseja iniciar o programa?\nS/N\n"))
#exercicio 4#
age = int(input("Qual a sua idade? "))

if (age < 5 and age !=0):
    print("Desculpe mas você nao pode participar")
elif(age >= 5 and age<=7):
    print("Categoria Infantil A")
elif(age>=8 and age<=10):
    print("Categoria Infantil B")
elif(age>=11 and age<=13):
    print("Categoria Juvenil A")
elif(age>=14):
    print("Categoria Sênior")
elif(age==0):
    print("Idade Invalida")
