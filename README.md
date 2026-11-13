Язык: python 3.13
LLM-бэкенд: Ollama
Библиотеки: openai, os

Убедитесь, что на вашем компьютере установлены и запущены:
1. Ollama с загруженной моделью
2. Docker Desktop

Запуск через Docker Compose (рекомендуемый способ):
```bash
docker compose run --rm ai-chat
```

Альтернативный запуск:
Сборка образа:
```bash
docker build -t ai-chat .
```
Запуск интерактивного контейнера:
```bash
docker run -it --rm --network host -e PYTHONIOENCODING=utf-8 ai-chat
```

Структура проекта:
chat.py #основной код консольного чата с LLM
requirements.txt #список python-зависимостей 
Dockerfile #инструкция для сборки docker-образа
docker-compose.yml #конфигурация запуска контейнера
