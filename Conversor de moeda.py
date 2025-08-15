print("1 Dólar dos Estados Unidos USD\n2 Libra de Gibraltar GIP\n3 Libra Esterlina GBP\n4 Peso Chileno CLP\n5 O Rupia do Sri Lanka LKR\n6 Euro EUR\n7 Bitcoin BTC, \n8 Em breve terá 3 novas moedas." )
operador = int(input("Digite a moeda de seu desejo: "))
reais = int(input("Qual o seu valor em reais ? "))

if operador == 1:
   resultado = (reais * 0.1762487)
   print("O resultado da conversão é:", resultado)

elif operador == 2:
   resultado = (reais * 0.1327175)
   print ("O resultado da conversão é:", resultado)

elif operador == 3:
   resultado = (reais * 0.1324486)
   print("O resultado da conversão é:", resultado)

elif operador == 4:
   resultado = (reais * 165.5629139)
   print("O resultado da conversão é:", resultado)
   
elif operador == 5:
   resultado = (reais * 52.8541226)
   print("O resultado da conversão é:", resultado)

elif operador == 6:
   resultado = (reais * 0.155094)
   print ("O resultado da conversão é:", resultado)

elif operador == 7:
   resultado = (reais * 0.0000018)
   print("O resultado da conversão é:", resultado)

else:
   print("Moeda não reconhecida. Por favor, tente novamente.")


