# Учебный проект ч.1

Здесь находится предобученная модель для предсказания стоимости авто.

Для обучения модели использован датасет https://www.kaggle.com/CooperUnion/cardataset

Данный проект упакован в докер-контейнер и разворачивается командой:
``` 
docker pull irustam/mlprojectcarpriceback:latest
```

Запуск контейнера осуществляется командой:
``` 
docker run --rm -e "SECRET_API_KEY=K6ASUGFIuGW3IE839239gASJH" -it -p 5000:5000 irustam/mlprojectcarpriceback:latest
```
Для отправки данных в модель используйте форму на фронте. Подробнее тут https://github.com/irustam/ml-for-business/tree/project_front

Другой вариант проверки - использовать скрипт test_run.py из папки test_this_model
Тестовые данные в той же папке test_this_model