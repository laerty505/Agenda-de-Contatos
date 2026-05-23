import os


def menu():
    print("=====AGENDA DE CONTATOS=====")
    print("Escolha uma Opção!")
    print()

    print("1 - Cadastrar Contato")
    print("2 - Listar Contatos")
    print("3 - Excluir contatos")
    print('4 - Editar Contatos ')
    print('5 - Sair')

    

def listar_contatos(contatos):
    for contato in contatos:
        print(f'Nome: {contato[0]}')
        print(f'Telefone: {contato[1]}')
        print(f'Email: {contato[2]}')
        print()



def cadastrar(contatos):
    nome = input('Digite o nome: ')
    telefone = input('Digite o telefone: ')
    email = input('Digite o email: ')

    limpar_terminal()
    print('Cadastro efetuado com sucesso!')
    input('Aperte ENTER para continuar...')

    novo_contato = [nome, telefone, email]
    contatos.append(novo_contato)


def excluir_contato(contatos):
    if not contatos:
        print('Não há contatos para excluir.')
        return

    while True:
        print('Digite o índice do contato que deseja excluir!')
        print('Ou digite "N" para cancelar.')

        entrada = input('Índice: ').strip()

        if entrada.upper() == 'N':
            print('Operação cancelada.')
            break

        try:
            indice = int(entrada)
        except ValueError:
            print('Entrada inválida! Digite um número ou "N" para cancelar.')
            continue

        if not (0 <= indice < len(contatos)):
            print(f'Índice inválido! Escolha entre 0 e {len(contatos) - 1}.')
            continue


        print(f'O contato {contatos[indice][0]} foi excluído com sucesso!')
        input('Digite ENTER... Para continuar')
        contatos.pop(indice)
        limpar_terminal()
        break






def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')