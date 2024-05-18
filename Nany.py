# author: Seu Nome - Sua Matrícula

def menu():
    print("\nMenu:")
    print("1. Inserir novo contato")
    print("2. Apagar contato")
    print("3. Alterar contato")
    print("4. Listar contatos")
    print("5. Gravar contatos em arquivo")
    print("6. Ler contatos do arquivo")
    print("7. Ordenar contatos por nome")
    print("8. Consultar contato")
    print("9. Sair")

def inserir_contato(contatos):
    nome = input("Nome: ")
    if nome in contatos:
        print("Usuário já está cadastrado")
        return
    tipo_telefone = input("Tipo de telefone (cel, fixo): ")
    telefone = input("Telefone: ")
    contatos[nome] = (tipo_telefone, telefone)
    print("Contato inserido com sucesso")

def apagar_contato(contatos):
    nome = input("Nome do contato a ser apagado: ")
    if nome in contatos:
        del contatos[nome]
        print("Contato apagado com sucesso")
    else:
        print("Nome não cadastrado")

def alterar_contato(contatos):
    nome = input("Nome do contato a ser alterado: ")
    if nome in contatos:
        tipo_telefone = input("Novo tipo de telefone (cel, fixo): ")
        telefone = input("Novo telefone: ")
        contatos[nome] = (tipo_telefone, telefone)
        print("Contato alterado com sucesso")
    else:
        print("Nome não cadastrado")

def listar_contatos(contatos):
    if contatos:
        for nome, (tipo_telefone, telefone) in contatos.items():
            print(f"Nome: {nome}, Tipo: {tipo_telefone}, Telefone: {telefone}")
    else:
        print("Nenhum contato cadastrado")

def gravar_contatos_arquivo(contatos, arquivo):
    with open(arquivo, 'w') as f:
        for nome, (tipo_telefone, telefone) in contatos.items():
            f.write(f"{nome},{tipo_telefone},{telefone}\n")
    print("Contatos gravados com sucesso")

def ler_contatos_arquivo(arquivo):
    contatos = {}
    try:
        with open(arquivo, 'r') as f:
            for line in f:
                nome, tipo_telefone, telefone = line.strip().split(',')
                contatos[nome] = (tipo_telefone, telefone)
        print("Contatos lidos com sucesso")
    except FileNotFoundError:
        print("Arquivo não encontrado")
    return contatos

def ordenar_contatos(contatos):
    contatos_ordenados = dict(sorted(contatos.items()))
    listar_contatos(contatos_ordenados)
    return contatos_ordenados

def consultar_contato(contatos):
    nome = input("Nome do contato a ser consultado: ")
    if nome in contatos:
        print("Nome cadastrado")
    else:
        print("Nome não cadastrado")

def main():
    contatos = {}
    arquivo = 'seunome.txt'
    while True:
        menu()
        opcao = input("Escolha uma opção: ")
        if opcao == '1':
            inserir_contato(contatos)
        elif opcao == '2':
            apagar_contato(contatos)
        elif opcao == '3':
            alterar_contato(contatos)
        elif opcao == '4':
            listar_contatos(contatos)
        elif opcao == '5':
            gravar_contatos_arquivo(contatos, arquivo)
        elif opcao == '6':
            contatos = ler_contatos_arquivo(arquivo)
        elif opcao == '7':
            contatos = ordenar_contatos(contatos)
        elif opcao == '8':
            consultar_contato(contatos)
        elif opcao == '9':
            print("Saindo...")
            break
        else:
            print("Opção inválida, tente novamente")

if __name__ == "__main__":
    main()
