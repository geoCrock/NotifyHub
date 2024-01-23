# NotifyHub

Тестовое задание для компеании "Фабрика решений"

Из дополнительных задач сделанно:

- Cтраница со Swagger UI благодоря встроенной возможности FastAPI 

Приветствуем вас в Сервисе Рассылок – мощном инструменте для управления и отслеживания рассылок сообщений вашим клиентам. 
Этот проект предоставляет гибкий и удобный интерфейс для создания, управления и мониторинга рассылок, а также взаимодействия с внешним сервисом отправки сообщений.

## Функциональность

- Создание, обновление и удаление клиентов
- Управление рассылками с указанием фильтров
- Получение общей и детальной статистики рассылок
- Асинхронная отправка сообщений с сбором статистики
- Обработка ошибок внешнего сервиса без влияния на стабильность работы


## Требования

- Python 3.8 или выше
- Docker, Docker-Compose (для запуска в контейнере)

## Запуск локально

1. Скачать проект
```bash
https://github.com/geoCrock/NotifyHub.git
```

2. Перейти в корень проекта   
```bash
cd NotifyHub
```

3. Установить зависимости
```bash
pip install -r requirements.txt
```

4. Запустить главный файл `main.py` для запуска проекта
```bash
main.py
```

5. Проект доступен по адресу: http://127.0.0.1:8000
   

## Запуск через Docker

1. Скачать проект
```bash
https://github.com/geoCrock/NotifyHub.git
```

2. Запустить контейнер
```bash
docker-compose up --build
```
3. Проект доступен по адресу: http://127.0.0.1:8000

