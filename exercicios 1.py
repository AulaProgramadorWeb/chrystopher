#exercicio 1#

l1 = float(input("primeiro lado: "))
l2 = float(input("segundo lado: "))

area= l1 * l2

print("O valor da area é:", area)

#exercicio 2#

pao = float(input("Quantos pães?"))
sonho = float(input("Quantos sonhos?"))

pao= pao * 0.5
sonho = sonho * 2.0
resultado = pao + sonho

print("valor a pagar é: R$", resultado)

#exercicio 3#

dist = float(input("Qual a distancia do destino? "))
vgas = float(input("Qual o valor da gasolina? "))
kml = float(input("Quantos km por litro o seu carro percorre? "))

valor = (dist / kml) * vgas
print("O valor total gasto em combustivel será:R$ ",valor)

#exercicio 4#

alturac = float(input("Qual é a sua altura em centimetros? "))

alturam = alturac / 100

print("A sua altura em metros é: ", alturam ,"metros")

#exercicio 5#

vcompra = float(input("Insira o valor da sua compra: "))
desc = float(input("Insira o valor do desconto: "))

desc = desc / 100
vcompra = vcompra -(vcompra*desc)

print("o valor da sua compra com desconto é: ", vcompra)