def adicionar_contato(contatos, nome, telefone, email):
    contato = {"nome_contato": nome, "telefone_contato": telefone, "email_contato": email, "favorito": False}
    contatos.append(contato)
    print(f"Contato {nome} adicionado")
    return

def visualizar_lista_contatos(contatos):
    print("\nLista de Contatos")
    for indice, contato in enumerate(contatos, start=1):
        status = "☆" if contato["favorito"] else " "
        nome_contato = contato["nome_contato"]
        telefone_contato = contato["telefone_contato"]
        email_contato = contato["email_contato"]
        print(f"{indice}. {status} Nome: {nome_contato} Telefone: {telefone_contato} Email: {email_contato}")
    return

def editar_contato(contatos, indice_contato):
    indice_contato_ajustado = int(indice_contato) - 1
    print("Qual informação deseja editar: ")
    print("1. Nome")
    print("2. Telefone")
    print("3. Email")
    escolha = input("Digite o número da sua escolha: ")

    if escolha == "1":
        novo_nome = input("Informe o novo nome do contato: ")
        contatos[indice_contato_ajustado]["nome_contato"] = novo_nome
        print(f"Nome do contato {indice_contato} alterado")
    elif escolha == "2":
        novo_telefone = input("Informe o novo telefone do contato: ")
        contatos[indice_contato_ajustado]["telefone_contato"] = novo_telefone
        print(f"Telefone do contato {indice_contato} alterado")
    elif escolha == "3":
        novo_email = input("Informe o novo email do contato: ")
        contatos[indice_contato_ajustado]["email_contato"] = novo_email
        print(f"Email do contato {indice_contato} alterado")
    else:
        print("Indice inválido")
    return

def marcar_desmarcar_favorito(tarefas, indice_contato):
    indice_contato_ajustado = int(indice_contato) - 1
    if tarefas[indice_contato_ajustado]["favorito"]:
        tarefas[indice_contato_ajustado]["favorito"] = False
        print(f"Contato {indice_contato} desmarcado como favorito")
    else:
        tarefas[indice_contato_ajustado]["favorito"] = True
        print(f"Contato {indice_contato} marcado como favorito")
    return

def lista_contatos_favoritos(contatos):
    print("\nLista de Contatos Favoritos")
    for indice, contato in enumerate(contatos, start=1):
        if contato["favorito"]:
            nome_contato = contato["nome_contato"]
            telefone_contato = contato["telefone_contato"]
            email_contato = contato["email_contato"]
            print(f"{indice}. Nome: {nome_contato} Telefone: {telefone_contato} Email: {email_contato}")
    return

def apagar_contato(contatos, indice_contato):
    indice_contato_ajustado = int(indice_contato) - 1
    if indice_contato_ajustado >= 0 and indice_contato_ajustado < len(contatos):
        contatos.remove(contatos[indice_contato_ajustado])
        print(f"Contato removido")
    else:
        print("Indice de contato inválido")
    return

contatos = []

while True:
    print("\nAgenda de contatos")
    print("1. Adicionar um contato")
    print("2. Visualizar lista de contatos")
    print("3. Editar um contato")
    print("4. Marcar / Desmarcar um contato como favorito")
    print("5. Lista de contatos favoritos")
    print("6. Apagar um contato")
    print("7. Sair")

    escolha = input("Digite o número de sua escolha: ")
    
    if escolha == "1":
        nome_contato = input("Informe o nome do contato: ")
        telefone_contato = input("Informe o número do telefone: ")
        email_contato = input("Informe o email: ")
        adicionar_contato(contatos, nome_contato, telefone_contato, email_contato)
    elif escolha == "2":
        visualizar_lista_contatos(contatos)
    elif escolha == "3":
        visualizar_lista_contatos(contatos)
        indice_contato = input("Digite o número do contato para editar suas informações: ")
        editar_contato(contatos, indice_contato)
    elif escolha == "4":
        visualizar_lista_contatos(contatos)
        indice_contato = input("Digite o número do contato para marcar / desmarcar como favorito: ")
        marcar_desmarcar_favorito(contatos, indice_contato)
    elif escolha == "5":
        lista_contatos_favoritos(contatos)
    elif escolha == "6":
        visualizar_lista_contatos(contatos)
        indice_contato = input("Digite o número do contato para o apagar: ")
        apagar_contato(contatos, indice_contato)
    elif escolha == "7":
        break
print("Programa finalizado")