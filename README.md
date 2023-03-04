# django_hillel_tutorial
_This is an app from [Django tutorial](https://docs.djangoproject.com/en/4.0/intro/tutorial01/)._
_You may run it using this steps:_
* Clone the repo
* Install requirements
* Create environment variable with command:

``` export DJANGO_SECRET_KEY=<your_value>```

* Run commands to create the database tables:

```python manage.py makemigrations```

```python manage.py migrate```
* Create a superuser:

```python manage.py createsuperuser```
_You should enter username, email and password. For example: ```admin, admin@example.com, <your_password>```._
* Run server:

``` python manage.py runserver```
* Now you can see two pages:

_/polls/ page and /admin/ page._

_But polls page has no question yet_
* To create a question run commands:

``` python manage.py shell```

``` from polls.models import Question, Choice```

``` from django.utils import timezone```

``` q = Question(question_text="<Your question>?", pub_date=timezone.now())```

``` q.save()```
* To create choices run commads:

``` q.choice_set.create(choice_text='<Your text>', votes=0)```

_Create as many choices as you want. Then look at polls and admin pages._
