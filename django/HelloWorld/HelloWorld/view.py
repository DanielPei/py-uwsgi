#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by xiaoqiang.pei on 2018/6/30

import sys
reload(sys)
sys.setdefaultencoding('utf8')

# from django.http import HttpResponse
from django.shortcuts import render


def hello(request):
    # return HttpResponse("Hello World!")
    context = dict()
    context["hello"] = "Hello world!"
    return render(request, "hello.html", context)


def extend_html(request):
    context = dict()
    return render(request, "extend.html", context)


def condition(request):
    cond = request.GET.get('cond', None)
    clause = request.GET.get('clause', None)
    context = dict()

    context["cond"] = cond
    context["clause"] = clause

    items = list()

    for i in xrange(5):
        item = dict()
        item['num'] = i
        item['name'] = "Name_{}".format(i)
        items.append(item)

    context["items"] = items

    return render(request, "condition.html", context)
