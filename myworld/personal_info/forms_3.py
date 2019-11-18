#! /usr/bin/python3
# ! _*_ coding:utf-8 _*_

from django import forms

class Form_3(forms.Form):
    new_nickname = forms.CharField(label='昵称',max_length=10)
    new_username = forms.CharField(label='用户名',max_length=15)
    new_password = forms.CharField(label='用户密码',max_length=20)
    re_new_password = forms.CharField(label='确认密码',max_length=20)