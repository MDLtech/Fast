# FastApi Insurance
### Для запуска проекта необходимо иметь Docker.
1. Скопируйте репозиторий командой `git clone https://github.com/MDLtech/Fast . `
1. Запустите контейнеры командой `docker-compose up --build -d`


## Методы

### POST /update_tariffs/
- В теле запроса необходимо передать JSON <br/>
Пример JSON `{
    "2023-07-01": [
        {
            "cargo_type": "Glass",
            "rate": "0.05"
        }
        ]
      }`
<br/> В нём мы передаём ключом дату, внутри коллекцию тарифов для данной даты <br/>
В случае успешного обновления получаем
`{"message": "Tariffs updated successfully."}`

### GET /insurance_cost/
Параметры
1. **cost** - стоимость
1. **tariff** - название тарифа
1. **date** - Необязательный параметр, по умолчанию сегодняшняя дата.
<br/><br/>Пример запроса https://127.0.0.1:8000/insurance_cost/?cost=1000&tariff=Glass&date=2023-07-01 <br/> В ответ получим
`{
    "insurance_cost": 50.0
}`
<br/>Если коэффицент на указанный тариф и дату составляет 0.05
