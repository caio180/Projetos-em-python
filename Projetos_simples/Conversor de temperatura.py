print("Conversor de temperatura: \n1: temperatura kelvin para Celsius \n2: temperatura Celsius para kelvin \n3: temperatura Fahrenheit para Celsios \n4: temperatura Celsius para Fahrenheit \n5: temperatura kelvin para Fahrenheit \n6: temperatura Fahrenheit para kelvin")
escala = input(" Escolha o tipo de escala Termométrica = ").strip().lower()

if escala.lower() in("kelvin para celsius", "k para c", "1"):
   tk = float(input("K = "))
   temperatura_kelvin_p_Celsius = tk - 273.15
   print(round(temperatura_kelvin_p_Celsius, 2), "°C.")
elif escala.lower()  in("celsius para kelvin", "c para k", "2"):
    tc = float(input("C = "))
    temperatura_Celsius_p_kelvin = tc + 273.15
    print(round(temperatura_Celsius_p_kelvin, 2), "°K.")
elif escala.lower() in("fahrenheit para celsius", "f para c", "3"):
    tf = float(input("F = "))
    temp_Fahrenheit_p_C = (tf-32) * 5/9
    print(round(temp_Fahrenheit_p_C, 2), "°C.")
elif escala.lower() in("celsius para fahrenheit", "c para f", "4"):
    tcf = float(input("Cf = "))
    tempcf = (tcf * 9/5 ) + 32
    print(round(tempcf, 2), " °F.")
elif escala.lower() in("kelvin para fahrenheit", "k para f", "5"):
    tkf = float(input("Kf = "))
    tempkf = (tkf-273.15) * 9/5 + 32
    print(round(tempkf, 2), "°F.")
elif escala.lower() in("fahrenheit para kelvin", "f para k", "6"):
    tfk = float(input("Fk = "))
    tempfk = (tfk-32) * 5/9 + 273.15 
    print(round(tempfk, 2), "°K.")