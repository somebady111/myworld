#! /usr/bin/python3
# ! _*_ coding:utf-8 _*_

# 修改后台的默认展示和不同site的定义
from django.contrib.admin import AdminSite

class CustomSite(AdminSite):
    site_header = 'MyWorld'
    site_title = 'MyWorld管理后台'
    index_title = '首页'

custom_site = CustomSite(name='cus_admin')
