print(" Dólar dos Estados Unidos USD\n Libra de Gibraltar GIP\n Libra Esterlina GBP\n Peso Chileno CLP\n O Rupia do Sri Lanka LKR\n Euro EUR\n Bitcoin BTC, \n Em breve terá 3 novas moedas." )
moeda = input("Digite a moeda de seu desejo: ")
reais = int(input("Qual o seu valor em reais ? "))

if moeda == "USD" or moeda == "usd":
   resultado = (reais * 0.1762487)
   print(f"O resultado da conversão é: {resultado}")

elif moeda == "GIP" or moeda == "gip":
   resultado = (reais * 0.1327175)
   print (f"O resultado da conversão é: {resultado}")

elif moeda == "GBP" or moeda == "gbp":
   resultado = (reais * 0.1324486)
   print(f"O resultado da conversão é: {resultado}")

elif moeda == "CLP" or moeda == "clp":
   resultado = (reais * 165.5629139)
   print(f"O resultado da conversão é: {resultado}")
   
elif moeda == "LKR" or moeda == "lkr":
   resultado = (reais * 52.8541226)
   print(f"O resultado da conversão é: {resultado}")

elif moeda == "EUR" or moeda == "eur":
   resultado = (reais * 0.155094)
   print (f"O resultado da conversão é: {resultado}")

elif moeda == "BTC" or moeda == "btc":
   resultado = (reais * 0.0000018)
   print(f"O resultado da conversão é: {resultado}")

else:
   print("Moeda não reconhecida. Por favor, tente novamente.")


