# YaCut :scissors:

## Оглавление
- [YaCut :scissors:](#yacut-scissors)
  - [Оглавление](#оглавление)
  - [Используемые технологии](#используемые-технологии)
  - [Структура проекта](#структура-проекта)
  - [Описание проекта](#описание-проекта)
  - [Заполнение конфигурационного .env файла](#заполнение-конфигурационного-env-файла)
  - [Запуск проекта](#запуск-проекта)

## Используемые технологии
:snake: Python 3.8, Flask 2.0.2, Sqlalchemy 1.4.29, Wtforms 3.0.1, Flask-migrate 3.1.0, Jinja2 3.0.3, :snowflake: flake8

## Структура проекта
```
yacut:
  ├── __pycache__
          └── ...
  ├── tests
       ├── __pycache__
       └── ...
  ├── venv
  ├── yacut
       ├── __pycache__
       ├── static
       ├── templates
       ├── __init__.py
       ├── api_views.py
       ├── constants.py
       ├── error_handlers.py
       ├── forms.py
       ├── models.py
       └── views.py
  ├── .env
  ├──.flake8
  ├── .gitignore
  ├── openapi.yml
  ├── pytest.ini
  ├── README.md
  ├── requirements.txt
  └── settings.py
```

## Описание проекта
Проект YaCut — это сервис укорачивания ссылок. Его назначение — ассоциировать длинную пользовательскую ссылку с короткой, которую предлагает сам пользователь или предоставляет сервис.

Ключевые возможности сервиса:
 - генерация коротких ссылок и связь их с исходными длинными ссылками;
 - переадресация на исходный адрес при обращении к коротким ссылкам.

Пользовательский интерфейс сервиса — одна страница с формой. Эта форма состоит из двух полей:
 - поле для длинной исходной ссылки (обязательное для заполнения);
 - поле для пользовательского варианта короткой ссылки (необязательное для заполнения).

Пользовательский вариант короткой ссылки не должен превышать 16 символов.

[:top: Вернуться к оглавлению](#оглавление)


## Заполнение конфигурационного .env файла

```
FLASK_APP=yacut
FLASK_ENV=development
DATABASE_URI=ChooseDataBase
SECRET_KEY=Your!$ecretKey8

Example:
DATABASE_URI=sqlite:///db.sqlite3
```

## Запуск проекта
1. Клонировать репозиторий:
```bash
git clone https://github.com/simatheone/yacut.git
```

2. Создать и активировать виртуальное окружение и :
```bash
python3 -m venv venv

bash/zsh
source venv/bin/activate

Windows:
venv\Scripts\activate.bat
```

3. Обновить pip и установить зависимости из ```requirements.txt```
```bash
python3 -m pip install --upgrade pip

pip install -r requirements.txt
```

4. Создать и заполнить файл **.env** в соответствии с [рекомендациями](#заполнение-конфигурационного-env-файла):

```bash
touch .env
```

5. Выполнить миграции:
```bash
flask db init
flask db migrate -m "короткое сообщение"
flask db upgrade
```

6. Запустить проект:
```bash
flask run
```

После запуска проект будет доступен по адресу: http://127.0.0.1:5000

[:top: Вернуться к оглавлению](#оглавление)


**Автор проекта:** [Alexander Sviridov](https://github.com/simatheone/)

**Pytests:** [YandexPracticum](https://github.com/yandex-praktikum/scrapy_parser_pep/tree/main/tests)
