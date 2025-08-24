print(" Dólar dos Estados Unidos USD\n Libra de Gibraltar GIP\n Libra Esterlina GBP\n Peso Chileno CLP\n O Rupia do Sri Lanka LKR\n Euro EUR\n Bitcoin BTC, \n Em breve terá 3 novas moedas." )
operador = input("Digite a moeda de seu desejo: ")
reais = int(input("Qual o seu valor em reais ? "))

if operador == "USD" or operador == "usd":
   resultado = (reais * 0.1762487)
   print(f"O resultado da conversão é: {resultado}")

elif operador == "GIP" or operador == "gip":
   resultado = (reais * 0.1327175)
   print (f"O resultado da conversão é: {resultado}")

elif operador == "GBP" or operador == "gbp":
   resultado = (reais * 0.1324486)
   print(f"O resultado da conversão é: {resultado}")

elif operador == "CLP" or operador == "clp":
   resultado = (reais * 165.5629139)
   print(f"O resultado da conversão é: {resultado}")
   
elif operador == "LKR" or operador == "lkr":
   resultado = (reais * 52.8541226)
   print(f"O resultado da conversão é: {resultado}")

elif operador == "EUR" or operador == "eur":
   resultado = (reais * 0.155094)
   print (f"O resultado da conversão é: {resultado}")

elif operador == "BTC" or operador == "btc":
   resultado = (reais * 0.0000018)
   print(f"O resultado da conversão é: {resultado}")

else:
   print("Moeda não reconhecida. Por favor, tente novamente.")


