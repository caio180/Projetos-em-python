import time

print("Quiz")
questao = input("Para começar o quiz digite o número 1: ")

print("Iniciando...")
time.sleep(3)

for questao in range(11):
 if questao == 1:
     q1 = int(input("1) Quem foi o primeiro Papa da igreja Católica ? \n1 - Pedro \n2 - Tiago \n3 - Matias \n4 - André \n"))
     if q1 == 1:
        print("Resposta correta, parabéns")
     else:
        print("Resposta incorreta.")
 elif questao == 2:
     q2 = int(input("2) Qual é o Papa atual da igreja Católica ? \n1 - Papa Paulo VI \n2 - Papa Francisco \n3 - Papa Leão XIV \n4 - Papa João Paulo II \n"))
     if q2 == 3:
        print("Resposta correta, parabéns.")
     else: 
        print("Resposta incorreta.")
 elif questao == 3:
     q3 = int(input("3) Qual foi o Papa que durou apenas 33 dias no Papado ? \n1 - Papa Bento XV \n2 - Papa Pio XII \n3 - Papa Pio XI \n4 - Papa João Paulo I \n"))
     if q3 == 4:
        print("Resposta correta, parabéns.")
     else: 
        print("Resposta incorreta.")
 elif questao == 4:
     q4 = int(input("4) Em qual país o Papa Bento XVI nasceu ? \n1 - Itália \n2 - Alemanha \n3 - Brasil \n4 - França \n"))
     if q4 == 2:
        print("Resposta correta, parabéns.")
     else: 
        print("Resposta incorreta.")
 elif questao == 5:
     q5 = int(input("5) Qual Papa convocou o Concílio Vaticano II ? \n1 - Papa João XXIII \n2 - Papa Leão XIII \n3 - Papa Pio VI \n4 - Papa Bento XVI \n"))
     if q5 == 1:
        print("Resposta correta, parabéns.")
     else: 
        print("Resposta incorreta.") 
 elif questao == 6:
     q6 = str(input("6) Qual Papa ficou apenas 12 dias no Papado ? \n"))
     if q6.lower() in("urbano vii", "urbano 7"):
        print("Resposta correta, parabéns.")
     else: 
        print("Resposta incorreta.") 
 elif questao == 7:
     q7 = input("7) Quantos Papas com o nome bento a Igreja católica já teve ? \n")
     if q7.lower() in("16", "dezesseis", "16 papas"):
        print("Resposta correta, parabéns.")
     else: 
        print("Resposta incorreta.")
 elif questao == 8:
     q8 = input("8) Qual o nome mais usado pelos Papas? \n1 - Leão \n2 - João \n3 - Pio \n4 - Urbano \n")
     if q8.lower() in("2", "joão", "joao"):
        print("Resposta correta, parabéns.")
     else: 
        print("Resposta incorreta.") 
 elif questao == 9:
     q9 = int(input("9) Em qual ano o Papa Leão XIV nasceu ? \n"))
     if q9 == 1955:
        print("Resposta correta, parabéns.")
     else: 
        print("Resposta incorreta.")
 elif questao == 10:
     q10 = str(input("10) Em qual país o Papa Pio XII nasceu ? \n"))
     if q10.lower() in ("italia", "itália."):
        print("Resposta correta, parabéns.")
     else: 
        print("Resposta incorreta.") 
