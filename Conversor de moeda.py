print(" Dólar dos Estados Unidos USD\n Libra de Gibraltar GIP\n Libra Esterlina GBP\n Peso Chileno CLP\n O Rupia do Sri Lanka LKR\n Euro EUR\n Bitcoin BTC, \n Em breve terá 3 novas moedas." )
moeda = input("Digite a moeda de seu desejo: ")
reais = int(input("Qual o seu valor em reais ? "))

if moeda.lower() in ("1", "usd"):
   resultado = (reais * 0.1762487)
   print(f"O resultado da conversão é: {resultado}")

elif moeda.lower() in ("2", "gip"):
   resultado = (reais * 0.1327175)
   print (f"O resultado da conversão é: {resultado}")

elif moeda.lower() in ("3", "gbp"):
   resultado = (reais * 0.1324486)
   print(f"O resultado da conversão é: {resultado}")

elif moeda.lower() in ("1", "clp"):
   resultado = (reais * 165.5629139)
   print(f"O resultado da conversão é: {resultado}")
   
elif moeda.lower() in ("5", "lkr"):
   resultado = (reais * 52.8541226)
   print(f"O resultado da conversão é: {resultado}")

elif moeda.lower() in ("6", "eur"):
   resultado = (reais * 0.155094)
   print (f"O resultado da conversão é: {resultado}")

elif moeda.lower() in ("7", "btc"):
   resultado = (reais * 0.0000018)
   print(f"O resultado da conversão é: {resultado}")

else:
   print("Moeda não reconhecida. Por favor, tente novamente.")


