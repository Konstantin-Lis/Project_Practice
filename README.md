# Project_Practice

### Установка
1. Запустить rabbimq в Docker

`docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3.11-management`

2. Создать и активировать виртуальное окружение:

  `python -m venv venv`

  `venv\Scripts\activate`

3. Установить библиотеки

`pip install -r requirements.txt`
