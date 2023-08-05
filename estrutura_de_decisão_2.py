nota1 = float(input("Digite a nota 1:\n"))
nota2 = float(input("Digite a nota 2:\n"))

media = (nota1 * 4 + nota2 * 5 + nota * 6) /15

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
    # solicitar a nota 4
    # calcular a nova media (media + nota4) / 2
    # testar a nova media agora com media 5
    nota4 = float(input("Digite a nota 4:\n"))
    media = (media + nota4) / 2
    if aprovado:
        print(f"Parabéns! Você está APROVADO com média {media}! \o/")
    else
        
        
        elif reprovado:
    print(f"Que pena! Você está REPROVADO com média {media}! :(")