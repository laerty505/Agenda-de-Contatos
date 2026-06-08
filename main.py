import funcoes #Importa as funções utilizadas pelo sistema

contatos = funcoes.carregar_contatos()


# Loop principal do programa
# Continua executando até que o usuário escolha sair
while True:
    funcoes.limpar_terminal()
    funcoes.menu()
    try: # Verifica e trata erros de input
        opcao_usuario = int(input('Digite um número: '))
    except ValueError:
        print('Entrada inválida! Digite um número ou "N" para cancelar.')
        input('Aperte ENTER para continuar...')
        continue
    
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



   














