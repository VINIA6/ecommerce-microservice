# Usar a imagem oficial do Python
FROM python:3.9-slim

# Definir o diretório de trabalho no container
WORKDIR /app

# Copiar o arquivo de dependências
COPY requirements.txt .

# Instalar as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o código para o container
COPY ./src .

# Definir o PYTHONPATH para garantir que o diretório seja reconhecido
ENV PYTHONPATH=/app

# Expor a porta do FastAPI
EXPOSE 8000

# Comando para iniciar o serviço
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
