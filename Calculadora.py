print("Calculadora: \n+ Soma \n- Subtração \n* Multiplicação \n/ Divisão \n√ Raiz quadrada \n** Exponenciação \n// Divisão inteira \n% Resto da divisão")
num1 = int(input("Digite um número: "))
operação = input("Digite uma operação: ")
if operação != "√":
 num2 = int(input("Digite outro número: "))

if operação == "+":
    print(" O resultado é:", num1 + num2)

elif operação == "-":
    print(" O resultado é:", num1 - num2)

elif operação == "*":
    print(" O resultado é:", num1 * num2)

elif operação == "/":
    print(" O resultado é:", num1 / num2) 

elif operação == "√":
    import cmath
    raiz_quadrada = cmath.sqrt(num1)
    if num1 > 0 :
        import math
        raiz_quadrada = math.sqrt(num1)
    print(" O resultado é:", raiz_quadrada)

elif operação == "**":
    print("O resultado é:", num1 ** num2)

elif operação == "//":
    print("O resultado é:", num1 // num2)

elif operação == "%":
    print("O resto da divisão é:", num1 % num2)

else:
    print("Syntax Error.")