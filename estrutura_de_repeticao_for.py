#Criação de Código para Cálculo de Notas de Forma mais Resumida

lista_de_numeros = range(3)
soma = 0 #aqui digita o operador neutro da adição, caso fosse multiplicação seria 1
for numero in lista_de_numeros:
    nota = float(input(f"Digite a nota {numero + 1}:\n"))
    soma += nota #aqui é uma sintetização da comando para somar as várias notas, no caso 3

media = soma / len(lista_de_numeros)

print(f"Media: {media}")

