'''
. Escreva um programa que leia o valor de 3 ângulos de um triângulo e escreva
se o triângulo é Acutângulo,Retângulo ou Obtusângulo. Sendoque: − Triângulo Retângulo: possuium ângulo reto.
(igual a 90º) −Triângulo Obtusângulo: possui umângulo obtuso. (maior que90º)
−Triângulo Acutângulo: possui trêsângulos agudos. (menor que 90º
'''

ld1 = float(input("Digite o Valor do primeiro lado do Triangulo"))
ld2 = float(input("Dgite o valor do segundo lado do TRiangulo"))
ld3 = float(input("Digite o Valor do Terceiro lado do Triangulo"))

if ld1 == 90 and ld2 == 90 and ld3 == 90:
    print("Os lados informados são {}, {} e {}. portanto é um Triangulo Retângulo".format(ld1 , ld2, ld3))
elif ld1 > 90 or ld2 > 90 or ld3 > 90:
    print("Os lados informados são {}, {} e {}. portanto é um Triangulo Obtusângulo".format(ld1, ld2, ld3))
elif ld1 < 90 or ld2 < 90 or ld3 < 90:
    print("Os lados informados são {}, {} e {}. portanto é um Triangulo Acutângulo".format(ld1, ld2, ld3))

