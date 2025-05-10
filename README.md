# Miniblog-Flask

Link da aplicação - https://miniblog-flask.onrender.com

![image](https://github.com/user-attachments/assets/14cb5f50-07e2-4f47-8606-d9d48f93c072)


![image](https://github.com/user-attachments/assets/3eda24a8-1134-4c70-90e5-caa9e4d8694e)


## Instalar as dependências 
```sh
pip install -r requirements.txt
```

## Para rodar a aplicação 

```sh
python run.py

```


## Para teste com Docker 
```sh
docker compose up --build
```

# Criar migratiosn 
```sh
flask db init

flask db migrate -m "Criação das tabelas User e Book"

flask db upgrade
```

# Visualizar o banco de dados 

```sh
psql -U nome_do_usuario
```