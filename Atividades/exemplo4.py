'''
Acrescente as seguintesmensagens à solução do exercícioanterior conforme o caso. 
 Casoo número de lados seja inferior a 3 escrever NÃO É UM POLÍGONO.
 Caso o número de lados seja superior a 5 escrever POLÍGONONÃO IDENTIFICADO
'''

nome = str(input("qual seu nome?"))
lds = float(input("Certo, {} Digite quantos lados tem o poligno que deseja identifar?".format (nome)))

if lds < 3:
   print ("poxa {}, Não é um Poligno".format(nome))
elif lds == 3:
    area1 = float(input("Digite por favor o valor da primeira área: "))
    area2 = float(input("Digite por favor o valor da segunda área: "))
    area3 = float(input("Digite a terceira área: "))
    print ("{}, o seu poligno é um Triângulo com as areas {}, {} e {}." .format(nome,area1,area2,area3))
elif lds == 4:
    area1 = float(input("Digite por favor o valor da primeira área: "))
    area2 = float(input("Digite o valor da segunda área: "))
    area3 = float(input("Digite o valor da terceira área: "))
    area4 = float(input("Digite o valor da quarta área: "))
    print ("{}, o seu poligno é um Quadrado com as areas {}, {}, {} e {}." .format(nome,area1,area2,area3,area4))
elif lds == 5:
    area1 = float(input("Digite por favor o valor da primeira área: "))
    area2 = float(input("Digite o valor da segunda área: "))
    area3 = float(input("Digite o valor da terceira área: "))
    area4 = float(input("Digite o valor da quarta área: "))
    area5 = float(input("Digite o valor da quinta área: "))
    print ("{}, o seu poligno é um Pentágono com as areas {}, {}, {}, {} e {}." .format(nome,area1,area2,area3,area4,area5))
else:
 print("poxa {}, Poligno não identificado.".format(nome))