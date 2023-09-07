import os
from time import sleep
from utils import DataManager, Authenticator

class Tarefas:
    def __init__(self, login, tasks_list = [], history = []):
        self._login = login        # protected 
        self._tasks_list = tasks_list     # protected
        self._history = history       # protected
    
    def list_controller(self, task):
        task = task.strip()
        if task in self._tasks_list:
            self._tasks_list.remove(task)
            self._history.append(task)
            DataManager.save_data(login=self._login, key='tasks', value=self._tasks_list)
            DataManager.save_data(login=self._login, key='history', value=self._history)
            return f'✔ Sucesso! A tarefa "{task}" foi removida da lista'
        else:
            self._tasks_list.append(task)
            if task in self._history:
                self._history.remove(task)
            DataManager.save_data(login=self._login, key='tasks', value=self._tasks_list)
            DataManager.save_data(login=self._login, key='history', value=self._history)
            return f'✔ Sucesso! A tarefa "{task}" foi adicionada a lista'
    
    def desfazer(self):
        if self._tasks_list:
            task = self._tasks_list.pop(-1)
            self._history.append(task)
            DataManager.save_data(login=self._login, key='tasks', value=self._tasks_list)
            DataManager.save_data(login=self._login, key='history', value=self._history)
            return f'✔ Sucesso! Você removeu a última tarefa ({task})!'
        else:
            return '⚠ Não há nenhuma tarefa na lista para desfazer!'

    def refazer(self):
        if self._history:
            task = self._history.pop(-1)
            self._tasks_list.append(task)
            DataManager.save_data(login=self._login, key='tasks', value=self._tasks_list)
            DataManager.save_data(login=self._login, key='history', value=self._history)
            return f'✔ Sucesso! Você re-adicionou a tarefa ({task})!'
        else:
            return '⚠ Não há nenhuma tarefa no histórico para refazer!'

    @property
    def get_tasklist(self):
        if self._tasks_list:
            return '\n'.join([f'{num}: {i}' for num, i in enumerate(self._tasks_list, start=1)])
        else:
            return '⚠ A lista de tarefas está vazia!'

    @classmethod
    def create_user_data(cls):
        try:
            dados = Authenticator.on_startup()
            return cls(**dados) 
        except ValueError as e:
            print(f'ERRO! {e}')
            exit(1)


def main():
    task_control = Tarefas.create_user_data()
    comandos = {
        "desfazer": lambda: task_control.desfazer(),
        "refazer": lambda: task_control.refazer()
    }
    
    while True:
        os.system('cls')
        print(f'Olá {task_control._login}! Para adicionar/remover uma tarefa da lista basta digitar o nome dela!\nOutros comandos disponíveis: desfazer - refazer\n\nLista atual:\n{task_control.get_tasklist}')
        command = input('\nDigite um comando: ')
        if command.lower() in comandos:
            print(comandos[command]())
        else:
            print(task_control.list_controller(command))
        sleep(1.0)

if __name__ == "__main__":
    main()
