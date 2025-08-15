print("Conversor de temperatura: \n1 temperatura kelvin para Celsius \n2 temperatura Celsius para kelvin \n3 temperatura Fahrenheit para Celsios \n4 temperatura Celsius para Fahrenheit \n5 temperatura kelvin para Fahrenheit \n6 temperatura Fahrenheit para kelvin")
Escala = int(input(" Escolha o tipo de escala Termométrica = "))

if Escala == 1:
   tk = float(input("K = "))
   temperatura_kelvin_p_Celsius = tk - 273.15
   print(round(temperatura_kelvin_p_Celsius), "°C.")
elif Escala == 2:
    tc = float(input(" C = "))
    temperatura_Celsius_p_kelvin = tc + 273.15
    print(round(temperatura_Celsius_p_kelvin), "°K.")
elif Escala == 3:
    tf = float(input(" F = "))
    temp_Fahrenheit_p_C = (tf-32) * 5/9
    print(round(temp_Fahrenheit_p_C), "°C.")
elif Escala == 4:
    tcf = float(input(" Cf = "))
    tempcf = (tcf * 9/5 ) + 32
    print(round(tempcf), " °F.")
elif Escala == 5:
    tkf = float(input(" Kf = "))
    tempkf = (tkf-273.15) * 9/5 + 32
    print(round(tempkf), "°F.")
elif Escala == 6:
    tfk = float(input(" Fk = "))
    tempfk = (tfk-32) * 5/9 + 273.15 
    print(round(tempfk), "°K.")