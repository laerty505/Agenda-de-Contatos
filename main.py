import funcoes

contatos = [
    ["Laerty", "91234-5678", "laerty@gmail.com"]
]

while True:
    funcoes.menu()

    opcao_usuario = int(input('Digite um número: '))
    print()

    match opcao_usuario:
        case 1:
            pass
        case 2:
            funcoes.listar_contatos(contatos)
            input('Aperte ENTER... Para continuar!')
        case 3:
            pass
        case 4:
            pass
        case 5:
            print('Encerrando...')
            break
        case _:
            print('Digite um número válido!')














