# Create a Django project
django-admin startproject HelloWorld

## 目录说明：

HelloWorld: 项目的容器。
manage.py: 一个实用的命令行工具，可让你以各种方式与该 Django 项目进行交互。
HelloWorld/__init__.py: 一个空文件，告诉 Python 该目录是一个 Python 包。
HelloWorld/settings.py: 该 Django 项目的设置/配置。
HelloWorld/urls.py: 该 Django 项目的 URL 声明; 一份由 Django 驱动的网站"目录"。
HelloWorld/wsgi.py: 一个 WSGI 兼容的 Web 服务器的入口，以便运行你的项目。

## Startup Server
python manage.py runserver 0.0.0.0:8000


### set first view.

templates/hello.html
``` html
<h1>{{ hello }}</h1>
```

update templates config in 'settings.py'
```
...
TEMPLATES = [
    {
        ...
        'DIRS': [BASE_DIR + "/templates", ],
        ...
    }
    ...
    ]
...
```


view.py
``` python
from django.shortcuts import render

def hello(request):
    # return HttpResponse("Hello World!")
    context = dict()
    context["hello"] = "Hello world!"
    return render(request, "hello.html", context)
```

add url patterns to 'urls.py'
``` python
...
url(r'^$', view.hello)
...
```


### for templates extend, view 'base.html' and 'extend.html'


# Start app for Django

Install mysql connector
``` shell
pip install mysqlclient
```

Update mysql setting in 'settings.py'
``` python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # 或者使用 mysql.connector.django
        'NAME': 'test',
        'USER': 'test',
        'PASSWORD': 'test123',
        'HOST':'localhost',
        'PORT':'3306',
    }
}

```

Create an app
``` shell
django-admin.py startapp TestModel

```

Define model in 'models.py'. ClassName => TableName, PropertyName => ColumnName.

Add the app to INSTALLED_APPS in 'settings.py'

Create tables
``` shell
python manage.py migrate   # 创建表结构

python manage.py makemigrations TestModel  # 让 Django 知道我们在我们的模型有一些变更
python manage.py migrate TestModel   # 创建表结构
```


python manage.py createsuperuser



## uwsgi django

uwsgi uwsgi-8000.ini

kill process : kill -9 $(cat uwsgi.pid )

### error
- invalid request block size: 21573 (max 4096)...skip
    - usgi参数-s表示以socket方式提供通信端口，默认的协议是tcp.通过浏览器访问使用的协议是http.