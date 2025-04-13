import os

restaurantes = ['Pizza', 'Sushi']

def exibir_nome_do_programa():
    print('𝕊𝕒𝕓𝕠𝕣 𝔼𝕩𝕡𝕣𝕖𝕤𝕤\n')

def exibir_opcoes():
    print('1. Cadastrar Restaurante')
    print('2. Listar Restaurante')
    print('3. Ativar Restaurante')
    print('4. Sair\n')

def finalizando_app():
    exibir_subtitulo('Finalizar App')

def voltar_ao_menu_principal():
    input('\nDigite uma tecla para voltar ao menu principal ')
    main()  

def exibir_subtitulo(texto):
    os.system('cls')
    print(texto)
    print()

def opcao_invalida():
    print('Opção Inválida!')
    voltar_ao_menu_principal()

def cadastrar_novo_restaurante():
    exibir_subtitulo('Cadastrar novo restaurante')
    nome_do_restaurante = input('Digite o nome do Restaurante que gostaria de cadastrar: ')
    restaurantes.append(nome_do_restaurante)
    print(f'Você cadastrou o restaurante {nome_do_restaurante} com sucesso!')
    voltar_ao_menu_principal()


def listar_restaurantes():
    exibir_subtitulo('Listando os restaurantes\n')
    for restaurante in restaurantes:
        print(f'.{restaurante}')
    voltar_ao_menu_principal()


def escolher_opcoes():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
    
        if opcao_escolhida == 1:
                cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
                listar_restaurantes()

        elif opcao_escolhida == 3:
                print('Ativar restaurante')
        elif opcao_escolhida == 4:
                finalizando_app()
        else :
                opcao_invalida()
    except:
        opcao_invalida()

def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcoes()

if __name__ == '__main__':
    main()
