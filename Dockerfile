FROM python:3.7-stretch
MAINTAINER Rustam Iskenderov 'is.rustam@gmail.com'

# устанавливаем параметры сборки
RUN apt-get update && \
 apt-get install -y gcc make apt-transport-https ca-certificates build-essential

# проверяем окружение python
RUN python3 --version
RUN pip3 --version

# копируем все файлы из корня проекта в рабочую директорию
COPY . /app

# задаем рабочую директорию для контейнера
WORKDIR /app

# устанавливаем зависимости python
RUN pip install -r requirements.txt

# запускаем приложение Python
CMD ["python3", "/app/run.py"]