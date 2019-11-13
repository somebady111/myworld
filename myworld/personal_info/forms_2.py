#! /usr/bin/python3
# ! _*_ coding:utf-8 _*_

from django import forms
# 表单2：注册表单,获取注册表单输入数据

class Form_2(forms.Form):
    nickname = forms.CharField(label='昵称',max_length=10)
    username = forms.CharField(label='用户名',max_length=15)
    password = forms.CharField(label='账户密码',max_length=20)
    repassword = forms.CharField(label='确认密码',max_length=20)
