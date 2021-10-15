# YaMDb API
##### В этом проекте реализован API для небольшой социальной сети YaMDb. В YaMDb пользователи могут писать рецензии к различным произведениям (книги, музыка, фильмы и т.д.), а также оставлять к рецензиям комментарии. Сами произведения в YaMDb не хранятся.  

### Больше информации:
Подробную документацию к API вы можете найти после запуска проекта по адресу http://127.0.0.1:8000/redoc/

### Как запустить проект:
Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/4uku/api_yamdb.git
```

```
cd api_yamdb
```

Cоздать и активировать виртуальное окружение:

```
python -m venv venv
```

```
source venv/Scripts/activate
```

Установить зависимости из файла requirements.txt:

```
python -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python manage.py migrate
```

Запустить проект:

```
python manage.py runserver
```
##### Для добавления данных из ```csv``` файлов в базу в следующем порядке выполнить:
```
python manage.py add_user users.csv
python manage.py add_category category.csv
python manage.py add_genre genre.csv
python manage.py add_title titles.csv
python manage.py add_review review.csv
python manage.py add_comment comments.csv
```
