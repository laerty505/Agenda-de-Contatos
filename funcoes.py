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


def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')