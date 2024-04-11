'''Tendo como entrada a altura e o sexo (codificado da seguinteforma:
 1:feminino 2:masculino)de uma pessoa,
 construa um programa que calcule e imprima seu peso ideal, utilizando asseguintes
 Fórmulas: - para homens: (72.7 * Altura) – 58 -para mulheres: (62.1 * Altura) –44.7'''

print("SISTEMA DE INDICAÇÃO DE PESO")
nome = str(input("Digite seu nome"))
sex = int(input("Digite seu sexo: 1 para masculino ou 2 para feminino"))
alt = float(input("Digite sua altura"))

if sex == 1:
    sexresp = "Masculino"
elif sex > 1 and sex < 3:
    sexresp = "Feminio"
else:
    sexresp = "esta opção não é valida"

if sexresp == "masculino":
    altres = (72.7 * alt ) - 50
else:
    altres = (62 * alt) - 44.7


print("Ola {}, Seu peso ideal é {}.".format(nome, altres))