'''
Escreva um programa para ler o número de lados 
de um polígono regular e a medida do lado (em cm).
Calcular e imprimir o seguinte: 
se o número de lados for igual a 3 escrever TRIÂNGULO e o valor da área 
Se o número de lados for igual a 4 escrever QUADRADO e o valor da sua área.
Se o número de lados for igual a 5 escreve Pentagono e o valor da sua área
'''
print("SISTEMA QUE IDENTIFICA O POLIGNO")

nome = str(input("qual seu nome?"))
lds = float(input("Certo, {} Digite quantos lados tem o poligno que deseja identifar?".format (nome)))

if lds == 3:
    area1 = float(input("Digite por favor o valor da primeira área: "))
    area2 = float(input("Digite por favor o valor da segunda área: "))
    area3 = float(input("Digite a terceira área: "))
    print("{}, o seu poligno é um Triângulo com as areas {}, {} e {}." .format(nome,area1,area2,area3))
elif lds == 4:
    area1 = float(input("Digite por favor o valor da primeira área: "))
    area2 = float(input("Digite o valor da segunda área: "))
    area3 = float(input("Digite o valor da terceira área: "))
    area4 = float(input("Digite o valor da quarta área: "))
    print("{}, o seu poligno é um Quadrado com as areas {}, {}, {} e {}." .format(nome,area1,area2,area3,area4))
elif lds == 5:
    area1 = float(input("Digite por favor o valor da primeira área: "))
    area2 = float(input("Digite o valor da segunda área: "))
    area3 = float(input("Digite o valor da terceira área: "))
    area4 = float(input("Digite o valor da quarta área: "))
    area5 = float(input("Digite o valor da quinta área: "))
    print("{}, o seu poligno é um Pentágono com as areas {}, {}, {}, {} e {}." .format(nome,area1,area2,area3,area4,area5))
else:
 print("Poligno não identificado.")
