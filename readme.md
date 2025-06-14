Платформа питомника включает в себя разделы:

породы
собаки
пользователи
отзывы
Виртуальное окружение используемое для проекта: 
--venv

После настройки виртуального окружения установите зависимости из файла requirements.txt
--pip install -r requirements.txt
Заполните .env файл согласно файла .env_sample
Создайте базу данных при помощи команды
python manage.py create_db
Создайте миграции при помощи команды
python manage.py makemigrations
Примените созданные миграции
python manage.py migrate
Выполните команду для создания основных пользователей
python manage.py comand_create_super_user
Выполните команду для заполнения базы данных
python manage.py loaddata dogs.json
Выполните команду для запуска redis сервера
redis-server
Выполните команду для запуска приложения, желательно в отдельном терминале
python manage.py runserver