from contatos import criar_contato, listar_contatos, deletar_contato, editar_contato
from arquivo import salvar_contatos_em_arquivo, carregar_contatos_de_arquivo

def main():
    arquivo_contatos = "contatos.txt"
    agenda = carregar_contatos_de_arquivo(arquivo_contatos)

    while True:
        print("\nMenu:")
        print("1. Criar Contato")
        print("2. Listar Contatos")
        print("3. Deletar Contato")
        print("4. Editar Contato")
        print("5. Salvar e Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            criar_contato(agenda)
        elif opcao == '2':
            listar_contatos(agenda)
        elif opcao == '3':
            deletar_contato(agenda)
        elif opcao == '4':
            editar_contato(agenda)
        elif opcao == '5':
            salvar_contatos_em_arquivo(agenda, arquivo_contatos)
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()