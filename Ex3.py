dist = float(input("Qual a distancia do destino? "))
vgas = float(input("Qual o valor da gasolina? "))
kml = float(input("Quantos km por litro o seu carro percorre? "))

valor = (dist / kml) * vgas
print("O valor total gasto em combustivel será:R$ ",valor)