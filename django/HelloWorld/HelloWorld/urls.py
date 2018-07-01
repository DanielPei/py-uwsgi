"""HelloWorld URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from django.conf.urls import url
from django.contrib import admin

from . import view
from MyModel import testdb


# it's wired, if we set the two form request with the same url prefix, only one will work, the other will refer to the first one.
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', view.hello),
    url(r'^cond', view.condition),
    url(r'^extend', view.extend_html),
    url(r'^testdb', testdb.testdb),
    url(r'^show', testdb.show),
    url(r'^search_view', testdb.get_form),
    url(r'^search', testdb.get_req),
    url(r'^pp', testdb.search_post),

]
