nota1 = float(input("Digite a nota 1:\n"))
nota2 = float(input("Digite a nota 2:\n"))

#critérios
media = (nota1 + nota2) /2

media_invalida = media < 0 or media > 10
aprovado = media >= 7
recuperacao = media > 3 and media < 7
reprovado = media < 3

if media_invalida:
    print(f"Media inválida -> {media}")
elif aprovado:
    print(f"Parabéns! Você está APROVADO com média {media}! \o/")
elif recuperacao:
    print(f"Quase! Você está em RECUPERAÇÃO com {media}! :|")
elif reprovado:
    print(f"Que pena! Você está REPROVADO com média {media}! :(")






