
# ActivityControl API

Api para controle de atividades atraves de alunos, sendo ela realizando CRUD para as 3 entidades disponiveis atraves de endpoints.

Tarefa Realizada por: Erick Moreira Cassoli de Souza
## Indice

- [Funcionalidades](#funcionalidades)
- [Setup](#setup)
- [Uso](#uso)
- [Documentação da API](#documentação-da-api)

## Funcionalidades



## Setup

Execute o arquivo Setup.bat atraves do terminal usando:
```
.\Setup.ps1
```
Caso de algum erro use primeiro esse comando:
```
Set-ExecutionPolicy Bypass -Scope Process
```

e execute o Setup.ps1 novamente.

Ele criara a .env e intalara os requirements automaticamente.

Caso ele não execute os comandos vc pode tentar fazer isso manualmente utilizando 
```
python -m venv .env

.\.env\Scripts\activate

pip install -r requirements.txt
```
## Uso
Para iniciar a api utilize:

```
python manage.py makemigrations

python manage.py migrate

python manage.py runserver
```
após isso você pode fazer requisições atraves do postman ou da url em questão
a url padrão da api é localhost ou ```http://127.0.0.1:8000/```.

Apos isso voce pode importar as Colections da pasta "postmanCollections" para o seu proprio postman para testar.

## Documentação da API

### Retorna todos os alunos

```http
GET /api/alunos/
```

### Retorna um aluno específico

```http
GET /api/alunos/${id}/
```

| Parâmetro | Tipo   | Descrição             |
| --------- | ------ | -------------------- |
| `id`      | `int`  | **Obrigatório**. ID do aluno desejado |

