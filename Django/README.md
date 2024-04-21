

# Django

[Django](https://www.djangoproject.com/start/overview/) is a high-level Python web framework that follows the model-view-template architectural pattern.

## Install Django

Django can be installed using pip, which is a package manager for Python. Here are the steps to install Django:

`pip install django`


### Start Django Project


```bash
django-admin startproject myproject location
```


## Django Apps

Django apps are Python modules that contain models, views, and other code.


### Start Django App

```bash
django-admin startapp myapp location
```

## Start Django Server

```bash
python manage.py runserver
```


<!-- How urls works -->

## Urls

Django provides a way to map URLs to views. Here's an example of mapping a URL to a view:

```python
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]
```

How to include apps in urls

```python
from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('myapp/', include('myapp.urls')),
]
```

<!-- How views works  -->

## Views

Django provides a way to define views. Here's an example of defining a view:
view is a function that takes a request and returns a response.

```python
from django.shortcuts import render
def index(request):
    return render(request, 'index.html')
```



## Models

Django Models are used to store data in a database. Here's an example of defining a model:

```python
from django.db import models
class Person(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
```


## Static and Media Files

Django uses a concept called "static files" to manage and serve static content like CSS, JavaScript, and images. It also provides a way to serve files uploaded by users, like images or documents.

To serve static files, you need to configure a "static files" directory and a "media files" directory in your settings.py file. Here's an example:


```PYTHON

    # settings.py
    STATIC_URL = '/static/'
    STATIC_ROOT = BASE_DIR / 'static'
    STATICFILES_DIRS = [
        BASE_DIR / 'staticfiles',
    ]

    MEDIA_URL = '/media/'
    MEDIA_ROOT = BASE_DIR / 'media'


    # urls.py
    from django.conf import settings
    from django.conf.urls.static import static

    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

```






