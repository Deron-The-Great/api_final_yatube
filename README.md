# API_FINAL_YATUBE
## Проект, демонстрирующий возможности Django Rest Framework



## В проекте реализовано:

- Создание и редактирование постов.
- Создание и редактирование комментариев к постам.
- Доступ ко всей информации, касающейся постов.
- Подписка на авторов постов.

## В проекте были использованы технологии:
- Python 3.9
- Django 2.2.16
- djangorestframework 3.12.4
- Pillow 8.3.1
- PyJWT 2.1.0
## Запуск проекта:
- Активируйте виртуальное окружение: py -m venv venv
- Подгрузите необходимые библиотеки: pip install -r requirements.txt
- Выполните миграции: py yatube_api/manage.py migrate
- Запустите сервер: py yatube_api/manage.py runserver
- Наслаждайтесь тестированием...
 
## Примеры запросов:
- GET http://127.0.0.1:8000/api/v1/posts/ ->  {"count": 123,"next":"http://api.example.org/accounts/?offset=400&limit=100","previous":"http://api.example.org/accounts/?offset=200&limit=100","results": [{}]}
- POST http://127.0.0.1:8000/api/v1/posts/ -> {"text": "string","image": "string","group": 0}

Больше примеров в документации: http://127.0.0.1:8000/redoc/
made by Шубин Сергей