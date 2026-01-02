import threading
import math


def verificar_par():
    numero = int(input("Digite um número para verificar se é par ou impar: "))
    
    if numero % 2 == 0:
        print(f"{numero} é par")
    else:
        print(f"{numero} é impar")


def verificar_numeros_primos():
    num = int(input("Digite um número para verificar se é primo: "))

    if num <= 1:
        print(f"{num} não é primo")
        return
    elif num == 2:
        print(f"{num} é primo")
        return
    elif num % 2 == 0:
        print(f"{num} não é primo")
        return
    
    limite = int(math.sqrt(num)) + 1
    for i in range(3, limite, 2):
        if num % i == 0:
            print(f"{num} não é primo")
            return
    print(f"{num} é primo")


def validar_cpf():
   cpf = input("Digite o CPF (somente números): ")
   cpf_numeros = ''.join(filter(str.isdigit, cpf))


   if len(cpf_numeros) != 11:
          print(f"O cpf: {cpf} é inválido, pois ele deve conter 11 dígitos numéricos.")
   else:

       if cpf_numeros == cpf_numeros[0] * 11:
        print(f"O cpf: {cpf} é inválido, contém todos os números iguais.")
       else:
           
             soma1 = sum(int(cpf_numeros[i]) * (10 - i) for i in range(9))
             digito1 = (soma1 * 10) % 11
             if digito1 == 10:
              digito1 = 0

            
             soma2 = sum(int(cpf_numeros[i]) * (11 - i) for i in range(10))
             digito2 = (soma2 * 10) % 11
             if digito2 == 10:
              digito2 = 0

            
             if cpf_numeros[-2:] == f"{digito1}{digito2}":
               print(f"O cpf: {cpf} é válido.")
             else:
               print(f"O cpf: {cpf} é inválido.")


#Cria as threads
thread1 = threading.Thread(target=verificar_par)
thread2 = threading.Thread(target=verificar_numeros_primos)
thread3 = threading.Thread(target=validar_cpf)

#Inicia as threads
thread1.start()
thread2.start()
thread3.start()

#Aguarda as threads terminarem antes de continuar o código principal.
thread1.join()
thread2.join()
thread3.join()
