Этот HTTP POST-запрос используется для 
разбора изображений через конечную точку 
{{baseURL}}/api/parse_images/. Запрос должен быть отправлен 
с form-data в качестве типа тела запроса, включая параметры 
"images" и "csv_file", оба типа file. При успешном выполнении 
API возвращает код состояния 200, а также информацию о грузовом 
пространстве, сведения о грузе и список распакованных предметов в теле ответа.

Ссылка на postman-collection
https://api.postman.com/collections/31515047-baee5b5b-2aab-4939-bcf3-c60a261b3b90?access_key=PMAT-01HK0B2YQJMQ69MHKA16WEV5B0

В данно приложении используется протокол REST API:

POST{{baseURL}}/api/parse_images/

Что передает изображения ящиков в переменной images.png
и file.csv что передает координаты, на сайт где пользователю
необходимо пройти авторизацию загрузить файлы, нажать кнопку рассчитать
и скачать объединенный.json файл с расчетами

# Инструкция, как вручную развернурть проект

При оишбках возможно использование 
WSL (Windows Subsystem for Linux) 
https://learn.microsoft.com/ru-ru/windows/wsl/install

0. Необходимо иметь: python, python-dev, pip, venv/pipenv, python IDE (VSCode / PyCharm)

1. Создайте файл с переменными окружения:

```
cp example.env .env
```

2. Активируйте виртуальное окружение:

* Если у вас установлен venv:

    + Для Unix, MacOS:

```

python -m venv .
sudo chmod -R 777 bin/
source bin/activate

```
*
    + Для Windows:

```

python -m venv .
Scripts/activate

```

* Если у вас установлен pipenv:

```

pipenv shell

```

3. Установите необходимые зависимости python

* venv:

```
pip install -r requirements.txt
```

* pipenv:

```
pipenv install -r requirements.txt
```

4. Примените миграции:

```
python backend/manage.py migrate
```

5. Создайте учетную запись администратора:

```
python backend/manage.py createsuperuser
```

6. Запустите сервер django, чтобы убедиться, что все работает:

```
python backend/manage.py runserver

```

Затем откройте указанный в консоли адрес в браузере. Если все прошло успешно, вы увидите приветственное окно.
