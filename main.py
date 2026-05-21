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
            funcoes.cadastrar(contatos)
        case 2:
            funcoes.limpar_terminal()
            funcoes.listar_contatos(contatos)
            input('Aperte ENTER... Para continuar!')
            funcoes.limpar_terminal()
        case 3:
            pass
        case 4:
            pass
        case 5:
            print('Encerrando...')
            break
        case _:
            print('Digite um número válido!')














