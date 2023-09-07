# To-Do App em Python

Um aplicativo desenvolvido em Python de lista de tarefas com recursos diferenciais. Ele permite que os usuários criem, gerenciem, desfaçam e refaçam tarefas da sua lista de tarefas. O aplicativo salva os dados em formato json, e também possui a funcionalidade de autenticação de usuários.

## Recursos:
- **Adicionar Tarefas:** Adicione tarefas à sua lista de tarefas digitando o nome da tarefa.
- **Remover Tarefas:** Remova tarefas da lista digitando o nome da tarefa existente.
- **Desfazer:** Desfaça a última ação realizada (remover tarefa).
- **Refazer:** Refaça a última ação desfeita.
- **Autenticação de Usuário:** O aplicativo permite que os usuários se autentiquem usando um nome de usuário exclusivo. Os dados do usuário são salvos em arquivos JSON separados para persistência dos dados.

## Pré-requisitos
- Python 3.x

## Instalação
1. Clone o repositório usando:
```bash
git clone https://github.com/mtzdev/lista-to-do.git
```
2. Acesse o diretório do projeto:
```bash
cd lista-to-do
```
3. Execute o aplicativo:
```bash
python main.py
```

## Uso
- Ao iniciar o aplicativo, você precisa inserir seu nome de usuário. Caso seja um novo usuário, será criada uma nova conta. Se você já possuir uma conta, seu histórico de tarefas será carregado.
- Após a autenticação, você pode adicionar, remover, desfazer e refazer tarefas usando os comandos.
- Para adicionar ou remover uma tarefa basta digitar o nome da tarefa.
- Para refazer ou desfazer, use os comandos **"desfazer"** ou **"refazer"**.
- Para sair do aplicativo, pressione **CTRL+C** ou feche o aplicativo.

## Contribuições e Licença
Este é um projeto de código aberto, sinta-se a vontade de melhorar o código, abrir problemas ou enviar solicitações de pull!
<br>
Este projeto é licenciado sob a Licença MIT. Consulte o arquivo [LICENSE](https://github.com/mtzdev/lista-to-do/blob/main/LICENSE) para obter detalhes.
