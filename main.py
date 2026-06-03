import funcoes

contatos = [
    ["Laerty", "91234-5678", "laerty@gmail.com"]
]

while True:
    funcoes.limpar_terminal()
    funcoes.menu()

    opcao_usuario = int(input('Digite um número: '))
    funcoes.limpar_terminal()

    match opcao_usuario:
        case 1:
            funcoes.limpar_terminal()
            funcoes.cadastrar(contatos)
        case 2:
            funcoes.limpar_terminal()
            funcoes.listar_contatos(contatos)
            input('Aperte ENTER... Para continuar!')
            funcoes.limpar_terminal()
            
        case 3:
            funcoes.limpar_terminal()
            funcoes.excluir_contato(contatos)
        case 4:
            funcoes.limpar_terminal()
            funcoes.editar_contato(contatos)
        case 5:
            funcoes.limpar_terminal()
            print('Encerrando...')
            break
        case _:
            funcoes.limpar_terminal()
            print('Digite um número válido!')



   














