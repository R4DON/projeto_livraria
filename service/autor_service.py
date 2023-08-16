from dao.autor_dao import AutorDAO
from model.autor import Autor


class AutorService:

    def __init__(self):
        self.__autor_dao: AutorDAO = AutorDAO()

    @property
    def autor_dao(self) -> AutorDAO:
        return self.__autor_dao

    def menu(self):
        print('[autors] Escolha uma das seguintes opções:\n'
              '1 - Listar todos autores\n'
              '2 - Adicionar novo/a autor\n'
              '3 - Excluir autor/a\n'
              '4 - Ver autor/a por Id\n'
              '0 - Voltar ao menu anterior\n')
        escolha = input('Digite a opção: ')

        if escolha == '0':
            return
        if escolha == '1':
            self.listar()
        elif escolha == '2':
            self.adicionar()
        elif escolha == '3':
            self.remover()
        elif escolha == '4':
            self.mostrar_por_id()
        else:
            print('Opção inválida! Por favor, tente novamente!')

        self.menu()

    def listar(self):
        print('\nListando autores...')

        try:
            autores = self.__autor_dao.listar()
            if len(autores) == 0:
                print('Nenhuma autor encontrada!')

            for autor in autores:
                print(
                    f'{autor.id} | {autor.nome} | {autor.email} | {autor.telefone} | {autor.bio} ')
        except Exception as e:
            print(f'Erro ao exibir as autors! - {e}')
            return

        input('Pressione uma tecla para continuar...')

    def adicionar(self):
        print('\nAdicionando autor...')

        try:
            id = self.__autor_dao.ultimo_id() + 1
            nome = input('Digite o nome da autor: ')
            email = input('Digite o email do autor: ')
            telefone = input('Digite o Telefone do autor: ')
            bio = input('Digite uma bio reduzida do autor: ')
            novo_autor = Autor(id, nome, email, telefone, bio)
            self.__autor_dao.adicionar(novo_autor)
            print('autor adicionada com sucesso!')
        except Exception as e:
            print(f'Erro ao inserir autor! - {e}')
            return

        input('Pressione uma tecla para continuar...')

    def remover(self):
        print('\nRemovendo autor...')

        try:
            autor_id = int(
                input('Digite o ID da autor para excluir: '))
            if (self.__autor_dao.remover(autor_id)):
                print('autor excluída com sucesso!')
            else:
                print('autor não encontrada!')
        except Exception as e:
            print(f'Erro ao excluir autor! - {e}')
            return

        input('Pressione uma tecla para continuar...')

    def mostrar_por_id(self):
        print('\nautor por Id...')

        try:
            id = int(input('Digite o Id da autor para buscar: '))
            aut = self.__autor_dao.buscar_por_id(id)

            if (aut == None):
                print('autor não encontrada!')
            else:
                print(f'Id: {aut.id} | autor: {aut.nome}')
        except Exception as e:
            print(f'Erro ao exibir autor! - {e}')
            return

        input('Pressione uma tecla para continuar...')
