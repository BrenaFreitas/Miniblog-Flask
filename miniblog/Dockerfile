# Use a imagem base oficial do Python
FROM python:3.9-slim

# Define o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copia o arquivo de requisitos para instalar dependências
COPY requirements.txt .

# Instala as dependências do PostgreSQL
RUN apt-get update && apt-get install -y libpq-dev postgresql-client


# Instala as dependências do Python
RUN pip install --no-cache-dir -r requirements.txt

# Copia todo o código da aplicação para o contêiner
COPY . .

# Expõe a porta que o Flask usará
EXPOSE 8000

# Define o comando padrão para rodar a aplicação
CMD ["flask", "run", "--host=0.0.0.0"]
