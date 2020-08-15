# Учебный проект ч.2

Фронт для отправки данных в готовую модель машинного обучения и получения результатов предсказания

Данный проект упакован в докер-контейнер и разворачивается командой:
``` 
docker pull irustam/mlprojectcarpricefront:latest
```

Запуск контейнера осуществляется командой:
``` 
docker run --rm -e "MODEL_URL=http://localhost:5000/api/predict/" -e "SECRET_API_KEY=K6ASUGFIuGW3IE839239gASJH" -it -p 5001:5001 irustam/mlprojectcarpricefront:latest
```
Вместо __localhost:5000__ из команды запуска укажите хост и порт, где развернут контейнер с моделью.

Контейнер с моделью по ссылке https://github.com/irustam/ml-for-business/tree/project