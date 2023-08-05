#Esse código conjuga a estrutura de decisão das notas

nota1 = float(input("Digite a nota 1:\n"))

nota_invalida = nota1 < 0 or nota1 > 10

while nota_invalida:
    print("A nota de ser entre 0 (zero) e 10 (dez)")
    nota1 = float(input("Digite a nota 1:\n"))
    nota_invalida = nota1 < 0 or nota1 > 10


nota2 = float(input("Digite a nota 2:\n"))
nota_invalida = nota2 < 0 or nota2 > 10

while nota_invalida:
    print("A nota de ser entre 0 (zero) e 10 (dez)")
    nota2 = float(input("Digite a nota 2:\n"))
    nota_invalida = nota2 < 0 or nota2 > 10

nota3 = float(input("Digite a nota 3:\n"))
nota_invalida = nota3 < 0 or nota3 > 10

while nota_invalida:
    print("A nota de ser entre 0 (zero) e 10 (dez)")
    nota3 = float(input("Digite a nota 3:\n"))
    nota_invalida = nota3 < 0 or nota3 > 10

media = (nota1 * 4 + nota2 * 5 + nota3 * 6) / 15

aprovado = media = 7
recuperacao = media > 3 and media < 7
reprovado = media < 3

#aqui digitar o resto do código da estrutura de decisão 2 - ver vídeo da aula para complementar.
