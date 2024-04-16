#exercicio 01
numero = float(input("Digite um número: "))

if (numero > 0):
    print("numero positivo")
elif(numero == 0):
    print("numero neutro")
else:
    print("numero negativo")
    
#exercicio 02
numero = float(input("Digite um número: "))

if((numero % 5 ) == 0):
    print("divisivel por 5")
else:
    print("nao eh divisivel por 5")
    
#exercicio 03
idade = int(input("Digite sua idade: "))

if(idade >= 18):
    print("maior de idade")
else:
    print("menor de idade")
    
#exercicio 04 
numero = float(input("Digite um número: "))

if(numero % 2 == 0):
    print("numero par")
else:
    print("impar")

#exercicio 05
idade = int(input("Digite sua idade: "))

if(idade <= 12):
    print("crianca")
elif(idade > 12 and idade < 18):
    print("adolescente")
elif(idade >= 18 and idade < 60):
    print("adulto")
else:
    print("idoso")

#exercicio 06
nota = float(input("Digite a nota do aluno: "))

if(nota < 6):
    print("insujficiente")
elif(nota >= 6 and nota <= 7.5):
    print("satisfatorio")
elif(nota > 7.5 and nota <= 9):
    print("Bom")
else:
    print("excelente")

#exercicio 07
numero = int(input("Digite um número: "))

if(numero > 0 and (numero % 2 == 0)):
    print("numero positivo e par")
elif(numero == 0):
    print("numero neutro")
else:
    print("numero ou nao eh positivo ou nao eh par")

#exercicio 08
idade = int(input("Digite sua idade: "))
permissao = input("Você tem permissão dos pais? (sim/nao): ")

if(idade < 18 and permissao == "sim"):
    print("podera participar da viagem")
elif(idade < 18 and permissao == "nao"):
    print("nao podera participar da viagem")
elif(idade >= 18): 
    print("podera participar da viagem pois tem 18 anos ou mais")



    