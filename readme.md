## news_drf
Project news_drf endpoints:

###  Получения списка новостей по методу GET --> https://jibek123.pythonanywhere.com/news/
###  Получения новости (detail) по методу GET --> https://jibek123.pythonanywhere.com/news/1/
###  Создания новости (add) по методу POST --> https://jibek123.pythonanywhere.com/news/add/
##### Пример json строки для добавления новости
#### 
        { 
            "title": "title 123",
            "description": "description 123",
            "published": false
        }
#### 
###  Обновления новости (update) по методу POST --> https://jibek123.pythonanywhere.com/news/1/update/
##### Пример json строки для обновления новости
#### 
        { 
            "title": "title 1234",
            "description": "description 1234",
            "published": true
        }
###  Удаления новости (delete) по методу DELETE --> https://jibek123.pythonanywhere.com/news/1/delete/