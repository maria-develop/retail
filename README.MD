# Retail Network Management System

Это веб-приложение для управления сетью по продаже электроники. Оно включает в себя API-интерфейс и админ-панель для управления объектами сети (заводами, розничными сетями и индивидуальными предпринимателями), а также их продуктами.

## Основные функции

- **Иерархическая структура сети**: Заводы, розничные сети и индивидуальные предприниматели.
- **Управление объектами сети**:
  - Создание, чтение, обновление и удаление объектов.
  - Фильтрация объектов по стране.
  - Очистка задолженности перед поставщиком через админ-панель.
- **Управление продуктами**: Каждый объект сети может иметь список продуктов.
- **API-интерфейс**: CRUD-операции для объектов сети и продуктов.
- **Аутентификация и авторизация**: Доступ к API только для активных пользователей.

## Технологии

- **Python 3.8+**
- **Django 3+**
- **Django REST Framework (DRF) 3.10+**
- **PostgreSQL 10+**
- **JWT-аутентификация**

## Установка и настройка

### 1. Клонирование репозитория

git clone https://github.com/maria-develop/retail
cd retail-network-management

### 2. Установка зависимостей
Создайте виртуальное окружение и установите зависимости:

python -m venv venv
source venv/bin/activate  # Для Linux/MacOS
# venv\Scripts\activate    # Для Windows
pip install -r requirements.txt

### 3. Настройка базы данных
Создайте базу данных PostgreSQL и настройте подключение в файле config/settings.py:

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "ваша_база_данных",
        "USER": "ваш_пользователь",
        "PASSWORD": "ваш_пароль",
        "HOST": "localhost",
        "PORT": "5432",
    }
}
### 4. Применение миграций

python manage.py migrate

### 5. Создание суперпользователя

python manage.py csu

### 6. Запуск сервера

python manage.py runserver


Теперь приложение доступно по адресу: http://127.0.0.1:8000.

## Использование API
### Аутентификация
Для доступа к API используйте JWT-токен. Получите токен, отправив POST-запрос на /users/login/ с email и паролем:
curl -X POST http://127.0.0.1:8000/users/login/ \
    -H "Content-Type: application/json" \
    -d '{"email": "ваш_email", "password": "ваш_пароль"}'

Ответ будет содержать access и refresh токены:
{
    "refresh": "ваш_refresh_токен",
    "access": "ваш_access_токен"
}

Используйте access токен для авторизации в API:
curl -X GET http://127.0.0.1:8000/retails/ \
    -H "Authorization: Bearer ваш_access_токен"

Примеры запросов
Получение списка объектов сети
curl -X GET http://127.0.0.1:8000/retails/ \
    -H "Authorization: Bearer ваш_access_токен"

Создание нового объекта сети
curl -X POST http://127.0.0.1:8000/retails/create/ \
    -H "Authorization: Bearer ваш_access_токен" \
    -H "Content-Type: application/json" \
    -d '{
        "type": "retail",
        "name": "Retail 2",
        "email": "retail2@example.com",
        "country": "Country 3",
        "city": "City 3",
        "street": "Street 3",
        "house_number": "3",
        "supplier": 1
    }'

Фильтрация объектов по стране
curl -X GET http://127.0.0.1:8000/retails/?country=Country%201 \
    -H "Authorization: Bearer ваш_access_токен"

## Админ-панель
Админ-панель доступна по адресу: http://127.0.0.1:8000/admin. Используйте учетные данные суперпользователя для входа.

Возможности админ-панели:
1. Просмотр и редактирование объектов сети и продуктов.
2. Фильтрация объектов по городу.
3. Очистка задолженности перед поставщиком для выбранных объектов.

## Тестирование
Текущее покрытие тестами: 88%.