'''
Escreva um programa que leia as medidas dos lados de um triângulo 
e escreva se ele é Equilátero, Isósceles ou Escaleno.
Sendo que:
Triângulo Equilátero: possui os 3 lados iguais.
Triângulo Isóscele:possui 2 lados iguais.
Triângulo Escaleno: possui 3 lados diferentes
'''

print("SISTEMA QUE DEFINE O TRIÂNGULOS")

ld1 = float(input("Digite o Primeiro lado do Triângulo"))
ld2 = float(input("Digite o Segudndo lado do Triângulo"))
ld3 = float(input("Digite o Terceiro lado do Triângulo"))

if ld1 == ld2 and ld2 == ld3:
    print("os lados digitados são {}, {} e {}. portanto o Triângulo é Equilatero".format(ld1,ld2,ld3))
elif ld1 != ld2 or ld2 != ld3:
    print("os lados digitados são {}, {} e {}. portanto o Triângulo é Isóscele".format(ld1,ld2,ld3))
else:
    print("os lados digitas são {}, {} e {}. portanto o Triângulo é Escaleno".format(ld1,ld2,ld3))