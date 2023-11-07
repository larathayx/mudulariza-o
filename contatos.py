def criar_contato(agenda):
    nome = input("Digite o nome do contato: ")
    endereco = input("Digite o endereco do contato: ")
    telefones = input("Digite os números de telefone (separados por vírgula): ").split(',')
    
    agenda[nome] = {
        'endereco': endereco,
        'telefones': telefones
    }
    print(f"Contato {nome} criado com sucesso!")

def listar_contatos(agenda):
    print("Lista de Contatos:")
    for nome, info in agenda.items():
        print(f"Nome: {nome}")
        print(f"Endereço: {info['endereco']}")
        print("Telefones:")
        for telefone in info['telefones']:
            print(f"  {telefone}")
        print("\n")

def deletar_contato(agenda):
    nome = input("Digite o nome do contato que deseja deletar: ")
    if nome in agenda:
        del agenda[nome]
        print(f"Contato {nome} deletado com sucesso!")
    else:
        print(f"Contato {nome} não encontrado na agenda.")

def editar_contato(agenda):
    nome = input("Digite o nome do contato que deseja editar: ")
    if nome in agenda:
        print(f"Editando contato {nome}:")
        endereco = input("Novo endereço (pressione Enter para manter o mesmo): ")
        telefones = input("Novos números de telefone (separados por vírgula) (pressione Enter para manter os mesmos): ").split(',')
        
        if endereco:
            agenda[nome]['endereco'] = endereco
        if telefones:
            agenda[nome]['telefones'] = telefones
        
        print(f"Contato {nome} editado com sucesso!")
    else:
        print(f"Contato {nome} não encontrado na agenda.")