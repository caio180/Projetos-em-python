print("Conversor de temperatura: \n1: temperatura kelvin para Celsius \n2: temperatura Celsius para kelvin \n3: temperatura Fahrenheit para Celsios \n4: temperatura Celsius para Fahrenheit \n5: temperatura kelvin para Fahrenheit \n6: temperatura Fahrenheit para kelvin")
Escala = input(" Escolha o tipo de escala Termométrica = ")

if Escala == "kelvin para Celsius" or Escala == "Kelvin para Celsius" or Escala == "K para C" or Escala == "k para c" or Escala == "KpC" or Escala == "kpc" or Escala == "1":
   tk = float(input("K = "))
   temperatura_kelvin_p_Celsius = tk - 273.15
   print(round(temperatura_kelvin_p_Celsius), "°C.")
elif Escala == "Celsius para kelvin" or Escala == "celsius para kelvin" or Escala == "C para K" or Escala == "c para k" or Escala == "CpK" or Escala == "cpk" or Escala == "2":
    tc = float(input(" C = "))
    temperatura_Celsius_p_kelvin = tc + 273.15
    print(round(temperatura_Celsius_p_kelvin), "°K.")
elif Escala == "Fahrenheit para Celsius" or Escala == "fahrenheit para celsius" or Escala == "F para C" or Escala == "f para c" or Escala == "FpC" or Escala == "fpc" or Escala == "3":
    tf = float(input(" F = "))
    temp_Fahrenheit_p_C = (tf-32) * 5/9
    print(round(temp_Fahrenheit_p_C), "°C.")
elif Escala == "Celsius para Fahrenheit" or Escala == "celsius para fahrenheit" or Escala == "C para F" or Escala == "c para f" or Escala == "CpF" or Escala == "cpf" or Escala == "4":
    tcf = float(input(" Cf = "))
    tempcf = (tcf * 9/5 ) + 32
    print(round(tempcf), " °F.")
elif Escala == "kelvin para Fahrenheit" or Escala == "Kelvin para Fahrenheit" or Escala == "K para F" or Escala == "k para f" or Escala == "KpF" or Escala == "kpf" or Escala == "5":
    tkf = float(input(" Kf = "))
    tempkf = (tkf-273.15) * 9/5 + 32
    print(round(tempkf), "°F.")
elif Escala == "Fahrenheit para kelvin" or Escala == "fahrenheit para kelvin" or Escala == "F para K" or Escala == "f para k" or Escala == "Fpk" or Escala == "fpk" or Escala == "6":
    tfk = float(input(" Fk = "))
    tempfk = (tfk-32) * 5/9 + 273.15 
    print(round(tempfk), "°K.")