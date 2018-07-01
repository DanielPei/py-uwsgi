#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by xiaoqiang.pei on 2018/7/1
import sys

reload(sys)
sys.setdefaultencoding('utf8')

from models import Test
from django.http import HttpResponse
from django.shortcuts import render_to_response, render
from django.views.decorators import csrf


# 数据库操作
def testdb(request):
    test1 = Test(name="runoob")
    test1.save()
    return HttpResponse("Save data success")


def show(request):
    # 初始化
    response = ""
    response1 = ""

    # 通过objects这个模型管理器的all()获得所有数据行，相当于SQL中的SELECT * FROM
    list = Test.objects.all()

    # filter相当于SQL中的WHERE，可设置条件过滤结果
    response2 = Test.objects.filter(id=1)

    # 获取单个对象
    response3 = Test.objects.get(id=1)

    # 限制返回的数据 相当于 SQL 中的 OFFSET 0 LIMIT 2;
    Test.objects.order_by('name')[0:2]

    # 数据排序
    Test.objects.order_by("id")

    # 上面的方法可以连锁使用
    Test.objects.filter(name="runoob").order_by("id")

    # 输出所有数据
    for var in list:
        response1 += var.name + " "
    response = response1
    return HttpResponse("<p>" + response + "</p>")


def get_form(request):
    return render_to_response('search_form.html')


def search_post(request):
    request.encoding = 'utf-8'
    ctx = {}
    if request.POST:
        ctx['rlt'] = request.POST['q']
    return render(request, "post_form.html", ctx)


# 接收请求数据
def get_req(request):
    request.encoding = 'utf-8'
    if 'q' in request.GET:
        message = '你搜索的内容为 [Get]: ' + request.GET['q']
    else:
        message = '你提交了空表单'
    return HttpResponse(message)


if __name__ == '__main__':
    str = "django.server"
    str = str.decode('utf-8')
    print str
