import threading
import math

#Função que será executada pela thread
def verificar_par():
    numero = int(input("Digite um número para verificar se é par ou impar: "))
    #Vai verificar se é par ou impar, se numero % 2 for igual 0 ele vai ser par, se não vai ser impar
    if numero % 2 == 0:
        print(f"{numero} é par")
    else:
        print(f"{numero} é impar")

#Função que será executada pela thread
def numeros_primos():
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

#Função que será executada pela thread
def validar_cpf():
   cpf = input("Digite o CPF (somente números): ")
   cpf_numeros = ''.join(filter(str.isdigit, cpf))

#Verifica se o CPF tem 11 dígitos
   if len(cpf_numeros) != 11:
          print("CPF inválido! Ele deve conter 11 dígitos numéricos.")
   else:
    #Verifica se todos os dígitos são iguais
       if cpf_numeros == cpf_numeros[0] * 11:
        print(f"{cpf} é inválido, contém todos os números iguais.")
       else:
            # Cálculo do primeiro dígito
             soma1 = sum(int(cpf_numeros[i]) * (10 - i) for i in range(9))
             digito1 = (soma1 * 10) % 11
             if digito1 == 10:
              digito1 = 0

            # Cálculo do segundo dígito
             soma2 = sum(int(cpf_numeros[i]) * (11 - i) for i in range(10))
             digito2 = (soma2 * 10) % 11
             if digito2 == 10:
              digito2 = 0

            # Verificação final
             if cpf_numeros[-2:] == f"{digito1}{digito2}":
               print(f"{cpf} é válido.")
             else:
               print(f"{cpf} é inválido.")


#Cria as threads
thread1 = threading.Thread(target=verificar_par)
thread2 = threading.Thread(target=numeros_primos)
thread3 = threading.Thread(target=validar_cpf)

#Inicia as threads
thread1.start()
thread2.start()
thread3.start()

#Aguarda as threads terminarem antes de continuar o código principal.
thread1.join()
thread2.join()
thread3.join()
