ls_lista_compras = []
ls_quantidades = []
lf_lista_valores = []


while True:
    print()
    print("--Digite 1 para adicionar itens à lista--")
    print("--Digite 2 para editar um item da lista--")   
    print("--Digite 3 para remover itens da lista--")
    print("--Digite 4 para visualizar a lista--")
    print("--Digite 5 para visualizar o valor total--")
    print("--Digite 6 para fechar a lista--")
    print()
    # Trata entrada inválida (ex: letras no lugar de número)
    try:
        li_opcao_escolhida = int(input("Digite a opção escolhida: "))
    except ValueError:
        print("Por favor, digite um número inteiro válido!")
        continue # volta ao início do while sem executar o restante

    # OPÇÃO 1: ADICIONAR
    if li_opcao_escolhida == 1:
        try: 
            # .lower() padroniza para minúsculas; .strip() remove espaços extras
            ls_item = input("digite o item a ser adicionado: ").lower().strip()
            ls_item_quantidade = (int(input("digite quantas unidades do item você quer adicionar: ")))
            lf_valores = float(input("digite o valor de cada unidade do item que voce quer adicionar:  "))
            if  ls_item_quantidade <= 0 or lf_valores <=0:
                print()
                print("error: quantidade invalida de itens")
                print()
            elif ls_item in ls_lista_compras: # Impede duplicatas: mesmo nome não pode aparecer duas vezes
                print("Erro: item duplicado")

            else:
                # Adiciona nas três listas no mesmo índice
                ls_lista_compras.append(ls_item)
                ls_quantidades.append(ls_item_quantidade)
                lf_lista_valores.append(lf_valores)
        except ValueError:
            print("erro: digite um numero valido")

    # OPÇÃO 2: EDITAR
    elif li_opcao_escolhida == 2:

        ls_item = input("digite o item a ser editado: ").lower().strip()
        if ls_item not in ls_lista_compras:
            print("Erro: Item inexistente")
        else:
            try:
                ls_novo_item = input("Digite o novo item: ").lower().strip()
                print()
                li_nova_quantidade = int(input("Digite quantas unidades terão o item"))
                print()
                lf_novo_valor = float(input("Digite o valor de cada unidade: "))

                if li_nova_quantidade <= 0 or lf_novo_valor <= 0:
                    print("Erro: Quantidade e valor devem ser maiores que zero.")

                elif ls_novo_item in ls_lista_compras and ls_novo_item != ls_item: # Bloqueia duplicata, MAS permite manter o mesmo nome (só mudar qtd/valor)
                    print("Erro: item duplicado")

                else:
                    # .index() encontra a posição do item nas três listas
                    index = ls_lista_compras.index(ls_item)
                    ls_lista_compras[index] = ls_novo_item
                    ls_quantidades[index] = li_nova_quantidade
                    lf_lista_valores[index] = lf_novo_valor
                    print("Item editado com sucesso")
            except ValueError:
                print("Erro: Valor numérico inválido")
                  
             
    #OPÇÃO 3: REMOVER
    elif li_opcao_escolhida == 3:
        try:
            ls_item = input("digite o item a ser removido: ").lower().strip()
            index = ls_lista_compras.index(ls_item) # lança ValueError se não achar

            # Remove o mesmo índice nas três listas para mantê-las sincronizadas
            ls_lista_compras.pop(index )
            ls_quantidades.pop(index)
            lf_lista_valores.pop(index)
            print("Item removido com sucesso")
        except ValueError:
            print("Error: item não encontrado")
            
    # OPÇÃO 4: VISUALIZAR LISTA
    elif li_opcao_escolhida == 4:
        if (len(ls_lista_compras)) <= 0:
            print()
            print("não há itens na lista")
            print()
        else:
            print()
            for x in range (len(ls_lista_compras)):
                ls_item = ls_lista_compras[x]
                li_quantidade = ls_quantidades[x]
                lf_valor_compras = lf_lista_valores[x]

                # .capitalize() exibe a primeira letra maiúscula na saída
                ## :.2f formata o float com 2 casas decimais
                print(f"-- {ls_item.capitalize()}: {li_quantidade} unidades x R$ {lf_valor_compras:.2f} = R$ {lf_valor_compras * li_quantidade:.2f}")
            print()

    #OPÇÃO 5: VALOR TOTAL
    elif li_opcao_escolhida == 5:
        lf_valor_total = 0
        if (len(ls_lista_compras)) <= 0:
            print()
            print("não há itens na lista")
            print()
        else:

            # Percorre todas as posições e acumula: subtotal = preço × quantidade
            for x in range (len(ls_lista_compras)):
                li_quantidade = ls_quantidades[x]
                lf_valor_compras = lf_lista_valores[x]

                lf_subtotal = (lf_valor_compras)*(li_quantidade)
                lf_valor_total +=  lf_subtotal # acumula no total geral

            print(f"o valor total é de: {(lf_valor_total):.2f}") 
        
        
    #OPÇÃO 6: SAIR
    elif li_opcao_escolhida == 6:
        print("saindo da lista")
        break # encerra o loop while True

    else:
        print("erro: opção não conhecida")