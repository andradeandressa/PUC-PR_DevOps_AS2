# Imagem base do Python
FROM python:3.8-slim-buster

# Diretório de trabalho para a aplicação
WORKDIR /app

# Copia os arquivos de dependência para o diretório de trabalho
COPY requirements.txt .

# Instala as dependências
RUN pip3 install --no-cache-dir -r requirements.txt

# Copia todo o restante do diretório de trabalho para o contêiner
COPY . .

# Define a porta
EXPOSE 5000

# Executa a aplicação
CMD ["python3", "app.py"]