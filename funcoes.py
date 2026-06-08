import os # Importa o módulo para manipulação de arquivos



ARQUIVO = "contatos.txt" #Lista principal onde os contatos são armazenados durante a execução

def menu():
    print("=====AGENDA DE CONTATOS=====")
    print("Escolha uma Opção!")
    print()

    print("1 - Cadastrar Contato")
    print("2 - Listar Contatos")
    print("3 - Excluir contatos")
    print('4 - Editar Contatos ')
    print('5 - Sair')

    

def listar_contatos(contatos): # Exibe todos os contatos cadastrados
    for contato in contatos: # Percorre a lista exibindo cada contato
        print(f'Nome: {contato[0]}')
        print(f'Telefone: {contato[1]}')
        print(f'Email: {contato[2]}')
        print()



def cadastrar(contatos): # Solicita os dados do novo contato e adiciona à lista
    nome = input('Digite o nome: ')
    telefone = input('Digite o telefone: ')
    email = input('Digite o email: ') # Coleta as informações do contato

    limpar_terminal()
    print('Cadastro efetuado com sucesso!')
    input('Aperte ENTER para continuar...')
    limpar_terminal()

    novo_contato = [nome, telefone, email]
    contatos.append(novo_contato) # Adiciona o contato à lista
    salvar_contatos(contatos) # Atualiza o arquivo após a edição


def excluir_contato(contatos): # Remove um contato da agenda
    if not contatos: # Verifica se a lista é vazia
        print('Não há contatos para excluir.')
        return

    while True:
        print('Digite o índice do contato que deseja excluir!')
        print('Digite "Indice" para ver os índices!')
        print('Ou digite "N" para cancelar.')

        entrada = input('Índice: ').strip().upper()
        limpar_terminal()

        if entrada == 'N':
            print('Operação cancelada.')
            break

        if entrada in ('INDICE', 'ÍNDICE'):
            limpar_terminal()
            mostrar_indice_contato(contatos)
            input('Aperte ENTER... para continuar')
            limpar_terminal()
            continue

        try: # Verifica e trata erros de input
            indice = int(entrada)
        except ValueError:
            print('Entrada inválida! Digite um número ou "N" para cancelar.')
            continue

        if not (0 <= indice < len(contatos)): #Verifica se o índice não é maior que o existente
            print(f'Índice inválido! Escolha entre 0 e {len(contatos) - 1}.')
            print()
            continue


        print(f'O contato {contatos[indice][0]} foi excluído com sucesso!')
        input('Digite ENTER... Para continuar')
        contatos.pop(indice) # Remove o contato selecionado
        salvar_contatos(contatos) # Atualiza o arquivo após a edição
        limpar_terminal()
        break



def limpar_terminal(): # Limpa o terminal 
    os.system('cls' if os.name == 'nt' else 'clear')


def mostrar_indice_contato(contatos): # Exibe os índices da lista contatos
    for indice, nome in enumerate(contatos): # Percorre a lista contatos e mostra o índice 
        print(f'Índice: {indice}')
        print(f'Contato: {nome[0]}')
        print(f'Telefone: {nome[1]}')
        print(f'Email: {nome[2]}')
        print()


def editar_contato(contatos): # Permite alterar os dados de um contato existente
    if not contatos:
        print('Não há contatos para editar.')
        return
    
    while True:
        print('Digite o índice do contato que deseja editar!')
        print('Digite "Indice" para ver os índices!')
        print('Ou digite "N" para cancelar.')

        entrada = input('Índice: ').strip().upper()
        limpar_terminal()

        if entrada == 'N':
            print('Operação cancelada.')
            break

        if entrada in ('INDICE', 'ÍNDICE'):
            limpar_terminal()
            mostrar_indice_contato(contatos)
            input('Aperte ENTER... para continuar')
            limpar_terminal()
            continue

        try: # Verifica e trata erros de input
            indice = int(entrada)
        except ValueError:
            print('Entrada inválida! Digite um número ou "N" para cancelar.')
            continue

        if not (0 <= indice < len(contatos)):
            print(f'Índice inválido! Escolha entre 0 e {len(contatos) - 1}.')
            print()
            continue

        nome = input('Digite o novo nome: ')
        telefone = input('Digite o novo telefone: ')
        email = input('Digite o novo email: ')

        contatos[indice] = [nome, telefone, email] # Salva o contato na lista
        salvar_contatos(contatos) # Atualiza o arquivo após a edição
        print(f'O contato {nome} foi editado com sucesso!')
        input('Digite ENTER... Para continuar')
        limpar_terminal()
        break

def salvar_contatos(contatos): # Salva todos os contatos no arquivo contatos.tx
    with open(ARQUIVO, "w", encoding="utf-8") as arquivo:
        for contato in contatos: # Percorre cada contato da lista e grava uma linha no arquivo
            linha = ";".join(contato) # Junta os dados do contato usando ";" como separador
            arquivo.write(linha + "\n")

def carregar_contatos(): # Lê os contatos armazenados no arquivo e recria a lista
    contatos = []

    if not os.path.exists(ARQUIVO): # Verifica se o arquivo existe antes de tentar ler
        return contatos

    with open(ARQUIVO, "r", encoding="utf-8") as arquivo: 
        for linha in arquivo:
            linha = linha.strip()

            if linha:
                contato = linha.split(";") # Divide os dados da linha usando ";" como separador
                contatos.append(contato)

    return contatos