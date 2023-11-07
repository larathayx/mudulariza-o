def salvar_contatos_em_arquivo(agenda, arquivo):
    with open(arquivo, 'w') as file:
        for nome, info in agenda.items():
            file.write(f"{nome}#{info['endereco']}#{','.join(info['telefones'])}\n")

def carregar_contatos_de_arquivo(arquivo):
    agenda = {}
    try:
        with open(arquivo, 'r') as file:
            for linha in file:
                partes = linha.strip().split('#')
                nome, endereco, telefones = partes[0], partes[1], partes[2].split(',')
                agenda[nome] = {'endereco': endereco, 'telefones': telefones}
    except FileNotFoundError:
        pass  
    return agenda
