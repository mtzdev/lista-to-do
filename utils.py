import json
import os
from time import sleep

class DataManager:
    @staticmethod
    def load_data():
        with open('data.json', 'r') as f:
            data = json.load(f)
            return data

    @classmethod
    def save_data(cls, data: dict = None, login: str = None, key: str = None, value = None):
        if data is None and key:
            data = cls.load_data()

            if (isinstance(value, list) and len(value) == 0):       # Caso seja passado uma lista vazia
                data[login][key] = []
            else:
                data[login][key] = value

        with open('data.json', 'w') as f:
            json.dump(data, f, indent=4)

class Authenticator:
    @staticmethod
    def login_existing_account(login: str, data: dict):
        pass_counter = 3
        while pass_counter > 0:
            password = input(f'Digite sua senha para a conta ({login}): ').strip()
        
            if password == data[login]["password"]:
                os.system('cls')
                print('Logado com sucesso!')
                sleep(1)
                os.system('cls')
                return {'login': login, 'tasks_list': data[login]["tasks"], 'history': data[login]["history"]}  
 
            pass_counter -= 1
            print(f'Senha incorreta! Você tem mais {pass_counter} tentativas!')
            sleep(1)
            os.system('cls')
        raise ValueError('ERRO! Você esgotou as tentativas de login!')
    
    @staticmethod
    def create_new_account(login, data: dict):
        password = input(f'Você não possui nenhuma conta cadastrada para o nickname: ({login})\nDigite uma senha para realizar o cadastro: ').strip()
        password2 = input('Confirme sua senha: ').strip()
        while password != password2:
            password2 = input('Senha incorreta! Confirme novamente sua senha: ')
        os.system('cls')

        data[login] = {}
        data[login]["password"] = password
        data[login].setdefault("tasks", [])
        data[login].setdefault("history", [])
        DataManager.save_data(data=data)

        print(f'Sucesso! Sua conta foi criada, anote os dados para não esquecer!\nLogin: {login}\nSenha: {password}')
        input('Aperte ENTER para continuar')
        os.system('cls')
        return {'login': login, 'tasks_list': [], 'history': []}        
    

    @staticmethod
    def auth(login: str):
        data = DataManager.load_data()
        if login in data:
            return Authenticator.login_existing_account(login, data)
        else:
            return Authenticator.create_new_account(login, data)
            

    @staticmethod
    def on_startup():
        login = input('Digite seu nickname: ').strip()
        return Authenticator.auth(login)