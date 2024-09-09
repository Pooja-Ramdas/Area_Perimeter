# PharmaLink

To Run project on your PC 

Proceed through each step in order :

First , Install `virtualenv` using `pip`

`pip install virtualenv`

Create Virtual Enviroment using virtualenv 

`virtualenv venv`

Activate Virtual Environment using 

`venv\scripts\activate` for Windows

Install all requirements using 

`pip install -r requirements.txt`

To initialize Project , use 

`python manage.py migrate`

To Run Project 

`python manage.py runserver`

Make sure to create `.env` file 

In .env file , Write 

```
SECRET_KEY = <your-secret-key>
```

To create Secret key , Use this script 

```
from django.core.management.utils import get_random_secret_key

print(get_random_secret_key())
```

You will get some output like `django-insecure <some-random-numbers` , That will be your secret key. 


Use `python manage.py add_sample_drugs` command to add sample drugs to database