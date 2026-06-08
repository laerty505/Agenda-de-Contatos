# 📒 Agenda de Contatos

Projeto final da disciplina de Lógica de Programação. Uma agenda de contatos via terminal, com persistência de dados em arquivo, que permite cadastrar, listar, editar e excluir contatos.

---

## ✨ Funcionalidades

- **Cadastrar** novo contato (nome, telefone e e-mail)
- **Listar** todos os contatos salvos
- **Editar** um contato existente pelo índice
- **Excluir** um contato pelo índice
- **Persistência** — os dados são salvos em arquivo `.txt` e mantidos entre execuções

---

## 🗂️ Estrutura do Projeto

```
Projeto_agenda_contatos/
├── main.py        # Ponto de entrada — menu principal e loop do programa
├── funcoes.py     # Todas as funções da agenda (cadastrar, listar, editar, excluir, salvar...)
└── contatos.txt   # Arquivo gerado automaticamente para armazenar os contatos
```

---

## ▶️ Como executar

**Pré-requisito:** Python 3.10 ou superior instalado.

1. Clone ou baixe o repositório: https://github.com/laerty505/Agenda-de-Contatos.git
2. Acesse a pasta do projeto pelo terminal
3. Execute o arquivo principal:

```bash
python main.py
```

O arquivo `contatos.txt` será criado automaticamente na primeira vez que um contato for cadastrado.

---

## 🖥️ Exemplo de uso

```
=====AGENDA DE CONTATOS=====
Escolha uma Opção!

1 - Cadastrar Contato
2 - Listar Contatos
3 - Excluir contatos
4 - Editar Contatos
5 - Buscar por nome
6 - Sair

Digite um número: 1

Digite o nome: Maria Silva
Digite o telefone: 81 99999-0000
Digite o email: maria@email.com

Cadastro efetuado com sucesso!
```

---

## 🛠️ Tecnologias utilizadas

- **Python 3.10+**
- Módulo `os` (limpeza de terminal multiplataforma)
- Arquivos `.txt` para persistência de dados

---

## 👨‍💻 Autor
Laerty Batista de Santana Silva - IFPE 
Desenvolvido como projeto final de Lógica de Programação.