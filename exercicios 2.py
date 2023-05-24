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
euro = float(input("Insira o valor atual do EURO: "))
dolar = float(input("Insira o valor atual do DOLAR: "))
real = float(input("Insira o valor atual do REAL: "))
valor = float(input("Insira o valor para converter: "))

euro = valor * euro
dolar = valor * dolar
real = valor * real

print("valor em EURO: {}".format(euro), "valor em DOLAR: {}".format(dolar), "valor em REAL:{} ".format(real))
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
