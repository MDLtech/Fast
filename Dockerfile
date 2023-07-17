# Используем базовый образ Python
FROM python:3.9.5

# Устанавливаем переменные окружения для PostgreSQL
ENV POSTGRES_USER=postgres
ENV POSTGRES_PASSWORD=admin
ENV POSTGRES_DB=tarrifs
ENV POSTGRES_HOST=db

# Устанавливаем рабочую директорию в контейнере
WORKDIR /app

# Копируем зависимости проекта в контейнер
COPY requirements.txt .

# Устанавливаем зависимости проекта
RUN pip install --no-cache-dir -r requirements.txt

# Копируем исходный код проекта в контейнер
COPY . .

# Запускаем приложение FastAPI
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]