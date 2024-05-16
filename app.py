import os

restaurantes =  [{'Nome': 'Praca', 'Categoria' : 'Japones', 'Ativo' : False},
                 {'Nome': 'Pizza Suprema', 'Categoria' : 'Italiana', 'Ativo' : True},
                 {'Nome': 'Sushi Bar', 'Categoria' : 'Japones', 'Ativo' : False}
                ]

def exibir_nome_do_programa():
    print('\n丂闩⻏ㄖ尺 㠪〤尸尺🝗丂丂\n')

def exibir_opcoes():
    print('1- Cadastrar restaurante')
    print('2- Listar restaurante')
    print('3- Ativar restaurante')
    print('4- Sair\n')

def finalizar_app():
    exibir_subtitulo('Obrigado por utilizar nosso Aplicativo')

def voltar_ao_menu_principal():
    input('\nDigite uma tecla para voltar ao menu Principal  ')
    main()

def opcao_invalida():
    os.system('cls')
    print('Opcao invalida, tente novamente!\n')
    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    os.system('cls')
    linha = '*' * (len(texto) + 4)
    print(linha)
    print(texto)
    print(linha)
    print()

def cadastrar_novo_restaurante():
    exibir_subtitulo('Cadastro de novo Restaurante')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja acadastrar: ')
    categoria = input(f'Digite a categoria do restaurante {nome_do_restaurante}: ')
    dados_do_restaurante = {'Nome': nome_do_restaurante, 'Categoria': categoria, 'Ativo': False}
    restaurantes.append(dados_do_restaurante)
    print(f'O Restaurante {nome_do_restaurante} foi Cadastrado com Sucesso!')
    voltar_ao_menu_principal()

def listar_restaurantes():
    exibir_subtitulo('Listando os restaurantes')
    for restaurante in restaurantes:
        nome_restaurante = restaurante ['Nome']
        categoria = restaurante ['Categoria']
        ativo = 'Ativado' if restaurante ['Ativo'] else 'Desativado'
        print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}' )
    
    voltar_ao_menu_principal()

def alternar_estado_restaurante():
    exibir_subtitulo('Alternando estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alternar o estado: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['Nome']:
            restaurante_encontrado = True
            restaurante['Ativo'] = not restaurante['Ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante ['Ativo']  else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)
    if not restaurante_encontrado:
        print('O restaurante nao foi encontrado')        
    voltar_ao_menu_principal()

def escolher_opcoes():
    try:
        opcao_escolhida = int (input('Escolha uma opcao: '))
        print(f'Voce escolheu a opcao: {opcao_escolhida}')

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()    
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_estado_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except: opcao_invalida()

def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcoes()

if __name__ == '__main__':
    main()
