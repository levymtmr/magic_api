# Use uma imagem base oficial do Python
FROM python:3.10-slim

# Defina o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copie o arquivo de dependências e instale-as
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copie o restante do código-fonte para o contêiner
COPY . .

# Exponha a porta em que o Flask será executado
EXPOSE 5000

# Comando para iniciar a aplicação usando o servidor de desenvolvimento do Flask
# CMD ["flask", "run", "--host=0.0.0.0"]