# NotifyHub

Тестовое задание для компании "Фабрика решений"

Из дополнительных задач сделанно:

- Cтраница со Swagger UI благодоря встроенной возможности FastAPI
- Docker-compose для запуска всех сервисов проекта одной командой

Комментарии:
1. Здесь нет никакой БД и брокеров сообщений (всё сделанно через переменные), в реальной разработке без них никак
2. Я не понял для чего и где нужно использовать внешнее API, которое я получил, поэтому ее тут нет
3. Если рассылка должна быть в будущем, то необходимо подождать до это времени для выпонения отпраки сообщения

## Функциональность

Приветствуем вас в NotifyHub – мощном инструменте для управления и отслеживания рассылок сообщений вашим клиентам. 
Этот проект предоставляет гибкий и удобный интерфейс для создания, управления и мониторинга рассылок, а также взаимодействия с внешним сервисом отправки сообщений.

- Создание, обновление и удаление клиентов
- Управление рассылками с указанием фильтров
- Получение общей и детальной статистики рассылок
- Асинхронная отправка сообщений с сбором статистики
- Обработка ошибок внешнего сервиса без влияния на стабильность работы


## Требования

- Python 3.8 или выше (Желательно Python 3.11)
- Docker, Docker-Compose (для запуска в контейнере)

## Запуск локально

1. Скачать проект
```bash
git clone https://github.com/geoCrock/NotifyHub.git
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

Проект доступен по адресу: http://127.0.0.1:8000
   

## Запуск через Docker

1. Скачать проект
 ```bash
git clone https://github.com/geoCrock/NotifyHub.git
```

2. Перейти в корень проекта   
```bash
cd NotifyHub
```

3. Запустить контейнер
```bash
docker-compose up --build
```
Проект доступен по адресу: http://127.0.0.1:8000
