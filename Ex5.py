vcompra = float(input("Insira o valor da sua compra: "))
desc = float(input("Insira o valor do desconto: "))

desc = desc / 100
vcompra = vcompra -(vcompra*desc)

print("o valor da sua compra com desconto é: ", vcompra)