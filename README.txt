start commands 

git clone https://github.com/TarlexGit/DjangoPollsApp.git
cd pollApp
python manage.py makemigrations
python manage.py migrate 

python manage.py createsuperuser

добаить грумму для администраторов с набором разрешений
python manage.py add_admins

под супером или через 'python manage.py shell' можно добаить админов и создавать ими опросы через админку

API DOC

Авторизация юзера - получение токена 
POST http://127.0.0.1:8000/users/token/
body - raw
{
    "username": "admin",
    "password": "admin"
}

получение опросов (название, пк)
GET http://127.0.0.1:8000/polls/pollsets/

Получение всех вопросов с полем айдишника опроса (poll_set)
GET http://127.0.0.1:8000/polls/questions/

То же самое, только с фильтром 
GET http://127.0.0.1:8000/polls/poll/
GET http://127.0.0.1:8000/polls/poll/?poll_set=1

Ответ пользователя на вопрос 
POST http://127.0.0.1:8000/polls/answer/
body - raw
{
    "poll_set":1,
    "answers": {"1":[1] }
}
На два вопроса, второй с несколькими вариантами 
POST http://127.0.0.1:8000/polls/answer/
body - raw
{
    "poll_set":1,
    "answers": {"1":[1], "2":[4,5]}
}

* при авторизованном юзере в authorization (postman) добавить Bearer Token и значение токена от логина,
* анонимные юзеры получают куки (http-only)


Получение ответов юзера (та же логика из **)
GET http://127.0.0.1:8000/polls/user/answer/