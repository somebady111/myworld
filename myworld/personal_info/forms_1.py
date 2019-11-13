#! /usr/bin/python3
# ! _*_ coding:utf-8 _*_
# 表单一：登录表单，获取登录表单输入内容，用户名，账户密码

from django import forms

class Form_1(forms.Form):
    username = forms.CharField(label='用户名',max_length=15)
    password = forms.CharField(label='密码',max_length=20)